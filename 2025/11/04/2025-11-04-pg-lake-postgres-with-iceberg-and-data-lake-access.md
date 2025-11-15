# Pg_lake: Postgres with Iceberg and data lake access

- Score: 371 | [HN](https://news.ycombinator.com/item?id=45812606) | Link: https://github.com/Snowflake-Labs/pg_lake

- TL;DR
  - pg_lake is a Postgres extension suite that turns PostgreSQL into a transactional lakehouse: create Apache Iceberg tables, query Parquet/CSV/JSON on S3, and COPY to/from object storage—all from SQL. It embeds DuckDB for fast execution while Postgres supplies transactions and catalog, enabling high‑rate OLTP writes and atomic moves into Iceberg. HN praises it as an “open‑source Snowflake,” compares it with DuckLake’s simpler stack, and asks for a managed option; maintainers emphasize Iceberg interoperability and Postgres‑native orchestration.

- Comment pulse
  - Single system for apps and analytics → teams avoid ETL pipelines; OLTP changes become analytics-ready snapshots with ACID guarantees.
  - Use DuckLake instead → simpler stack with DuckDB and pg_duckdb; — counterpoint: Postgres adds ACID across OLTP/analytics, high-rate inserts, orchestration, Iceberg interoperability.
  - Ask for managed offering via Snowflake billing → Docker eases trials, but production teams prefer hosted operations and integration.

- LLM perspective
  - View: Embedding DuckDB under Postgres flips lakehouse architecture: compute engine inside database, not database inside engine.
  - Impact: SMBs can consolidate OLTP and analytics workflows on Postgres, deferring warehouse spend while keeping Iceberg portability.
  - Watch next: Benchmarks versus Snowflake/BigQuery and DuckDB; write-heavy stress, Iceberg compatibility matrix, security model, and a managed service announcement.
