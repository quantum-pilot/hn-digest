# Show HN: PgDog – Scale Postgres without changing the app

- Score: 166 | [HN](https://news.ycombinator.com/item?id=47123631) | Link: https://github.com/pgdogdev/pgdog

## TL;DR

PgDog is a Rust-based PostgreSQL proxy that combines connection pooling, load balancing, and transparent sharding so applications can scale without changing database code. It manages schema sync, data movement, logical replication, and traffic cutover, with commands to orchestrate online resharding and rollbacks. It supports broadcasting DDL across shards and is adding two-phase commit for atomic cross-shard operations. Hacker News discussion focuses on how seamlessly it can be adopted later, automation of sharding, and the maturity of reliability features.

---

## Comment pulse

- Can you add PgDog later without downtime? → Yes; use online resharding to migrate from a single Postgres instance to a sharded cluster.
- How are schemas and sharding handled? → PgDog auto-shards, syncs schemas, moves data in parallel, sets up logical replication, and performs traffic cutover.
- Reliability today vs future → 2PC is usable but still needs crash safety; retry-on-failure and transparent failover aren’t implemented yet—counterpoint: maintainers say both are on the near-term roadmap.

---

## LLM perspective

- View: This targets teams that outgrow single-node Postgres but want to avoid Citus-like rewrites or managed-vendor lock-in.
- Impact: Backend engineers get “drop-in” sharding plus pooling, at the cost of trusting a relatively young proxy as critical infrastructure.
- Watch next: Persistence for 2PC logs, automatic safe retries/failover, and real-world benchmarks at high scale will determine production adoption.
