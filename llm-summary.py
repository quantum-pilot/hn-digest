# /// script
# dependencies = [
#   "beautifulsoup4",
#   "python-slugify",
#   "requests",
# ]
# ///

import base64
import io
import json
import logging
import os
import re
import requests
import subprocess
import sys
import uuid
from bs4 import BeautifulSoup
from slugify import slugify
from typing import Any, List, Dict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from requests.adapters import HTTPAdapter
from typing import List, Tuple
from urllib.parse import urlparse
from urllib3.util.retry import Retry

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

READ_TIMEOUT = 250
CLIP_ERROR_CONTENT = 200
STORIES_PER_DAY = 20

BATCH_REF_FILE = "LAST_BATCH_ID.txt"
STATE_DIR = Path(os.environ.get("HN_DIGEST_STATE_DIR", ".hn-state"))
FORCE_PAGE = "1"
FORCE_UTC_DAY = None
args = sys.argv[1:]
if args:
    FORCE_PAGE = int(args[0])
    FORCE_UTC_DAY = args[1]


with open("SYSTEM_PROMPT.md") as f:
    SYSTEM_PROMPT = f.read().strip()


def notify(msg: str):
    resp = HTTP.post(
        f"http://{os.environ['APPRISE_HOST']}/notify/{os.environ['APPRISE_HN_NOTIFY_KEY']}",
        data={"body": msg, "tags": "all"},
        timeout=READ_TIMEOUT,
    )
    if resp.status_code != 200:
        logging.error(f"Notification failed: {resp.status_code} {resp.text[:CLIP_ERROR_CONTENT]}")


def _aggregated_stories() -> Dict[str, Any]:
    rr = HTTP.get(
        f"https://api.hcker.news/api/timeline?page={FORCE_PAGE}&sort_by=score&filter=top20&limit=500",
        timeout=READ_TIMEOUT,
    )
    if rr.status_code != 200:
        logging.error(
            f"HN stories fetch failed: {rr.status_code} {rr.text[:CLIP_ERROR_CONTENT]}"
        )
    rr.raise_for_status()
    return rr.json()["stories"]


def _extract_comments(story_id: int, max_children: int = 5):
    r = HTTP.get(
        f"https://news.ycombinator.com/item?id={story_id}",
        headers={"User-Agent": "HN-digest-scraper (contact: lab@waffles.space)"},
        timeout=READ_TIMEOUT,
    )
    if r.status_code != 200:
        logging.error(
            f"HN comments fetch failed: {r.status_code} {r.text[:CLIP_ERROR_CONTENT]}"
        )
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    rows = soup.select("tr.athing.comtr")

    def extract(row):
        def get_indent() -> int:
            ind = row.select_one("td.ind")
            if ind is None:
                return 0
            return int(ind["indent"])

        default = row.select_one("td.default")
        comhead = default.select_one(".comhead") if default else None
        author_el = comhead.select_one(".hnuser") if comhead else None
        text_el = default.select_one(".commtext") if default else None

        return {
            "author": author_el.get_text(strip=True) if author_el else None,
            "text": text_el.get_text(" ", strip=True) if text_el else "",
            "indent": get_indent(),
            "replies": [],
        }

    roots: list[dict] = []
    collect_depths = (0,)
    last_at_indent: dict[int, dict] = {}

    for row in rows:
        node = extract(row)
        d = node["indent"]

        for k in list(last_at_indent.keys()):
            if k > d:
                last_at_indent.pop(k, None)

        if d == 0:
            if len(roots) < max_children:
                roots.append(node)
                if 0 in collect_depths:
                    last_at_indent[0] = node
            else:
                break
        else:
            parent = last_at_indent.get(d - 1)
            if (
                parent
                and (d - 1) in collect_depths
                and len(parent["replies"]) < max_children
            ):
                parent["replies"].append(node)
                if d in collect_depths:
                    last_at_indent[d] = node
            else:
                continue

    comments = [(c["text"], [r["text"] for r in c["replies"]]) for c in roots]
    concat_replies = lambda replies: "\n" + "\n".join(f"    - {r}" for r in replies)
    return "\n".join(
        f"{i + 1}. {c}{concat_replies(replies)}"
        for i, (c, replies) in enumerate(comments)
    )


def _make_session():
    s = requests.Session()
    retry = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=[429, 502, 503, 504, 524],
        allowed_methods=["GET", "POST"],
    )
    s.mount("https://", HTTPAdapter(max_retries=retry))
    s.mount("http://", HTTPAdapter(max_retries=retry))
    return s


