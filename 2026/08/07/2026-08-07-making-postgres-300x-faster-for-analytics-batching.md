# Making Postgres 300x faster for analytics: batching, operator fusion, and SIMD

- Score: 230 | [HN](https://news.ycombinator.com/item?id=49208535) | Link: https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/

### TL;DR

pgrust 0.2 reports 30% better OLTP performance than PostgreSQL and a 300× ClickBench advantage, with its redesigned query engine contributing roughly 10×. A miniature Volcano executor shows why: processing one row per virtual `next()` call took 1.3 seconds; 1,024-row stack batches cut that to 480ms, operator fusion to 358ms, and ARM SIMD to 135ms. The benchmark used warm data, disabled PostgreSQL parallelism, and isolates only part of total database overhead. HN admired the engineering but treated correctness, production behavior, and institutional trust as harder adoption barriers than speed.

### Comment pulse

- The author has formally or differentially tested about 15% of the surface, finding roughly 100 pgrust bugs and 20 PostgreSQL bugs.
- Performance work must survive real cache, I/O, and noisy-neighbor conditions; synthetic improvements do not always move production profiles.
- Some wanted optimizations upstream — counterpoint: adaptive planning, work stealing, and architectural changes may exceed PostgreSQL’s incremental design path.

### LLM perspective

- View: Row-at-a-time abstraction costs become dominant when storage is fast; batching restores locality before specialization removes abstraction entirely.
- Impact: Analytics users gain a PostgreSQL-compatible candidate, but operators inherit a new implementation’s correctness and continuity risk.
- Watch next: Publish full ClickBench configuration, query-level results, WAL mirroring readiness, scheduler behavior, verification coverage, and JIT details.
