# Making Postgres 300x faster for analytics: batching, operator fusion, and SIMD

- Score: 230 | [HN](https://news.ycombinator.com/item?id=49208535) | Link: https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/

- TL;DR  
  pgrust is a Rust reimplementation of Postgres that rethinks the query engine for in-memory, CPU-bound analytics. The post walks through replacing Postgres’s row-at-a-time Volcano executor with batched processing, operator fusion, and explicit SIMD, shrinking a SUM over 500M floats from ~20s in stock Postgres to 135ms in pgrust’s style. Comments focus on how to trust a new engine, formal verification and fuzzing efforts, adoption skepticism, and interest in adaptive planning and smarter IO/thread scheduling.

- Comment pulse  
  - Correctness is top priority → author uses formal proofs, fuzzing, external testers; already found ~100 pgrust and ~20 Postgres bugs — counterpoint: only ~15% covered.  
  - Users want advanced planning and scheduling → excitement about adaptive planning, plus questions on IO and thread schedulers to fix noisy-neighbor workloads.  
  - Adoption remains debated → many doubt organizations will trust a non-core fork; others argue real gains and new capabilities can override conservatism.

- LLM perspective  
  - View: Modern vectorized Rust engine plus Postgres compatibility echoes DuckDB/ClickHouse, but targets full SQL surface and OLTP+OLAP.  
  - Impact: Could become an analytical replica or accelerator for existing Postgres deployments, reducing need to ETL into separate columnar systems.  
  - Watch next: Stability under Jepsen-style tests, JIT operator fusion, WAL-based mirroring, and whether core Postgres adopts similar batching/scheduling ideas.
