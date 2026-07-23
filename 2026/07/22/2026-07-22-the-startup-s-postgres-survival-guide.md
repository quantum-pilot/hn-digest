# The startup's Postgres survival guide

- Score: 299 | [HN](https://news.ycombinator.com/item?id=49005787) | Link: https://hatchet.run/blog/postgres-survival-guide

### TL;DR
A founder distills two years of running Postgres in production into a pragmatic survival guide for startups: design schemas around real query patterns, rely heavily on primary-key and compound indexes, keep transactions and locks minimal, and be careful with migrations and connection counts. At higher load, you must understand the query planner, batch writes, and aggressively tune autovacuum to avoid bloat and XID wraparound. Advanced topics include SKIP LOCKED job queues, time-based partitioning, and trigger-driven large table migrations.

---

### Comment pulse
- Backups and HA are underemphasized → many recommend managed services (RDS, CloudSQL) plus pgBackRest/pg_dump and/or volume snapshots for simple, reliable recovery.  
- Indexing/tuning nuances → use uuidv7, hash/GIN/GiST indexes, `EXPLAIN` variants, and test with `seqscan=off` to see future index use.  
- Organizational discipline beats micro-tuning → avoid ORMs or use carefully, keep append-only sources of truth, use explicit schema tooling, and invest early in monitoring/alerting for wraparound—counterpoint: ORMs are worth it for developer productivity.

---

### LLM perspective
- View: Guides like this complement LLM-generated SQL by teaching failure modes (locks, autovacuum) that models easily ignore.  
- Impact: Startup teams can rely on AI for query drafting, but still need humans owning schema, migrations, and operational tuning.  
- Watch next: Tools that auto-suggest indexes, autovacuum settings, and migration plans from live workloads, with “explain plan” visualizations integrated into dev workflows.
