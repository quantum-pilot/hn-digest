# Why DuckDB is my first choice for data processing

- Score: 193 | [HN](https://news.ycombinator.com/item?id=46645176) | Link: https://www.robinlinacre.com/recommend_duckdb/

## TL;DR
DuckDB is presented as a “default” engine for modern data work: an in-process OLAP database that’s trivial to install, extremely fast on single machines, and unusually pleasant to use. Highlights include a friendly SQL dialect (EXCLUDE, COLUMNS, QUALIFY, function chaining), great CSV/Parquet/JSON support over local, S3, and web sources, tight Python integration for stepwise pipelines, new ACID capabilities for medium-scale lakehouse-style workloads, and easy C++ UDFs/extensions. HN comments both celebrate real-world wins and question how far “single machine + SQL first” really scales.

---

## Comment pulse
- DuckDB fans: stellar CSV/Parquet/JSON handling, globbing, schema-flex unions, tiny binaries, and tools like Malloy/PRQL make experimentation and embedding analytics radically easier.  
- Production use: powers Bluesky analytics via Arrow/SQG and a biodiversity validator that may run offline in-browser, impressing users with speed and portability.  
- Skeptics: “single machine” and “SQL-first” claims overlook OOM risks and complex analysis needs — counterpoint: author says most real-world tabular workloads are modest in size.

---

## LLM perspective
- View: DuckDB is crystallizing a pattern where analytics engines are linked libraries, not separate services or clusters.  
- Impact: Encourages data teams to favor simple, testable pipelines and local-first experimentation before moving to distributed systems.  
- Watch next: Maturity of pg_duckdb, robustness of distributed DuckDB, and benchmarks versus Polars/DataFusion for >100GB workflows.
