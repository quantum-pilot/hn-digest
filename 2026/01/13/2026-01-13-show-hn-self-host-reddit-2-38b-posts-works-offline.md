# Show HN: Self-host Reddit – 2.38B posts, works offline, yours forever

- Score: 193 | [HN](https://news.ycombinator.com/item?id=46602324) | Link: https://github.com/19-84/redd-archiver

### TL;DR

Redd-Archiver converts compressed Reddit, Voat, and Ruqqus dumps into self-hosted archives. It covers 2.38 billion Reddit posts through 2024 plus complete Voat and Ruqqus collections, offering JavaScript-free offline HTML, PostgreSQL full-text search, REST and MCP interfaces, and Docker, HTTPS, Tor, or static deployment. Its streaming pipeline targets multi-terabyte data with bounded memory and resumable processing. HN welcomed preservation and distributed hosting, but split over restoring deleted or protest-overwritten comments: historical utility conflicts with authors’ attempts to withdraw contributions.

### Comment pulse

- Restoring vanished troubleshooting context helps users → old technical answers remain valuable — counterpoint: resurfacing deletions can override an author’s deliberate withdrawal.
- Distributed mirrors improve resilience → registry and team tooling could divide preservation across self-hosters and reduce dependence on one archive.
- Dataset freshness remains operationally hard → monthly dumps may help, but hosts must repeatedly download, split, and reprocess data.

### LLM perspective

- View: The software turns preservation from centralized warehousing into deployable infrastructure, while leaving deletion ethics unresolved.
- Impact: Researchers gain searchable corpora; self-hosters inherit terabytes of storage, moderation, privacy, and maintenance obligations.
- Watch next: Measure import throughput, search latency, update cadence, deletion handling, and cross-instance deduplication at multi-terabyte scale.
