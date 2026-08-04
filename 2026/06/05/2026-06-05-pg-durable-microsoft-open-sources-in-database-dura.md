# pg_durable: Microsoft open sources in-database durable execution

- Score: 282 | [HN](https://news.ycombinator.com/item?id=48414367) | Link: https://github.com/microsoft/pg_durable

### TL;DR

Microsoft’s preview pg_durable extension lets PostgreSQL 17 or 18 execute SQL-defined workflow graphs, checkpoint every step, and resume after failures, restarts, or failovers. Its in-process background worker stores orchestration state in Postgres, potentially replacing cron jobs, queues, workers, and status tables for data-local ingestion, maintenance, aggregation, AI, and HTTP workflows. It explicitly does not target low-latency requests or orchestration spanning many heterogeneous systems. HN welcomed fewer moving parts but questioned SQL readability, versioning, debugging, observability, write scaling, and comparisons with general-purpose systems like Temporal.

### Comment pulse

- Data locality can simplify operations → retries, progress, auditing, and backups share PostgreSQL’s existing state and authorization model.
- SQL-shaped orchestration strains developer experience → complex graphs are hard to read, test, debug, release, and evolve through migrations.
- Temporal comparisons overreach → pg_durable favors database-centric work and rejects heterogeneous workflows — counterpoint: that narrower scope may remove substantial glue.

### LLM perspective

- **View:** This is strongest as a transactional job engine, not a universal workflow platform.
- **Impact:** DBAs gain auditable automation; application teams trade infrastructure reduction for deeper database coupling.
- **Watch next:** Preview stability, tooling for Git-based deployment and tracing, idempotent starts, failover benchmarks, and managed-host availability.
