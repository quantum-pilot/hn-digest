# SQLite concurrency and why you should care about it

- Score: 241 | [HN](https://news.ycombinator.com/item?id=45781298) | Link: https://jellyfin.org/posts/SQLite-locking/

- TL;DR
    - Jellyfin explains intermittent SQLite “database locked” crashes tied to heavy parallel writes and long transactions. They now use EF Core interceptors to add configurable locking: default no-lock, optimistic retries with Polly, or pessimistic single-writer via ReaderWriterLockSlim. WAL helps readers but doesn’t eliminate write contention. Initial tests stabilized affected systems; root cause remains unclear. HN discussion critiques their WAL explanation, emphasizes SQLite’s single-writer model, and shares practical fixes and maintenance tips for aging databases.

- Comment pulse
    - Design for one writer → SQLite in WAL is single-writer/multi-reader; enforce a write queue, set busy_timeout, and use BEGIN IMMEDIATE to avoid upgrade deadlocks.
    - Article overstates WAL concurrency → WAL doesn’t permit multiple writers; SQLite already locks files — counterpoint: app-level interceptors can still reduce self-inflicted contention.
    - Aged DBs slow or lock → Fragmentation observed; copying file or running VACUUM can defragment and restore performance on long-lived devices.

- LLM perspective
    - View: Treat SQLite as embedded, single-writer; Jellyfin’s interceptors formalize this in EF Core with configurable cost/stability tradeoffs.
    - Impact: Users on flaky systems gain reliability; developers get a drop-in pattern without invasive code changes.
    - Watch next: Publish benchmarks across modes, default sane PRAGMAs, reproduction harness for SQLITE_BUSY, and guidance on VACUUM/maintenance schedules.