MCP_HOST = os.environ["MCP_HOST"]
MCP_TOKEN = os.environ["MCP_TOKEN"]
LITELLM_HOST = os.environ["LITELLM_HOST"]
LITELLM_KEY = os.environ["LITELLM_KEY"]
LITELLM_MODEL = "gpt-5.1-medium-4096"
LITELLM_HEADERS = {"Authorization": f"Bearer {LITELLM_KEY}"}
HTTP = _make_session()


def _user_msg(title: str, text: str, comments: str) -> str:
    return f"TITLE: {title}\nCONTENT:\n{text}\n\nCOMMENTS:\n{comments}"


def _make_line(custom_id: str, system_prompt: str, user_text: str) -> dict:
    return {
        "custom_id": custom_id,
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "gpt-5",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text},
            ],
            "reasoning_effort": "medium",
            "verbosity": "medium",
        },
    }


def _make_request_id(run_tag: str, index: int) -> str:
    return f"{run_tag}-{uuid.uuid4().hex[:16]}-{index:02d}"


def submit_batch_summaries(items: List[Tuple[str, str]], run_tag: str) -> Tuple[str, List[Dict[str, str]]]:
    lines = []
    requests = []
    for index, (filename, user_msg) in enumerate(items):
        custom_id = _make_request_id(run_tag, index)
        requests.append({"custom_id": custom_id, "filename": filename})
        lines.append(_make_line(custom_id, SYSTEM_PROMPT, user_msg))

    jsonl_bytes = io.BytesIO()
    for obj in lines:
        jsonl_bytes.write(
            (json.dumps(obj, ensure_ascii=False, indent=None) + "\n").encode("utf-8")
        )
    jsonl_bytes.seek(0)

    files = {
        "file": ("hn_batch_" + run_tag + ".jsonl", jsonl_bytes, "application/jsonl")
    }
    r = HTTP.post(
        f"http://{LITELLM_HOST}/v1/files",
        headers=LITELLM_HEADERS,
        files=files,
        data={"purpose": "batch", "target_model_names": LITELLM_MODEL},
        timeout=READ_TIMEOUT,
    )
    if r.status_code != 200:
        logging.error(
            f"File upload failed: {r.status_code} {r.text[:CLIP_ERROR_CONTENT]}"
        )
    r.raise_for_status()
    file_id = r.json()["id"]

    payload = {
        "input_file_id": file_id,
        "endpoint": "/v1/chat/completions",
        "completion_window": "24h",
    }
    r = HTTP.post(
        f"http://{LITELLM_HOST}/v1/batches",
        headers={**LITELLM_HEADERS, "Content-Type": "application/json"},
        json=payload,
        timeout=READ_TIMEOUT,
    )
    if r.status_code != 200:
        logging.error(
            f"Batch submission failed: {r.status_code} {r.text[:CLIP_ERROR_CONTENT]}"
        )
    r.raise_for_status()
    resp = r.json()
    logging.info(f"Batch submission: {resp}")
    return resp["id"], requests


def _webfetch(url: str) -> str:
    rr = HTTP.post(
        f"http://{MCP_HOST}/fetch/fetch",
        headers={
            "Authorization": f"Bearer {MCP_TOKEN}",
            "Content-Type": "application/json",
        },
        json={"url": url},
        timeout=READ_TIMEOUT,
    )
    if rr.status_code != 200:
        logging.error(f"Fetch failed: {rr.status_code} {rr.text[:CLIP_ERROR_CONTENT]}")
    rr.raise_for_status()
    return rr.text.replace("\\n", "\n")


def _fetch_file(out_file_id: str):
    out_resp = HTTP.get(
        f"http://{LITELLM_HOST}/openai-file-content-proxy/{out_file_id}/content",
        headers=LITELLM_HEADERS,
        timeout=READ_TIMEOUT,
    )
    if out_resp.status_code != 200:
        logging.error(
            f"Output fetch failed: {out_resp.status_code} {out_resp.text[:CLIP_ERROR_CONTENT]}"
        )
    out_resp.raise_for_status()
    return out_resp.text


def _working_path(name: str) -> Tuple[str, bool]:
    year, month, day = name.split("-")[:3]
    base_dir = os.path.join(".", year, month, day)
    fpath = os.path.join(base_dir, name)
    if not os.path.isdir(base_dir):
        os.makedirs(base_dir, exist_ok=True)
    return base_dir, fpath, os.path.isfile(fpath)


