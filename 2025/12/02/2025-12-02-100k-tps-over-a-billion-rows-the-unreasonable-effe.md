# 100k TPS over a billion rows: the unreasonable effectiveness of SQLite

- Score: 252 | [HN](https://news.ycombinator.com/item?id=46124205) | Link: https://andersmurphy.com/2025/12/02/100000-tps-over-a-billion-rows-the-unreasonable-effectiveness-of-sqlite.html

### TL;DR

A billion-row benchmark on an M1 Pro measured SQLite at 44,096 interactive transactions per second, rising to 186,157 with dynamic batching and 121,922 with savepoints; a mixed 75/25 read-write workload reached 102,545. Local PostgreSQL reached 13,756, then fell sharply with simulated latency and serializable contention. The author’s narrower lesson is architectural: embedding the database removes network round trips and enables a single writer to batch work. Commenters stressed that SQLite and PostgreSQL often solve different deployment problems.

### Comment pulse

- SQLite enthusiasm → embedded deployment can simplify operations and accelerate local workloads — counterpoint: PostgreSQL serves fundamentally different distributed needs.
- Benchmark skepticism → topology, durability choices, and contention assumptions matter more than headline TPS.

### LLM perspective

- View: The compelling result is batching across an embedded boundary, not a universal SQLite victory.
- Impact: Monolithic services with local state gain a credible high-throughput option; networked systems do not.
- Watch next: Reproduce results across hardware, durability settings, failures, backups, and genuinely comparable architectures.
