# SQLite is all you need for durable workflows

- Score: 310 | [HN](https://news.ycombinator.com/item?id=48326802) | Link: https://obeli.sk/blog/sqlite-is-all-you-need-for-durable-workflows/

### TL;DR

Obelisk argues durable workflows need durable state, not durable compute: keep each agent or tenant’s replay log in a local SQLite file, run disposable workers, and asynchronously replicate changes with Litestream to S3-compatible storage. This removes network hops and database-service operations while making execution easy to replay, inspect, migrate, and isolate. The author recommends Postgres when high availability, shared scaling, or stronger replication guarantees matter, because Litestream can lose recent writes. HN debated SQLite’s production concurrency and weak typing, with defenders emphasizing partitioned workloads, simplicity, and substantial single-node capacity.

### Comment pulse

- SQLite’s fit depends on partitioning → one file per agent or tenant avoids multi-writer coordination and strengthens fault isolation.
- Production suitability polarized readers → critics cited concurrency and HA limits — counterpoint: defenders reported high single-node throughput with far less operational complexity.
- Ergonomics remain uneven → strict tables, WAL, foreign keys, timeouts, and constraints mitigate SQLite’s permissive defaults, while DuckDB better serves analytical scripts.

### LLM perspective

- **View:** The architecture is strongest when workflow state is naturally sharded and occasional recovery-point loss is acceptable.
- **Impact:** Agent platforms can replace shared orchestration infrastructure with cheap isolated runtimes, reducing cost and blast radius.
- **Watch next:** Recovery-point measurements, concurrent-writer benchmarks, restore automation, corruption drills, observability tooling, and migration paths to Postgres.
