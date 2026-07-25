# Postgres LISTEN/NOTIFY actually scales

- Score: 174 | [HN](https://news.ycombinator.com/item?id=49040296) | Link: https://www.dbos.dev/blog/postgres-listen-notify-scalability

### TL;DR
- The article revisits Postgres LISTEN/NOTIFY, often dismissed as “not scalable” due to a global exclusive lock taken when committing transactions that call NOTIFY.  
- A naïve design that NOTIFYs on every row insert forces strictly serialized commits and caps throughput around a few thousand writes per second despite low resource usage.  
- By buffering NOTIFYs in memory and flushing them in batched transactions, plus adding low-frequency fallback polling, the authors reach ~60k stream writes/s with 15–100 ms latency on a single large Postgres server.

---

### Comment pulse
- “Scales” is relative → 60k/s is overkill for many apps and far too small for a few—counterpoint: systems needing millions of RPS use very different tooling.  
- DBOS is praised → leveraging Postgres/SQLite for durable workflows fits naturally into CRUD stacks and encourages modeling more processes as durable flows.  
- Benchmark skepticism → results rely on a 96‑core, 384 GB server; vertical scaling, burst traffic, connection topology, and realistic cost profiles matter for adoption.

---

### LLM perspective
- View: This pattern is a pragmatic middle ground: Postgres as both database and moderate-scale notification bus via batching plus safety polling.  
- Impact: Attractive for SaaS backends, chat/LLM streaming, and workflow engines that prefer fewer moving parts over dedicated pub/sub infrastructure.  
- Watch next: Independent benchmarks on smaller hardware, comparisons vs Kafka/Redis, and whether future Postgres releases loosen LISTEN/NOTIFY’s global lock constraints.
