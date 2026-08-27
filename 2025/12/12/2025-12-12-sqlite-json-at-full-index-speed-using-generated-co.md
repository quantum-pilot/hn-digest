# SQLite JSON at full index speed using generated columns

- Score: 359 | [HN](https://news.ycombinator.com/item?id=46243904) | Link: https://www.dbpro.app/blog/sqlite-json-virtual-columns-indexing

### TL;DR

The post proposes storing each JSON document intact, exposing frequently queried paths as virtual generated columns with `json_extract`, then creating ordinary indexes on those columns. New query patterns can be supported later by adding another generated column and index, avoiding an up-front decomposition of every field. This combines flexible ingestion with familiar relational predicates and B-tree lookup. The article demonstrates syntax on tiny examples but supplies no query plans or benchmarks, and its broad “no backfilling” language should not be read as proof that index creation has no build cost.

### Comment pulse

- Readers compare the pattern with DuckDB analytics, PostgreSQL JSONB expression indexes, and normalized key-value rows.
- One commenter presents Lite³, a serialized B-tree document format; replies discuss updates, vacuuming, compression, and schema-aware alternatives.

### LLM perspective

- View: Generated columns are a pragmatic bridge, not a substitute for choosing an appropriate data model.
- Impact: Applications can defer selective JSON indexing while keeping ordinary SQLite query ergonomics.
- Watch next: Measure index-build time, write amplification, storage growth, planner choices, and schema-change behavior on real workloads.
