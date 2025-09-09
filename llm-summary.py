# /// script
# dependencies = [
#   "beautifulsoup4",
#   "python-slugify",
#   "requests",
# ]
# ///

import io
import json
import logging
import os
import requests
import sys
from bs4 import BeautifulSoup
from slugify import slugify
from typing import Any, List, Dict
from datetime import datetime, timedelta, timezone
from requests.adapters import HTTPAdapter
from typing import List, Tuple
from urllib3.util.retry import Retry

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

READ_SHORT = 120
READ_LONG  = 300
CLIP_ERROR_CONTENT = 100


with open("SYSTEM_PROMPT.md") as f:
    SYSTEM_PROMPT = f.read().strip()


def _aggregated_stories() -> Dict[str, Any]:
    rr = HTTP.get(
        "https://api.hcker.news/api/timeline?page=1&sort_by=score&filter=top20&limit=100",
        timeout=READ_SHORT,
    )
    if rr.status_code != 200:
        logging.error(f"HN stories fetch failed: {rr.status_code} {rr.text[:CLIP_ERROR_CONTENT]}")
    rr.raise_for_status()
    return rr.json()["stories"]


def _extract_comments(story_id: int, max_children: int = 5):
    r = HTTP.get(
        f"https://news.ycombinator.com/item?id={story_id}",
        headers={"User-Agent": "HN-digest-scraper (contact: lab@waffles.space)"},
        timeout=READ_SHORT,
    )
    if r.status_code != 200:
        logging.error(f"HN comments fetch failed: {r.status_code} {r.text[:CLIP_ERROR_CONTENT]}")
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
            if parent and (d - 1) in collect_depths and len(parent["replies"]) < max_children:
                parent["replies"].append(node)
                if d in collect_depths:
                    last_at_indent[d] = node
            else:
                continue

    return roots


def _make_session():
    s = requests.Session()
    retry = Retry(
        total=3, backoff_factor=0.5,
        status_forcelist=[429, 502, 503, 504, 524],
        allowed_methods=["GET", "POST"]
    )
    s.mount("https://", HTTPAdapter(max_retries=retry))
    s.mount("http://", HTTPAdapter(max_retries=retry))
    return s


MCP_HOST = os.environ["MCP_HOST"]
MCP_TOKEN = os.environ["MCP_TOKEN"]
LITELLM_HOST = os.environ["LITELLM_HOST"]
LITELLM_KEY = os.environ["LITELLM_KEY"]
LITELLM_HEADERS = {"Authorization": f"Bearer {LITELLM_KEY}"}
TAVILY_API_KEY = os.environ["TAVILY_API_KEY"]
HTTP = _make_session()


def _user_msg(title: str, text: str, comments: str) -> str:
    return f"TITLE: {title}\nCONTENT:\n{text}\n\nCOMMENTS:\n{comments}"


def _make_line(custom_id: str, system_prompt: str, user_text: str) -> dict:
    return {
        "custom_id": custom_id,
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "gpt-5-medium-4096",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text},
            ],
        },
    }


def submit_batch_summaries(items: List[str], run_tag: str) -> str:
    lines = []
    for idx, user_msg in enumerate(items, start=1):
        cid = f"hn-{run_tag}-{idx:02d}"
        lines.append(_make_line(cid, SYSTEM_PROMPT, user_msg))

    jsonl_bytes = io.BytesIO()
    for obj in lines:
        jsonl_bytes.write((json.dumps(obj, ensure_ascii=False, indent=None) + "\n").encode("utf-8"))
    jsonl_bytes.seek(0)

    files = {"file": ("hn_batch_"+run_tag+".jsonl", jsonl_bytes, "application/jsonl")}
    data = {"purpose": "batch"}
    r = HTTP.post(f"{LITELLM_HOST}/v1/files", headers=LITELLM_HEADERS, files=files, data=data, timeout=READ_LONG)
    if r.status_code != 200:
        logging.error(f"File upload failed: {r.status_code} {r.text[:CLIP_ERROR_CONTENT]}")
    r.raise_for_status()
    file_id = r.json()["id"]

    payload = {
        "input_file_id": file_id,
        "endpoint": "/v1/chat/completions",
        "completion_window": "24h",
    }
    r = HTTP.post(f"{LITELLM_HOST}/v1/batches", headers={**LITELLM_HEADERS, "Content-Type": "application/json"}, json=payload, timeout=READ_LONG)
    if r.status_code != 200:
        logging.error(f"Batch submission failed: {r.status_code} {r.text[:CLIP_ERROR_CONTENT]}")
    r.raise_for_status()
    return r.json()["id"]


