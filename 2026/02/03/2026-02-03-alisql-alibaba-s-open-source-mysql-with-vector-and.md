# AliSQL: Alibaba's open-source MySQL with vector and DuckDB engines

- Score: 130 | [HN](https://news.ycombinator.com/item?id=46875228) | Link: https://github.com/alibaba/AliSQL

### TL;DR

AliSQL 8.0.44 is Alibaba’s GPL-2.0 MySQL 8.0.44 branch, used internally and open-sourced in December 2025. It now embeds DuckDB as a native storage engine for lightweight analytics and adds SQL-accessible vector storage up to 16,383 dimensions with HNSW approximate-nearest-neighbor indexing. Planned work targets DDL, crash recovery, and replication. Commenters welcomed combining transactions, analytics, and vectors behind one interface, but disputed whether this constitutes true HTAP or merely coupled engines, and requested comparisons with pg_duckdb, MariaDB ColumnStore, TiDB, ClickHouse, and Tiger Data.

### Comment pulse

- Integrated analytics can simplify operations → keeping MySQL interfaces may reduce separate pipelines and connections for mixed transactional and analytical workloads.
- HTAP label is contested → transactional synchronization sounds promising — counterpoint: critics saw two engines without clearly stronger consistency guarantees.
- Ecosystem fit will decide adoption → users want benchmarks and operational comparisons against Postgres extensions, MariaDB, TiDB, ClickHouse, and existing CDC pipelines.

### LLM perspective

- View: AliSQL’s practical appeal is MySQL-compatible consolidation; the README establishes features, not comparative performance or end-to-end consistency.
- Impact: MySQL shops gain an incremental analytics and vector path while assuming fork maintenance, engine semantics, and migration risk.
- Watch next: DuckDB transaction guarantees, replication behavior, vector recall and latency, production benchmarks, roadmap delivery, packaging, documentation, and upstream divergence.
