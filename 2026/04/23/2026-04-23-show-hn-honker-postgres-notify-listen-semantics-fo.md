# Show HN: Honker – Postgres NOTIFY/LISTEN Semantics for SQLite

- Score: 222 | [HN](https://news.ycombinator.com/item?id=47874647) | Link: https://github.com/russellromney/honker

### TL;DR

Honker is an experimental SQLite extension and set of language bindings that adds PostgreSQL-style notifications, durable streams, at-least-once queues, retries, scheduling, locks, and rate limits without a separate broker. Messages are rows in the application database, so business writes and enqueues commit or roll back atomically. A shared thread polls WAL size and modification time every millisecond, waking subscribers for indexed reads and yielding roughly 1–2 ms median latency. Hacker News liked the single-file design for small apps but questioned polling alternatives, unnecessary cross-process coordination, broadcast wakeups, and checkpoint behavior.

### Comment pulse

- File-metadata polling cost under 0.1% CPU on one commenter’s hardware and avoids Darwin’s dropped same-process filesystem notifications.
- Single-process apps can use in-memory queues — counterpoint: Honker adds cross-language, cross-process coordination with transactional durability.
- `PRAGMA data_version`, targeted subscriber joins, and WAL-checkpoint handling surfaced as alternatives or open questions; the author had not tested checkpoint behavior.

### LLM perspective

- **View:** The core product is a transactional outbox in one file; WAL watching is merely its wake mechanism.
- **Impact:** Small single-server SQLite stacks can avoid broker operations but inherit single-writer, single-host, and retention constraints.
- **Watch next:** Checkpoint correctness, alpha API changes, many-listener load, false-wakeup cost, and cross-binding compatibility.
