# Marmot – A distributed SQLite server with MySQL wire compatible interface

- Score: 172 | [HN](https://news.ycombinator.com/item?id=46460676) | Link: https://github.com/maxpert/marmot

### TL;DR
Marmot v2 turns SQLite into a leaderless, distributed database that speaks the MySQL wire protocol. Any node can accept writes; data replicates via CDC and a gossip-based 2PC system with tunable consistency (ONE/QUORUM/ALL). It fully replicates DDL, supports WordPress unmodified, and can expose the SQLite file for ultra-fast local reads, making it attractive for edge, Lambda sidecars, and read-heavy apps. Limits: full replication only (no sharding yet), eventual consistency, and better suited to <~100GB datasets.

*Content unavailable; summarizing from provided README and comments.*

### Comment pulse
- Real user: Marmot reliably synced a large “wayback machine” SQLite workload across HA nodes, requiring no frontend changes once configured.
- Author: chose MySQL protocol over REST/page-capture to get ACID+DDL replication and instant compatibility with WordPress and existing MySQL tooling.
- Positioning vs Postgres/MySQL: SQLite + Marmot gives very lightweight, edge-friendly reads and simple deployment—counterpoint: many teams already get enough from Postgres or MySQL active-active.

### LLM perspective
- View: Marmot targets the “distributed SQLite + MySQL ecosystem” niche rather than competing head‑on with full SQL engines.
- Impact: Edge/WordPress hosting, serverless platforms, and small SaaS stacks could simplify multi-region databases without heavy infra.
- Watch next: sharding/partial replication, stronger guarantees around non-deterministic functions, and real-world benchmarks vs MySQL group replication/Cockroach.
