# Show HN: SQL-tap – Real-time SQL traffic viewer for PostgreSQL and MySQL

- Score: 218 | [HN](https://news.ycombinator.com/item?id=47011567) | Link: https://github.com/mickamy/sql-tap

### TL;DR
sql-tap is an open-source SQL traffic viewer that runs as a transparent proxy in front of PostgreSQL/MySQL and streams all queries to a terminal UI. It shows real-time queries, transactions, timing, rows affected, errors, and lets you run/edit EXPLAIN/EXPLAIN ANALYZE from the TUI. Installation is simple (Homebrew, Go, Docker), and you don’t change app code—just point it at the proxy. HN discussion focuses on usefulness for debugging, performance/latency trade-offs of wire-protocol proxies, and comparison with extension-based observability.

---

### Comment pulse
- Devs like it for quick debugging and exploration → feature requests: sort by duration, search/filter, PgUp/PgDn scrolling, and query frequency counts.
- Query-level observability helps understand complex apps and agents → some prefer separate tools (e.g., PGLite-based dbfor.dev) instead of touching production databases directly.
- Transparent proxies add latency and can struggle under high load → extensions + OTEL seen as better for production — counterpoint: proxy is great for ad‑hoc/local debugging and with managed DBs lacking extensions.

---

### LLM perspective
- View: Ideal as a low-friction “stethoscope” for databases during development, not a full observability stack for high-throughput production.
- Impact: Helps app devs, SREs, and LLM/agent builders quickly see ORM/agent behavior and N+1 patterns without code changes.
- Watch next: Benchmarks under load, TLS/credential handling, redaction/anonymization, and potential support for more drivers or extension-based backends.
