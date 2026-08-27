# SQLite concurrency and why you should care about it

- Score: 241 | [HN](https://news.ycombinator.com/item?id=45781298) | Link: https://jellyfin.org/posts/SQLite-locking/

### TL;DR

Jellyfin describes intermittent SQLite lock failures aggravated before version 10.11 by runaway library-scan scheduling and long transactions. Its EF Core solution adds selectable strategies: no locking by default, targeted retries after lock errors, or a reader-writer lock that serializes writes for maximum stability. However, commenters identified important technical errors: WAL permits concurrent readers with one writer, not parallel writes, and SQLite already coordinates multiple processes. They recommended busy timeouts, immediate write transactions, short transactions, and an explicit single-writer architecture before application-level pessimistic locking.

### Comment pulse

- Readers framed SQLITE_BUSY as a predictable transaction-upgrade problem, not an unexplained engine crash.
- One anecdote linked long-lived database slowdown to storage fragmentation, relieved by rewriting the file.
- SQLite remained well regarded, but commenters criticized its compatibility-driven defaults and the article's concurrency explanation.

### LLM perspective

- View: Jellyfin's defensive locks may relieve symptoms, while correct transaction modes address the underlying single-writer model.
- Impact: EF Core applications can trade throughput for reliability, but mistaken WAL assumptions risk unnecessary synchronization.
- Watch next: busy_timeout settings, BEGIN IMMEDIATE, contention telemetry, transaction duration, fragmentation tests, and smart-lock benchmarks.
