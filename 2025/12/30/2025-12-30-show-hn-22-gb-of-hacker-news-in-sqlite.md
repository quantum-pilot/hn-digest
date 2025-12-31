# Show HN: 22 GB of Hacker News in SQLite

- Score: 261 | [HN](https://news.ycombinator.com/item?id=46435308) | Link: https://hackerbook.dosaygo.com

## TL;DR
WebFetch’s Hacker Book packages the entire 2006–2025 Hacker News corpus (~22 GB of SQLite) as static shards fetched on demand into a browser‑run SQLite/WASM engine. Pages and ad‑hoc SQL queries operate without a server database, streaming only the relevant shard files. Commenters dig into the custom virtual file system approach, compare it to HTTP range–based SQLite/Parquet systems, debate performance and compression limits, and lament that the GitHub repo and up‑to‑date public HN datasets are hard to obtain.

## Comment pulse
- Client-side SQLite via WASM + sharded DB → browser fetches only needed shard files as assets; inspired by sql.js-httpvfs and simple read‑only VFS concepts.  
- Naive queries over all 1,636 shards are slow; filtering to specific shards is fast — counterpoint: smarter VFS and columnar storage could reduce full-scan costs.  
- People joke about compressing repetitive HN comments with custom dictionaries, but also note the repo’s disappearance and difficulty finding recent, comprehensive public HN datasets.

## LLM perspective
- View: Treating huge, mostly-public datasets as static, browser-queryable shards blurs lines between archive, API, and application.  
- Impact: Frontend-heavy apps, data journalists, and archivists gain a pattern for zero-backend exploration of large read-only corpora.  
- Watch next: Benchmarks versus DuckDB/Parquet over HTTP, open-sourcing of the tooling, and whether YC blesses redistribution of the HN dataset.
