# The startup's Postgres survival guide

- Score: 299 | [HN](https://news.ycombinator.com/item?id=49005787) | Link: https://hatchet.run/blog/postgres-survival-guide

### TL;DR

Hatchet distills two years of production Postgres battles into startup guidance: design schemas around actual queries, index filters and joins, keep transactions short, use nonblocking migrations and connection pools, inspect plans with EXPLAIN ANALYZE, batch writes, and tune autovacuum before bloat or transaction-ID wraparound. Advanced patterns include FOR UPDATE SKIP LOCKED queues, partitioning, and trigger-backed large-table migrations. Hacker News found it useful but called backups, restore drills, monitoring, and paging conspicuous omissions, while debating UUIDs, ORMs, cascading deletes, explicit locking, and specialized indexes.

### Comment pulse

- Operational survival starts with recovery → commenters prioritized tested backups, point-in-time restore, high availability, monitoring, and pager-connected alerts over deeper query tuning.
- Managed Postgres reduces undifferentiated risk → cloud services bundle backup, restoration, replication, and HA — counterpoint: simple dumps or snapshots suit smaller systems.
- Rules of thumb remain context-dependent → UUID versions, hash versus B-tree indexes, ORMs, cascades, and explicit locks all drew credible objections.

### LLM perspective

- **View:** The guide’s strongest lesson is abstraction leakage: ORM, planner, pooler, and migration tooling eventually demand underlying SQL literacy.
- **Impact:** Startups can postpone specialized infrastructure while building safe escape hatches from ORM, migration, and pooling abstractions.
- **Watch next:** Add a recovery chapter, baseline dashboards and alerts, deadlock ordering guidance, deployment compatibility rules, and representative workload tests.
