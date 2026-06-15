# PgDog is funded and coming to a database near you

- Score: 546 | [HN](https://news.ycombinator.com/item?id=48476466) | Link: https://pgdog.dev/blog/our-funding-announcement

### TL;DR
PgDog is an open-source proxy that adds horizontal scaling, sharding, load balancing, and HA on top of vanilla Postgres. It routes queries across multiple Postgres nodes, aiming to make 100 TB+ tables and 1M+ QPS feasible while keeping standard Postgres semantics and self-hosted control. The team announced $5.5M in funding and production usage at >2M QPS. HN discussion focuses on Postgres’s real pain points (HA and upgrades), sharding strategy trade-offs, and the operational complexity of sharding vs replicas.

---

### Comment pulse
- Postgres pain point = HA and upgrades → many report scaling is fine; downtime-heavy major upgrades and failover are harder than throughput — counterpoint: logical replication and tools like Patroni/CloudNativePG help a lot.  
- Sharding with `hash % num_shards` is criticized → modulo makes rebalancing expensive; people prefer virtual shards / rendezvous; PgDog says rendezvous hashing and custom routing plugins are coming.  
- Sharding use cases debated → PgDog can split a multi‑TB DB across smaller nodes, but apps must be shard-aware; commenters suggest exhausting read replicas and tuning before jumping to sharding.

---

### LLM perspective
- View: PgDog sits between “single-node Postgres” and heavy managed services, packaging sharding/HA without forcing a new database.  
- Impact: Most useful for fast-growing OLTP workloads that hit I/O or memory ceilings yet want to stay on standard Postgres.  
- Watch next: Adoption vs Citus and cloud-native operators, maturity of resharding/HA/upgrade tooling, and credible independent performance/operability benchmarks.
