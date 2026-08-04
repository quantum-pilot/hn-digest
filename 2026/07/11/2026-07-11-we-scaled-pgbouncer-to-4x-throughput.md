# We scaled PgBouncer to 4x throughput

- Score: 168 | [HN](https://news.ycombinator.com/item?id=48872874) | Link: https://clickhouse.com/blog/pgbouncer-clickhouse-managed-postgres

### TL;DR

ClickHouse’s Managed Postgres runs one PgBouncer process per core because each process is single-threaded. All workers share one port through SO_REUSEPORT, letting the kernel distribute new connections, while PgBouncer peering forwards cancellation requests to the process owning the target session. Per-process client and database limits are divided so aggregate capacity stays within PostgreSQL’s budget. On identical 16-vCPU AWS poolers, a 16-process fleet reached about 336,000 select-only transactions per second versus a single process’s 87,000 peak, using roughly eight cores before PostgreSQL and the load generator became limiting.

### Comment pulse

- Low concurrency needs no fleet → a single process was slightly faster before one core became the bottleneck.
- Cancellation is the subtle failure mode → SO_REUSEPORT can misroute new cancel connections; built-in PgBouncer peering supplies the required cross-process lookup.
- Alternatives broadened discussion → Odyssey and PgDog offer scalable proxies — counterpoint: operators valued PgBouncer’s maturity, native fit, and repaired prepared-statement support.

### LLM perspective

- **View:** This is horizontal scaling inside one host, preserving PgBouncer semantics while converting idle cores into connection-pooling capacity.
- **Impact:** The pattern postpones proxy replacement and raises throughput without changing client endpoints or PostgreSQL connection budgets.
- **Watch next:** Benchmark mixed queries, TLS, authentication, prepared statements, cross-host deployments, failover, cancellation latency, and fleet-management overhead.
