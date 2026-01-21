# Unconventional PostgreSQL Optimizations

- Score: 248 | [HN](https://news.ycombinator.com/item?id=46692116) | Link: https://hakibenita.com/postgresql-unconventional-optimizations

### TL;DR
The article explores three less-common PostgreSQL performance tricks. First, enabling `constraint_exclusion = on` lets PostgreSQL skip full table scans when predicates contradict CHECK constraints—especially valuable for ad‑hoc BI queries. Second, indexing a lower-cardinality expression (e.g., `date_trunc('day', sold_at)`), exposed via a virtual generated column, can shrink index size and speed queries without demanding “query-discipline.” Third, enforcing URL uniqueness via a hash-backed exclusion constraint yields a much smaller index but sacrifices foreign keys and some `INSERT ... ON CONFLICT` ergonomics; `MERGE` partly compensates.  

---

### Comment pulse
- Index size is part of broader write amplification → heavy analytical indexes belong on warehouses/replicas, not hot OLTP paths.  
- `MERGE` is more flexible than `INSERT ... ON CONFLICT` but interacts subtly with MVCC and failures; many prefer modeling around `ON CONFLICT` plus COPY for batches.  
- Hash uniqueness: collision worries are misplaced—Postgres verifies full values after hash match, so collisions don’t cause false “duplicate” errors.  

---

### LLM perspective
- View: These tricks suit mature systems needing incremental wins after conventional indexing, not as first-line tuning.  
- Impact: BI/reporting workloads, large text columns, and time-series analytics benefit most; OLTP-heavy systems must weigh extra write cost.  
- Watch next: Postgres 19 support for indexes on virtual generated columns could make the date-trunc pattern simpler and more widely applicable.
