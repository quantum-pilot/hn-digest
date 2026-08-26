# Unconventional PostgreSQL Optimizations

- Score: 248 | [HN](https://news.ycombinator.com/item?id=46692116) | Link: https://hakibenita.com/postgresql-unconventional-optimizations

### TL;DR

The article presents three PostgreSQL tactics: enable constraint_exclusion for ad-hoc analytics so impossible predicates can skip scans; index a lower-cardinality date expression instead of full timestamps, then expose it through a PostgreSQL 18 virtual generated column; and enforce uniqueness on long values with a hash-backed exclusion constraint. Examples shrink indexes from 214MB to 66MB and from 154MB to 32MB, with faster reads. HN praised the feature tour but emphasized workload context, write amplification, BRIN as a timestamp alternative, and concurrency caveats around replacing INSERT ... ON CONFLICT with MERGE.

### Comment pulse

- Workload design → BI indexes accelerate reads but amplify writes; large systems may isolate them on warehouses or delayed replicas.
- Date indexing → lower cardinality saves space, while BRIN may be even smaller when timestamps correlate with physical row order.
- Upsert tradeoff → MERGE handles exclusion-backed updates — counterpoint: commenters favored INSERT ... ON CONFLICT for clearer concurrency behavior.

### LLM perspective

- View: Each optimization exchanges generality for a narrower access pattern, so measured workload fit matters more than novelty.
- Impact: Specialized indexes can reduce storage and latency, but alter write cost, SQL ergonomics, referential options, and concurrency.
- Watch next: Benchmark planning overhead, index maintenance, BRIN, virtual-column indexing support, foreign keys, and concurrent MERGE behavior.
