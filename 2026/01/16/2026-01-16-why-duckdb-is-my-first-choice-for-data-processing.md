# Why DuckDB is my first choice for data processing

- Score: 193 | [HN](https://news.ycombinator.com/item?id=46645176) | Link: https://www.robinlinacre.com/recommend_duckdb/

### TL;DR

The author now defaults to DuckDB for tabular data processing, arguing that powerful single machines eliminate cluster complexity for most workloads. DuckDB is an in-process analytical SQL engine with a tiny dependency-free install, fast startup and execution, direct CSV/JSON/Parquet and remote-file querying, ergonomic SQL, lazy Python relations, ACID bulk operations, and distributable C++ extensions. Those traits simplify exploration, CI, testing, and medium-scale pipelines. HN users praised schema inference, globbing, union-by-name, portability, and real scientific and analytics deployments, while asking when Polars or ClickHouse offers a better syntax or scale tradeoff.

### Comment pulse

- Direct file querying changes exploration → users can ingest messy globbed datasets, validate assumptions quickly, and discover dead ends earlier.
- Portability enables unusual deployments → a biodiversity tool may run fully offline in an iPad browser while preserving validation workflows.
- DuckDB is not automatically superior → Polars may offer friendlier transformations, while ClickHouse targets distributed ingestion and larger systems.

### LLM perspective

- View: DuckDB’s advantage is the compound effect of speed, zero-service operation, rich I/O, and familiar SQL.
- Impact: Teams can replace heavyweight local clusters and bespoke parsers with reproducible single-machine pipelines that are easier to test.
- Watch next: Benchmark real workloads against Polars and ClickHouse; assess HDF5 gaps, extension safety, concurrency, and production-scale limits.
