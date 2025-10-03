# N8n added native persistent storage with DataTables

- Score: 151 | [HN](https://news.ycombinator.com/item?id=45450044) | Link: https://community.n8n.io/t/data-tables-are-here/192256

TL;DR
- n8n added Data Tables (beta) in v1.113: native persistent storage to keep state across workflow runs, dedupe executions, store prompts, and log AI evaluations. There’s a per‑instance cap (adjustable when self‑hosting). The initial release was briefly pulled over a SQLite slowdown, then re‑issued as 1.113.1 (beta) for cloud and self‑host. Early feedback notes missing schema controls (unique/primary keys, type edits), limited table UI, and number formatting quirks. HN responses mix enthusiasm with licensing distrust and comparisons to Node‑RED/Windmill.

Comment pulse
- Licensing risk → VC-backed OSS locks features; users cite MinIO, expect paywalls, move to Node‑RED/Windmill/AutoKitteh — counterpoint: this ships to all plans; self‑host OK.
- Fills a gap → Native state avoids JSON blobs and ad‑hoc DBs; Node‑RED noted for richer global/flow/node state options.
- Platform vs code → Visual flows can become spaghetti; connectors lacking; some prefer code. Others like n8n’s OAuth coverage and quick webhooks.

LLM perspective
- View: Built‑in tables reduce glue code for LLM pipelines: prompt catalogs, run logs, dedupe state, simple caches.
- Impact: Good for lightweight state and evaluation logs; complex pipelines should still rely on dedicated databases and queueing.
- Watch next: Benchmarks under concurrent load; clear multi-worker semantics; programmatic schema management; roadmap on licensing and GA timeline.
