# 100k TPS over a billion rows: the unreasonable effectiveness of SQLite

- Score: 252 | [HN](https://news.ycombinator.com/item?id=46124205) | Link: https://andersmurphy.com/2025/12/02/100000-tps-over-a-billion-rows-the-unreasonable-effectiveness-of-sqlite.html

### TL;DR
The post benchmarks interactive, contention-heavy transactions over a billion-row accounts table, comparing networked Postgres to embedded SQLite. Once realistic network latency (5–10 ms) and serializable isolation are added, Postgres collapses from ~13k TPS on-box to a few hundred TPS because locks are held across the network and Amdahl’s law dominates. SQLite, embedded in the app, avoids network hops and uses a single-writer plus batching and savepoints to hit ~100k TPS while preserving per-transaction rollback, illustrating how architecture often matters more than database brand.

---

### Comment pulse
- SQLite as embedded workhorse → In-memory or WAL-backed setups give ultra-fast CRUD and cheap backups; many workloads don’t need heavyweight servers.  
- Scale-up vs scale-out → Modern single machines (tens of TB RAM, 100s of cores) give huge headroom, but elasticity and resilience to host failure remain concerns.  
- Fairness of comparison → Critics say “local SQLite vs remote Postgres” is apples-to-oranges—counterpoint: article’s core lesson is avoiding unnecessary network boundaries.

---

### LLM perspective
- View: First decide if you truly need a remote DB; if not, embedded SQLite can radically simplify and accelerate systems.  
- Impact: Small/medium SaaS, internal tools, and edge/desktop apps can delay or avoid complex DB clusters and ops overhead.  
- Watch next: Better SQLite-based services (queuing, sharding, replication) and honest benchmarks of “local Postgres vs embedded SQLite” under real app workloads.
