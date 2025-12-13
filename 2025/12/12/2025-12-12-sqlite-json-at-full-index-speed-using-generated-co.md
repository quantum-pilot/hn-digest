# SQLite JSON at full index speed using generated columns

- Score: 297 | [HN](https://news.ycombinator.com/item?id=46243904) | Link: https://www.dbpro.app/blog/sqlite-json-virtual-columns-indexing

- TL;DR  
The post shows how to keep entire JSON documents in a single SQLite column, then add virtual generated columns using `json_extract()` and index them. Those generated columns act like normal indexed fields, giving full B-tree speed without rewriting data or pre-planning every index. You can later add more generated columns and indexes as query needs evolve, effectively combining schemaless ingestion with relational-style performance and ergonomics. HN expands with related formats, alternative engines, and broader patterns in JSON handling.

- Comment pulse  
  - Alternative: Lite³ stores JSON as a serialized B-tree, enabling indexed-style queries without parsing—counterpoint: still experimental and ecosystem is small.  
  - DuckDB excels at large analytic workloads over JSON files with SQL-on-files, but lacks SQLite’s broad embeddability and deployment simplicity.  
  - Generated columns over JSON are widely used (Postgres, SingleStore); many argue some JSON use-cases should eventually be normalized key–value tables.

- LLM perspective  
  - View: This pattern is a pragmatic bridge between schemaless ingestion and later, targeted relational optimization.  
  - Impact: Teams gain flexibility to experiment with JSON schemas without immediate migration or indexing decisions.  
  - Watch next: Comparative benchmarks of virtual-column indexes vs native JSON indexing in other databases and hybrid SQLite/DuckDB pipelines.
