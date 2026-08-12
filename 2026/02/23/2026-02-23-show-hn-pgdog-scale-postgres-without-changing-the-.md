# Show HN: PgDog – Scale Postgres without changing the app

- Score: 166 | [HN](https://news.ycombinator.com/item?id=47123631) | Link: https://github.com/pgdogdev/pgdog

### TL;DR

PgDog is an AGPL PostgreSQL proxy that combines connection pooling, load balancing, and database sharding. Its latest work adds an online resharding workflow that coordinates schema synchronization, parallel data copying, logical replication, traffic cutover, and reverse replication for rollback, with administrative progress controls. The author says teams can begin with ordinary PostgreSQL and add PgDog later. Commenters welcomed the integrated approach, but highlighted maturity gaps: production sharding experience remains limited, backend retries are absent, and two-phase commit still lacks durable crash recovery.

### Comment pulse

- Broadcasting DDL across shards can run in parallel, and two-phase commit can make changes atomic.
- Zero-downtime resharding is the goal; discussion and repository activity suggest the feature is new enough to warrant cautious validation.
- Retry logic must avoid replaying statements inside transactions, making safe backend failover more complicated than simple reconnection.

### LLM perspective

- **View:** Rollback engineering is the differentiator: copying rows is easier than preserving correctness while traffic and schemas change.
- **Impact:** Teams can postpone sharding decisions, but the proxy becomes a critical state coordinator during migration.
- **Watch next:** Crash-recovery tests, write-conflict handling, retry semantics, production reshardings, replication lag, and two-phase-commit durability.
