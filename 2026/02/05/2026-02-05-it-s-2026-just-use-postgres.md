# It's 2026, Just Use Postgres

- Score: 519 | [HN](https://news.ycombinator.com/item?id=46905555) | Link: https://www.tigerdata.com/blog/its-2026-just-use-postgres

### TL;DR
The article argues that most teams should consolidate on PostgreSQL plus extensions instead of running a zoo of specialized databases (Elasticsearch, Pinecone, Redis, MongoDB, Kafka, InfluxDB, etc.). It claims modern Postgres extensions implement essentially the same algorithms (BM25, HNSW/DiskANN, time-partitioning, PostGIS) while avoiding synchronization, operational overhead, and AI-era pains like cloning multi-database test environments. HN commenters broadly like Postgres-as-default, but push back on “one database for everything,” stressing scale limits, cost-effectiveness of purpose-built systems, and the ongoing appeal of SQLite for simplicity.

---

### Comment pulse
- Postgres as default → Many read the slogan as “start with Postgres, switch when you hit real limits,” not literal “never use anything else.”  
- Specialization vs ops cost → Purpose-built systems (ClickHouse, Redis, Pinecone, etc.) can be cheaper and better at scale—counterpoint: you only know you need them once Postgres actually struggles.  
- Simplicity spectrum → Postgres is powerful but operationally heavy; SQLite stays unbeatable for ultra-simple or local use—counterpoint: some quickly hit SQLite’s limits and prefer a small, boring Postgres instance.

---

### LLM perspective
- View: For AI-heavy stacks, minimizing database count meaningfully reduces orchestration, cloning, and consistency complexity for agents and pipelines.  
- Impact: Early-stage teams and solo developers benefit most from “Postgres-first,” while large orgs can afford polyglot data platforms.  
- Watch next: Independent benchmarks comparing PG extensions vs specialized systems under realistic, mixed workloads and TCO, not just microbenchmarks or vendor marketing.
