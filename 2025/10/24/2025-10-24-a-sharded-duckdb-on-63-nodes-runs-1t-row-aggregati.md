# A sharded DuckDB on 63 nodes runs 1T row aggregation challenge in 5 sec

- Score: 197 | [HN](https://news.ycombinator.com/item?id=45694122) | Link: https://gizmodata.com/blog/gizmoedge-one-trillion-row-challenge

### TL;DR

GizmoData reports that GizmoEdge coordinated 1,000 DuckDB workers across roughly 63 Azure nodes to count one trillion rows in under half a second and compute grouped aggregates in under five seconds. The planner split queries into shard-level work and a final aggregation, exchanging Arrow IPC over WebSockets. The headline excludes more than two minutes of startup and data preparation, while the hot cluster used about 4,000 virtual CPUs and 30 TB of RAM. Commenters found the engineering impressive but questioned cost and framing.

### Comment pulse

- Benchmark skepticism → warm caches, preparation time, and a large always-on cluster complicate the five-second headline.
- Architecture interest → commenters debated WebSockets and DuckDB’s role as an embedded worker rather than a distributed database.

### LLM perspective

- View: The result demonstrates orchestration scale more clearly than economical trillion-row analytics.
- Impact: Interactive performance is plausible for organizations able to keep thousands of workers hot.
- Watch next: Reproduce cold-start latency, cache state, hourly cost, and failure behavior under production workloads.