def _story_filename(utc_day: str, story: Dict[str, Any]) -> str:
    url = story.get("url")
    suffix = slugify(story["title"])[:50] if url else story["id"]
    return f"{utc_day}-{suffix}.md"


def _day_state_path(utc_day: str) -> Path:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    return STATE_DIR / f"{utc_day}.json"


def _read_day_state(utc_day: str):
    path = _day_state_path(utc_day)
    if not path.is_file():
        return None
    return json.loads(path.read_text())


def _write_day_state(state: Dict[str, Any]) -> None:
    path = _day_state_path(state["day"])
    tmp_path = path.with_suffix(".tmp")
    tmp_path.write_text(json.dumps(state, ensure_ascii=False, sort_keys=True))
    tmp_path.replace(path)


def _new_day_state(utc_day: str, target_files: List[str]) -> Dict[str, Any]:
    return {
        "version": 1,
        "day": utc_day,
        "target_files": target_files,
        "completed_files": [],
        "complete": False,
    }


def _mark_day_completed(utc_day: str, completed_files: set[str]) -> None:
    state = _read_day_state(utc_day)
    if not state:
        state = _new_day_state(utc_day, sorted(completed_files))
    state["completed_files"] = sorted(set(state.get("completed_files", [])) | completed_files)
    target_files = set(state.get("target_files", []))
    state["complete"] = bool(target_files) and target_files.issubset(set(state["completed_files"]))
    _write_day_state(state)


def _existing_digest_files(utc_day: str) -> set[str]:
    base_dir, _, _ = _working_path(f"{utc_day}-probe.md")
    return {p.name for p in Path(base_dir).glob(f"{utc_day}-*.md")}


def _git(*args: str) -> None:
    logging.info("Running git %s", " ".join(args))
    subprocess.run(["git", *args], check=True)


def _has_git_changes() -> bool:
    proc = subprocess.run(
        ["git", "status", "--porcelain"],
        check=True,
        capture_output=True,
        text=True,
    )
    return bool(proc.stdout.strip())


def _read_batch_ref(ref_file: Path):
    raw = ref_file.read_text().strip()
    if not raw:
        return None
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return {"batch_id": raw, "items": None}
    if isinstance(data, dict) and data.get("batch_id"):
        return data
    raise ValueError(f"Unexpected batch ref format in {ref_file}: {raw[:CLIP_ERROR_CONTENT]}")


def _write_batch_ref(ref_file: Path, batch_id: str, requests: List[Dict[str, str]]) -> None:
    ref_file.write_text(
        json.dumps(
            {"batch_id": batch_id, "requests": requests},
            ensure_ascii=False,
        )
    )


def _request_filename_map(batch_ref: Dict[str, Any]) -> Dict[str, str]:
    requests = batch_ref.get("requests")
    if requests:
        return {r["custom_id"]: r["filename"] for r in requests}

    legacy_items = batch_ref.get("items")
    if legacy_items:
        mapping = {}
        for item in legacy_items:
            if isinstance(item, dict):
                mapping[item["custom_id"]] = item["filename"]
            else:
                mapping[item] = item
        return mapping

    return {}


def _batch_filenames(ref_file: Path, batch_ref: Dict[str, Any]) -> set[str]:
    mapping = _request_filename_map(batch_ref)
    if mapping:
        return set(mapping.values())
    return {md_path.name for md_path in Path(ref_file.parent).rglob("*.md")}


