# Many Small Queries Are Efficient in SQLite

- Score: 151 | [HN](https://news.ycombinator.com/item?id=46742635) | Link: https://www.sqlite.org/np1queryprob.html

### TL;DR
SQLite argues that “N+1 queries” and ~200 SQL statements per page are only a problem for client/server databases, where every query pays network round‑trip latency. As an embedded library, SQLite runs in‑process, so many small queries are just cheap function calls and often complete a complex page (like Fossil’s timelines) in under 25 ms. This allows cleaner, modular application code without forced over‑aggregation, while still supporting large complex queries when needed. HN discussion stresses concurrency, migration risk, and write‑path caveats.

---

### Comment pulse
- SQLite excels for typical workloads: embedded, low‑latency, high read performance; can even shard per customer and still federate via foreign data wrappers.  
- But concurrent writers hit SQLite’s limits early; background workers (e.g., Celery) can cause contention, pushing teams to Postgres instead.  
- Designing for hundreds of local queries risks painful rewrites if you later move to a network DB — counterpoint: most projects never need that scale.  
- Core idea: O(N) work is fine; O(N) network calls isn’t. Per‑query overhead, not N, usually dominates performance.  
- Many small SELECTs can be cheap, but many small INSERTs must be grouped in transactions because fsync/durability costs dominate.

---

### LLM perspective
- View: Default to SQLite until clear multi-node, high-concurrency requirements emerge; it delays premature architectural complexity.  
- Impact: Simpler deployments, fewer moving parts, easier local development, but keep an abstraction layer for future network DB migration.  
- Watch next: Tooling for SQLite sharding, online migration to Postgres, and benchmarks clarifying read vs write scalability in real applications.
