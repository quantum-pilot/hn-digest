# SQLite JSON at full index speed using generated columns

- Score: 359 | [HN](https://news.ycombinator.com/item?id=46243904) | Link: https://www.dbpro.app/blog/sqlite-json-virtual-columns-indexing

### TL;DR
The post shows how to get full B‑tree index speed when querying JSON in SQLite by combining three features: store the original JSON blob, define **virtual generated columns** that use `json_extract` to expose specific fields, and then **index those generated columns**. You can add new generated columns and indexes later without rewriting existing rows, giving schemaless flexibility with relational performance. HN commenters extend this with alternative binary formats, compare SQLite to DuckDB and Postgres, and note that tools (and LLMs) now suggest this pattern.

---

### Comment pulse
- Encode JSON as a serialized B‑tree (Lite³) → lets you query fields at indexed speed without parsing, with in‑place updates and occasional “vacuum”.  
- DuckDB for analytics → SQLite is great, but DuckDB’s columnar engine and direct querying of JSON files excels on large analytical workloads—counterpoint: deployment is trickier than SQLite.
- Generated columns for JSON are widely used → Postgres, SingleStore, etc. already index JSON paths or use computed columns; some realize they should have normalized to key/value tables instead.

---

### LLM perspective
- View: This pattern is a practical “have your cake and eat it” compromise between schemaless JSON and strict schemas in embedded databases.
- Impact: Especially valuable for local-first apps, small services, and tools that evolve their data model frequently without costly migrations.
- Watch next: Benchmark VIRTUAL vs STORED columns, JSON vs binary formats like Lite³, and compare SQLite+JSON to DuckDB/Postgres JSONB for real workloads.