def _check_batch(ref_file: Path, batch_ref: Dict[str, Any]):
    batch_id = batch_ref["batch_id"]
    utc_day = ref_file.name[:10]
    rr = HTTP.get(
        f"http://{LITELLM_HOST}/v1/batches/{batch_id}",
        headers=LITELLM_HEADERS,
        timeout=READ_TIMEOUT,
    )
    if rr.status_code != 200:
        logging.error(
            f"Batch status fetch failed: {rr.status_code} {rr.text[:CLIP_ERROR_CONTENT]}"
        )
    rr.raise_for_status()
    batch = rr.json()
    status = batch.get("status")
    if status not in ("completed", "expired"):
        logging.info(f"Batch {batch_id} pending: {batch}")
        return

    notify(f"Batch for {ref_file.parent} {status}, processing results...")
    request_to_filename = _request_filename_map(batch_ref)
    errorred = []
    if batch.get("error_file_id"):
        notify(f"Batch for {ref_file.parent} has errors, checking...")
        output = _fetch_file(batch["error_file_id"])
        for line in output.splitlines():
            entry = json.loads(line)
            filename = request_to_filename.get(entry["custom_id"], entry["custom_id"])
            errorred.append(filename)

    litellm_out = base64.b64decode(batch["output_file_id"]).decode("utf-8")
    out_file_id = list(
        filter(lambda s: s.startswith("llm_output_file_id,"), litellm_out.split(";"))
    )[0].split(",")[-1]
    assert out_file_id.startswith("file-"), f"Unexpected output file id: {out_file_id}"

    unfinished_items = _batch_filenames(ref_file, batch_ref)
    completed_now = set()

    for line in _fetch_file(out_file_id).splitlines():
        entry = json.loads(line)
        filename = request_to_filename.get(entry["custom_id"], entry["custom_id"])
        _, filepath, exists = _working_path(filename)
        write_mode = "a" if exists else "w"
        if not exists:
            logging.warning(f"Creating missing output file: {filename}")
        resp = entry.get("response", {})
        if resp.get("status_code") == 200:
            txt = resp["body"]["choices"][0]["message"]["content"]
            with open(filepath, write_mode, encoding="utf-8") as f:
                f.write(txt + "\n")
            unfinished_items.discard(filename)
            completed_now.add(filename)
            _git("add", filepath)
        else:
            logging.error(f"Batch item failed for {filename}: {resp}")
            errorred.append(filename)

    os.remove(ref_file)
    if _has_git_changes():
        _git("commit", "-m", ref_file.name[:10])
        _git("push", "origin", "master")
        notify(f"Digest ready for {ref_file.parent}: https://github.com/quantum-pilot/hn-digest/tree/master/{ref_file.parent}")
    else:
        logging.info(f"No git changes for {ref_file.parent}.")

    if completed_now:
        _mark_day_completed(utc_day, completed_now)

    items = []
    for filename in sorted(set(errorred) | unfinished_items):
        _, filepath, _ = _working_path(filename)
        raw_text = filepath[:-3] + ".txt"
        with open(raw_text, "r", encoding="utf-8") as f:
            items.append((filename, f.read()))
    if items:
        notify(f"Resubmitting {len(items)} errored items from batch for {ref_file.parent}...")
        new_batch_id, requests = submit_batch_summaries(items, items[0][0][:10])
        _write_batch_ref(ref_file, new_batch_id, requests)
    else:
        state = _read_day_state(utc_day)
        if state and state.get("complete"):
            logging.info(f"Day {utc_day} is complete; future rank drift will be ignored.")


def _prepare_item(utc_yday: str, story: Dict[str, Any]) -> Tuple[str, str]:
    sid = story["id"]
    title = story["title"]
    url = story.get("url")
    score = story["score"]
    filename = _story_filename(utc_yday, story)
    _, filepath, _ = _working_path(filename)

    hn_link = f"https://news.ycombinator.com/item?id={sid}"
    resolved_url = url or hn_link
    md = f"# {title}\n\n- Score: {score} | [HN]({hn_link}) | Link: {resolved_url}\n\n"
    if not os.path.exists(filepath):
        logging.info(f"Writing summary file to {filepath}...")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md)

    raw_text = filepath[:-3] + ".txt"
    if os.path.isfile(raw_text):
        logging.info(f"Loading previously fetched content from {raw_text}...")
        with open(raw_text, "r", encoding="utf-8") as f:
            return filename, f.read()

    page_content = ""
    if url:
        try:
            logging.info(f"Fetching article content from {url}...")
            page_content = _webfetch(url)
        except Exception as e:
            logging.error(f"Fetch failed for {url}: {e}")

    comments = ""
    try:
        logging.info(f"Fetching comments for post {sid}...")
        comments = _extract_comments(int(sid))
        if story.get("merged_comments"):
            comments += f"\n\nMore comments: \n{story['merged_comments']}"
    except Exception as e:
        logging.error(f"Comments fetch failed for {hn_link}: {e}")

    user_msg = _user_msg(title, page_content, comments)
    with open(raw_text, "w", encoding="utf-8") as f:
        f.write(user_msg)
    return filename, user_msg


