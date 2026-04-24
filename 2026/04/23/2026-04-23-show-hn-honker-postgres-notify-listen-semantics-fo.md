# Show HN: Honker – Postgres NOTIFY/LISTEN Semantics for SQLite

- Score: 222 | [HN](https://news.ycombinator.com/item?id=47874647) | Link: https://github.com/russellromney/honker

## TL;DR
Honker is a SQLite extension (with multi-language bindings) that brings Postgres-style NOTIFY/LISTEN, durable queues, and streams directly into a single SQLite database. It watches the WAL file via cheap `stat(2)` polling (~1 ms cadence) to simulate push-style cross-process notifications without a separate broker or polling queries. Queues, notifications, and streams are just tables, so business writes and side effects can commit atomically and roll back together. Designed for “SQLite as primary DB” apps on a single machine, WAL-only, at-least-once delivery.

## Comment pulse
- Creator: core idea is WAL `stat(2)` polling for cross-process wakeups, giving language-agnostic NOTIFY/LISTEN plus queues/streams fully inside SQLite.
- Some say threaded runtimes (Go/Java/C#) can do intra-process notification themselves → biggest win is for process-concurrency stacks like Python/JS/Ruby — counterpoint: cross-language and multi-process workers still benefit.
- Discussion on alternatives: `PRAGMA data_version`, inotify/kqueue/FSEvents, stored subscriber state; cross-platform quirks (especially macOS) make plain `stat(2)` the most reliable choice.

## LLM perspective
- View: This makes “SQLite + queue + scheduler” a single-file deployment story, reducing operational overhead versus Redis/Celery or Kafka-like stacks.
- Impact: Ideal for small/medium services, edge deployments, and hobby apps standardizing on SQLite and wanting transactional outbox semantics.
- Watch next: real-world production reports, contention/latency benchmarks under heavy load, and higher-level framework integrations or patterns built atop Honker.
