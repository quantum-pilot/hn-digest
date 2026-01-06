# Databases in 2025: A Year in Review

- Score: 591 | [HN](https://news.ycombinator.com/item?id=46496103) | Link: https://www.cs.cmu.edu/~pavlo/blog/2026/01/2025-databases-retrospective.html

## TL;DR

2025 cemented PostgreSQL as the industry’s center of gravity: huge acquisitions (Neon → Databricks, CrunchyData → Snowflake), a serious new Azure offering, and emerging sharding layers (Multigres, Neki, PgDog) all orbit Postgres. Meanwhile, nearly every major database shipped an MCP server to plug into LLMs, raising sharp security and governance concerns. MongoDB sued FerretDB over Mongo-compatible APIs as Microsoft’s DocumentDB entered the same space. At the storage layer, Parquet faces fresh competition from new columnar formats aimed at AI-era workloads.

## Comment pulse

- Immutable/bi-temporal databases are overlooked → XTDB, Datomic, and homegrown Postgres setups show strong value for auditability, time-travel, and safe undo — counterpoint: author asks what concrete 2025 news to cover.  

- SQLite (and DuckDB) trend grows → many workloads move to single-file, embedded engines with JSON support or columnar analytics, despite older dogma against SQLite in production.  

- MCP database access worries people → protocol maximizes LLM context, clashing with least-privilege; practitioners stress strict DB roles, gateways, and read-only configs to avoid “LLM-driven SQL injection.”  

## LLM perspective

- View: Postgres is becoming the “Linux of databases,” with value shifting to cloud platforms, sharding middleware, and compatibility layers.  

- Impact: Niche engines must differentiate on immutability, latency, hardware specialization, or developer ergonomics rather than generic CRUD and SQL.  

- Watch next: Real-world MCP incident reports, MongoDB–FerretDB legal outcomes, and GPU-native file format adoption will shape 2030s data architectures.
