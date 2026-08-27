# Pipelining in psql (PostgreSQL 18)

- Score: 153 | [HN](https://news.ycombinator.com/item?id=45555308) | Link: https://postgresql.verite.pro/blog/2025/10/01/psql-pipeline.html

### TL;DR

PostgreSQL 18 adds `psql` commands for client-side query pipelining: `\startpipeline`, `\syncpipeline`, `\getresults`, and `\endpipeline`. Independent queries can be sent without awaiting each prior result, overlapping client, network, and server work while reducing round trips. A benchmark of prepared upserts reports speedups from 1.5× locally to 71× over the slowest tested network, increasing with batch size and latency. Pipeline blocks use transactional semantics, so dependent queries require synchronization and failures roll back work since the relevant sync point.

### Comment pulse

- Readers argued the main gain comes from eliminating round-trip waits, not merely packing queries into fewer network packets.
- Driver maintainers discussed uneven pipeline support and strong gains for transaction-scoped batches of writes.

### LLM perspective

- View: Pipelining is most valuable when many independent small statements are latency-bound rather than compute-bound.
- Impact: It preserves row-oriented application logic while approaching batching efficiency, without constructing huge multi-value statements.
- Watch next: Driver adoption, failure semantics, memory behavior, and production benchmarks with realistic result sizes.
