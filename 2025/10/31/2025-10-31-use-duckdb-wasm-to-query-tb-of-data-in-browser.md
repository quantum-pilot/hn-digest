# Use DuckDB-WASM to query TB of data in browser

- Score: 122 | [HN](https://news.ycombinator.com/item?id=45774571) | Link: https://lil.law.harvard.edu/blog/2025/10/24/rethinking-data-discovery-for-libraries-and-digital-humanities/

### TL;DR

Harvard’s Library Innovation Lab built Data.gov Archive Search as a static application over an 18 TB archive, with roughly 1 GB of catalog metadata stored as sorted, compressed Parquet. DuckDB-Wasm runs queries in each browser and uses HTTP range requests to retrieve relevant slices, avoiding a dedicated database server. The approach reduces operational burden for long-lived cultural collections, but requires careful data layout and incurs a large WASM startup cost. Commenters also warn that storage can be cheap while public bandwidth remains expensive.

### Comment pulse

- Client-side querying shifts infrastructure → static object storage plus range requests replaces a continuously operated application database.
- DuckDB need not be all-or-nothing → commenters describe embedded read modules alongside PostgreSQL and periodically refreshed files.
- Cost claims need traffic models → bandwidth and abuse can overwhelm cheap storage economics despite eliminating compute servers.

### LLM perspective

- View: This pattern fits large, mostly static catalogs where maintainability matters more than low-latency transactional behavior.
- Impact: Libraries can preserve interactive discovery despite shrinking budgets, while users supply query compute and memory.
- Watch next: Benchmark startup latency, transferred bytes, browser memory, accessibility, and monthly bandwidth under real traffic.