def _webfetch(url: str) -> str:
    rr = HTTP.post(
        f"http://{MCP_HOST}/fetch/fetch",
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {MCP_TOKEN}",
            "Content-Type": "application/json",
        },
        json={
            "max_length": 50_000,
            "raw": False,
            "start_index": 0,
            "url": url,
        },
        timeout=READ_SHORT,
    )
    if rr.status_code != 200:
        logging.error(f"Fetch failed: {rr.status_code} {rr.text[:CLIP_ERROR_CONTENT]}")
        logging.info("Attempting fallback...")
        rr = HTTP.post(
            "https://api.tavily.com/extract",
            headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {TAVILY_API_KEY}",
                "Content-Type": "application/json",
            },
            json={"urls": [url]},
            timeout=READ_LONG,
        )
        if rr.status_code != 200:
            logging.error(f"Tavily fetch failed: {rr.status_code} {rr.text[:CLIP_ERROR_CONTENT]}")
        else:
            return rr.json()["results"][0]["raw_content"]
    rr.raise_for_status()
    return rr.text


def _working_path(name: str) -> Tuple[str, bool]:
    year, month = name.split("-")[:2]
    base_dir = os.path.join(".", year, month)
    if not os.path.isdir(base_dir):
        os.makedirs(base_dir, exist_ok=True)
        return base_dir, False
    return base_dir, os.path.isfile(os.path.join(base_dir, name))


if __name__ == "__main__":
    http = _make_session()
    dt_start = datetime.now()
    utc_yday = (
        (dt_start - timedelta(days=1)).astimezone(timezone.utc).strftime("%Y-%m-%d")
    )
    stories = [
        s for s in _aggregated_stories() if s["utc_day"][:10] == utc_yday
    ]
    stories.sort(key=lambda x: x["score"], reverse=True)

    items = []
    for i, s in enumerate(stories[:20]):
        sid = s["id"]
        title = s["title"]
        url = s.get("url")
        logging.info(f"Processing {i+1}/{len(stories)}: {title} ({sid})")
        filename = f"{utc_yday}-{(slugify(title)[:50] if url else sid)}.md"
        base_dir, exists = _working_path(filename)
        if exists:
            logging.info(f"Skipping already uploaded: {filename}")
            continue

        raw_text = os.path.join(base_dir, filename[:-3] + ".txt")
        if os.path.isfile(raw_text):
            logging.info(f"Loading previously fetched content from {raw_text}...")
            with open(raw_text, "r", encoding="utf-8") as f:
                items.append(f.read())
            continue

        score = s["score"]

        page_content = ""
        hn_link = f"https://news.ycombinator.com/item?id={sid}"
        resolved_url = url or hn_link
        if url:
            try:
                logging.info(f"Fetching article content from {url}...")
                page_content = _webfetch(url)
            except Exception as e:
                logging.error(f"Fetch failed for {url}: {e}")

        comments = ""
        try:
            logging.info(f"Fetching comments for post {sid}...")
            res = _extract_comments(int(sid))
            comments = [(c["text"], [r["text"] for r in c["replies"]]) for c in res]
            concat_replies = lambda replies: "\n" + "\n".join(
                f"    - {r}" for r in replies
            )
            comments = "\n".join(
                f"{i + 1}. {c}{concat_replies(replies)}"
                for i, (c, replies) in enumerate(comments)
            )
        except Exception as e:
            logging.error(f"Comments fetch failed for {hn_link}: {e}")

        user_msg = _user_msg(title, page_content, comments)
        with open(raw_text, "w", encoding="utf-8") as f:
            f.write(user_msg)
        items.append(user_msg)

    if not items:
        logging.info("No new items to process, exiting.")
        sys.exit(0)

    run_tag = utc_yday
    batch_id = submit_batch_summaries(items, run_tag)
    logging.info(f"Submitted batch {batch_id} with {len(items)} items for processing")
    with open(os.path.join("LAST_BATCH_ID.txt"), "w") as f:
        f.write(batch_id)

    # md = f"# {title}\n\n- Score: {score} | [HN]({hn_link}) | Link: {resolved_url}\n\n"
    # if page_content or comments:
    #     try:
    #         logging.info(f"Generating summary for {resolved_url}...")
    #         page_summary = _summarize(title, page_content, comments)
    #         md += "\n" + page_summary + "\n\n"
    #     except Exception as e:
    #         logging.error(f"LLM summary failed: {e}")
