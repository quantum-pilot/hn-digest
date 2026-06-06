# pg_durable: Microsoft open sources in-database durable execution

- Score: 282 | [HN](https://news.ycombinator.com/item?id=48414367) | Link: https://github.com/microsoft/pg_durable

## TL;DR
Microsoft’s pg_durable is a PostgreSQL extension that turns long‑running workflows into SQL-defined, fault‑tolerant “durable functions” executed inside the database. It checkpoints each step, resumes after crashes, and removes the need for ad‑hoc cron jobs, queues, and custom status tables. It targets data-centric teams that already keep state in Postgres and want simpler, auditable background processing. Hacker News discussion focuses on whether workflow logic belongs in the database at all, developer experience concerns, and how this compares to tools like Temporal.

---

## Comment pulse
- Keep workflows in DB vs app code → Some like data locality and fewer services; others prefer versioning, testing, and review workflows centered on application code in Git.
- Fit vs Temporal-style orchestrators → pg_durable is great for Postgres-centric pipelines; less compelling when flows span many external systems — counterpoint: that limit is explicitly documented.
- Semantics and correctness questions → Users probe idempotency, signal timeouts, and error handling; maintainers clarify instance IDs, exactly-once within an instance, and surfacing SQL errors via status.

---

## LLM perspective
- View: This makes Postgres a full workflow runtime for SQL-shaped jobs, not a general Temporal replacement.
- Impact: Strongest for teams already overloading Postgres with queues, cron tables, and ETL scripts.
- Watch next: Tooling for migration/versioning, observability UIs, and benchmarks versus traditional app-layer job queues.
