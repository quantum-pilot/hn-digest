# AliSQL: Alibaba's open-source MySQL with vector and DuckDB engines

- Score: 130 | [HN](https://news.ycombinator.com/item?id=46875228) | Link: https://github.com/alibaba/AliSQL

- TL;DR
    - AliSQL is Alibaba’s hardened MySQL 8.0.44 fork, now open-sourced, that adds two headline capabilities: a native DuckDB storage engine and built‑in vector indexing. DuckDB runs as a MySQL engine, giving columnar analytics through normal MySQL connections, while the vector store supports up to 16k‑dimensional HNSW ANN search via SQL. Roadmap items focus on faster DDL, crash recovery, and replication. HN discussion centers on whether this is real HTAP, and how it compares with pg_duckdb, MariaDB, ClickHouse, and TiDB.

- Comment pulse
    - AliSQL+DuckDB pitched as HTAP → transactional sync keeps OLTP and analytics close, avoiding ETL pipelines. — counterpoint: others say guarantees match typical OLAP storage engines.
    - HN compares AliSQL to pg_duckdb, MariaDB ColumnStore, TiDB, ClickHouse, Tiger Data → many options already blend OLTP interfaces with columnar or vector backends.
    - Some wonder why extend MySQL instead of Postgres FDWs → likely because Alibaba already runs huge MySQL-based stacks and wanted minimal app-layer changes.

- LLM perspective
    - View: A MySQL-native DuckDB and vector engine reduces friction for LLM/RAG features in existing MySQL-centric applications.
    - Impact: MySQL shops gain ClickHouse-like analytics and pgvector-style search without new stacks; could pressure Oracle MySQL and MariaDB roadmaps.
    - Watch next: independent performance/consistency benchmarks, clarity on continuous ingestion semantics, and whether other vendors adopt embedded DuckDB-style column engines.
