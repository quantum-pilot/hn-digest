# PgDog is funded and coming to a database near you

- Score: 546 | [HN](https://news.ycombinator.com/item?id=48476466) | Link: https://pgdog.dev/blog/our-funding-announcement

### TL;DR

PgDog, a three-person startup building an open-source PostgreSQL proxy for pooling, load balancing, failover, and horizontal sharding, raised $5.5 million. It reports more than 2 million queries per second across dozens of production deployments, over 20 TB sharded, and 1.4 million Docker pulls. The software runs in customer infrastructure; an AWS-oriented enterprise edition will add SLA-backed support. HN welcomed another scaling option but focused on operational gaps: modulo-based shard mapping complicates expansion, high availability often matters more, and sharding still requires application-aware routing and consistency tradeoffs.

### Comment pulse

- Shard growth → Current hash-modulo placement can force full resharding when capacity changes — counterpoint: PgDog plans rendezvous hashing and supports custom routing plugins.
- Operational priority → Several users ranked failover and version upgrades above throughput; Patroni, CloudNativePG, logical replication, and pooler cutovers already address portions.
- Sharding reality → The proxy can split a 4 TB database across smaller nodes, but callers must understand shard routing, cross-shard limits, and consistency.

### LLM perspective

- **View:** Funding buys runway, but database trust will depend on migration safety and failure recovery more than benchmark throughput.
- **Impact:** Teams nearing vertical limits gain another self-hosted option without replacing PostgreSQL or surrendering infrastructure control.
- **Watch next:** Track rendezvous hashing, online resharding, cross-shard semantics, upgrade procedures, failover behavior, production incidents, and independent benchmarks.
