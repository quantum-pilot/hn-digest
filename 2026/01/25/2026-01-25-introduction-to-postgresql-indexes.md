# Introduction to PostgreSQL Indexes

- Score: 279 | [HN](https://news.ycombinator.com/item?id=46751826) | Link: https://dlt.github.io/blog/posts/introduction-to-postgresql-indexes/

### TL;DR
A hands-on PostgreSQL primer explains how table data is stored in heap files and why indexes speed queries by mapping key values to tuple locations, illustrated with `EXPLAIN (ANALYZE, BUFFERS)` before/after examples. It stresses tradeoffs—extra disk space, slower writes, planner complexity, and memory pressure—and then tours main index types: B-tree (including multi-column, partial, covering, and expression indexes), plus hash, BRIN, GIN, GiST, and SP-GiST, with guidance on when each fits. HN adds modern nuances and external resources.

---

### Comment pulse
- Core references → PostgreSQL’s index docs and Use The Index, Luke remain canonical, deeper on planner behavior and real-world query patterns.  
- Multi-column wisdom evolving → earlier “leftmost prefix only” rule is softened by bitmap scans and Postgres 18’s index skip scan, though full scans remain costly.  
- Beyond classic indexes → many want built-in incremental view maintenance; today you reach for extensions (pg_ivm) or systems like TimescaleDB continuous aggregates and stream processors.

---

### LLM perspective
- View: Treat indexes as query-specific accelerators, not generic performance toggles; always pair creation with `EXPLAIN ANALYZE` baselines.  
- Impact: Application developers gain clearer mental models to avoid over-indexing and pick specialized structures (BRIN/GIN) earlier.  
- Watch next: Postgres 18+ skip scans, auto-index advisers, and maturing IVM extensions that blur the line between indexes and materialized views.
