# The Case Against PGVector

- Score: 345 | [HN](https://news.ycombinator.com/item?id=45798479) | Link: https://alex-jacobs.com/posts/the-case-against-pgvector/

- TL;DR
  - The author argues pgvector’s happy-path demos hide production tradeoffs: IVFFlat vs HNSW indexing choices, memory-hungry builds/rebuilds, and real-time ingestion bottlenecks. Postgres’s planner struggles with pre/post filtering and hybrid (text+vector) ranking, pushing teams into manual tuning; pgvectorscale helps but adds dependencies and isn’t on RDS. Net: for most teams, a managed vector DB simplifies filtering, hybrid search, and scaling. HN reactions split: pgvector is fine at modest scale; huge deployments prefer specialized systems; Postgres features help but demand expertise.

- Comment pulse
  - Pgvector works at modest scale → Discourse runs thousands of DBs; quantization cuts storage; iterative scans (v0.8) ease filtering, but not a silver bullet.
  - Huge scale prefers specialized systems → Halcyon uses Vespa for trillions; parent–child filters, sharding, and reindexing are simpler; AlloyDB ScaNN claims 1B+ with adaptive filtering.
  - Postgres knobs mitigate pain → maintenance_work_mem, REINDEX CONCURRENTLY help — counterpoint: massive HNSW still hogs memory, slows rebuilds, and demands deep Postgres tuning.

- LLM perspective
  - View: Use pgvector for millions-scale and tight SQL joins; beyond that, managed vector DBs reduce complexity.
  - Impact: Better latency under writes, fewer memory spikes, simpler hybrid search and filters; teams ship features instead of database plumbing.
  - Watch next: Real benchmarks of pgvectorscale and AlloyDB ScaNN; RDS support for pgvectorscale; planner-level filtered-search improvements in Postgres core.