def _process_day(utc_yday: str, stories: List[Dict[str, Any]]):
    assert len(stories) == STORIES_PER_DAY, (
        f"Expected {STORIES_PER_DAY} stories, got {len(stories)}"
    )
    stories.sort(key=lambda x: x["score"], reverse=True)

    # special case: 2025-09-16 had two identical URLs topping the list
    cleaned = {}
    titles = {}
    for s in stories:
        url = s.get("url")
        title = s["title"]
        title_slug = slugify(title)
        if re.search("ask hn: who is hiring", title.lower()):
            logging.info(f"Skipping hiring post: {title} ({s['id']})")
            continue
        if url:
            u = urlparse(url)
            if (u.netloc, u.path) in cleaned:
                logging.info(f"Skipping duplicate URL: {url}")
                cleaned[(u.netloc, u.path)]["merged_comments"] = _extract_comments(
                    int(s.get("id"))
                )
                continue
            cleaned_key = (u.netloc, u.path)
            cleaned[cleaned_key] = s
            if title_slug in titles:
                # special case: 2025-12-26 had two posts with same content and titles
                # but different URLs topping the list
                ignoring = None
                if cleaned[titles[title_slug]]["score"] > s["score"]:
                    ignoring = cleaned.pop(cleaned_key)
                    cleaned_key = titles[title_slug]
                else:
                    ignoring = cleaned.pop(titles[title_slug])
                logging.info(f"Skipping duplicate title: {title} ({s.get('url')}) with score {ignoring['score']}")
            titles[title_slug] = cleaned_key
        else:
            cleaned[s["id"]] = s

    stories = list(cleaned.values())
    story_by_filename = {_story_filename(utc_yday, s): s for s in stories}
    current_targets = list(story_by_filename.keys())

    _, current_ref_file, ref_exists = _working_path(f"{utc_yday}-{BATCH_REF_FILE}")
    state = _read_day_state(utc_yday)

    if state and state.get("complete"):
        logging.info(f"Day {utc_yday} is already complete; ignoring current rank changes.")
        return

    if ref_exists:
        logging.info(f"Ref file already exists: {current_ref_file}; waiting for existing batch.")
        return

    if not state:
        existing_files = _existing_digest_files(utc_yday)
        if len(existing_files) >= STORIES_PER_DAY:
            state = _new_day_state(utc_yday, sorted(existing_files))
            state["completed_files"] = sorted(existing_files)
            state["complete"] = True
            _write_day_state(state)
            logging.info(f"Bootstrapped completed state for {utc_yday} from {len(existing_files)} existing files.")
            return

        state = _new_day_state(utc_yday, current_targets)
        _write_day_state(state)
        logging.info(f"Initialized target set for {utc_yday} with {len(current_targets)} items.")

    target_files = list(state.get("target_files", []))
    completed_files = set(state.get("completed_files", []))
    remaining_files = [filename for filename in target_files if filename not in completed_files]

    items = []
    for filename in remaining_files:
        _, filepath, _ = _working_path(filename)
        raw_text = filepath[:-3] + ".txt"
        if os.path.isfile(raw_text):
            logging.info(f"Loading previously fetched content from {raw_text}...")
            with open(raw_text, "r", encoding="utf-8") as f:
                items.append((filename, f.read()))
            continue
        if filename in story_by_filename:
            story = story_by_filename[filename]
            logging.info(f"Preparing target item: {story['title']} ({story['id']})")
            items.append(_prepare_item(utc_yday, story))
            continue
        logging.error(f"Missing raw input for frozen target {filename}; current ranks no longer include it.")

    if not items:
        logging.info(f"No incomplete target items to process for {utc_yday}.")
        return

    if len(items) != len(target_files):
        logging.info(f"Submitting {len(items)} incomplete target items for {utc_yday}; {len(target_files) - len(items)} already completed.")

    notify(f"Submitting batch for {utc_yday}.")
    batch_id, requests = submit_batch_summaries(items, utc_yday)
    _write_batch_ref(Path(current_ref_file), batch_id, requests)


if __name__ == "__main__":
    http = _make_session()
    dt_start = datetime.now()
    utc_yday = (
        (dt_start - timedelta(days=1)).astimezone(timezone.utc).strftime("%Y-%m-%d")
    )
    if FORCE_UTC_DAY:
        utc_yday = FORCE_UTC_DAY
    all_stories = _aggregated_stories()
    for day in utc_yday.split(","):
        logging.info(f"Processing day: {day}")
        stories = [s for s in all_stories if s["utc_day"][:10] == day]
        _process_day(day, stories)

    for ref in Path(".").rglob(f"*{BATCH_REF_FILE}"):
        logging.info(f"Checking ref file: {ref}")
        batch_ref = _read_batch_ref(ref)
        if batch_ref:
            _check_batch(ref, batch_ref)
        else:
            logging.info(f"Removed empty ref file: {ref}")
            os.remove(ref)
