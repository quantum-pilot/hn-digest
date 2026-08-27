# Pg_lake: Postgres with Iceberg and data lake access

- Score: 371 | [HN](https://news.ycombinator.com/item?id=45812606) | Link: https://github.com/Snowflake-Labs/pg_lake

### TL;DR

Snowflake Labs' Apache-licensed pg_lake project combines PostgreSQL extensions with a DuckDB-backed Postgres-wire server. It can create, modify, and query Iceberg tables; read or move data in S3 formats including Parquet, CSV, and JSON; and mix heap tables, Iceberg, and external files in SQL workflows. The project pitches a shared transactional and catalog boundary for operational and analytical data. Commenters welcomed the idea but questioned its use case, managed-service path, and differentiation from DuckLake; maintainers emphasized Postgres-native transactions and orchestration.

### Comment pulse

- Several readers wanted a managed offering and clearer production guidance.
- Maintainers argued the differentiator is transactional coordination between Postgres heap tables and Iceberg, not simply embedded DuckDB.

### LLM perspective

- View: The compelling unit is one transactional Postgres workflow spanning operational rows and lakehouse tables.
- Impact: Existing Postgres teams could add analytical storage without immediately adopting a separate control plane.
- Watch next: Independent benchmarks, recovery behavior, concurrency limits, catalog interoperability, and a credible managed deployment story.
