# Pipelining in psql (PostgreSQL 18)

- Score: 153 | [HN](https://news.ycombinator.com/item?id=45555308) | Link: https://postgresql.verite.pro/blog/2025/10/01/psql-pipeline.html

- TL;DR
  - PostgreSQL 18 adds psql meta-commands (\startpipeline, \syncpipeline, \endpipeline) to pipeline queries over the extended protocol, letting clients send many statements without waiting for prior results. In tests inserting/upserting 100–100k rows, throughput improved 1.5× on localhost up to 71× over WAN; benefits rise with latency and batch size. Pipelines run in an implicit transaction with optional sync points. HN debates whether gains stem from fewer round trips versus packet coalescing, and notes uneven driver support, underused batching patterns, and promising ORM/JS-library results.

- Comment pulse
  - Gains mostly from eliminating per-statement round trips; pipelining overlaps send/execute/receive, not from larger packets — counterpoint: some speculate shared scans could reduce duplicated work.
  - Batching is underused: execute read-only batches, then a write batch, to bound round trips; JS drivers often lack batching, complicating adoption.
  - Ecosystem: maintainers consider support; postgres.js and pgline pipeline now; ORMs report 3–6× in-transaction gains, but failure semantics deter cross-request sharing.

- LLM perspective
  - View: psql pipeline commands make high-latency OLTP scripts faster without schema changes; ideal where COPY isn’t applicable.
  - Impact: Driver ecosystems will prioritize pipelining; ORMs may add pipeline-aware flush modes; DBAs revisit batch sizing versus sync points.
  - Watch next: Standardized benchmarks across RTTs; node-postgres support decisions; guidance on error propagation, retries, and mixing pipelines with prepared statements.
