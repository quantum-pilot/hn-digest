# Marmot – A distributed SQLite server with MySQL wire compatible interface

- Score: 172 | [HN](https://news.ycombinator.com/item?id=46460676) | Link: https://github.com/maxpert/marmot

### TL;DR

Marmot v2 turns SQLite into a leaderless, fully replicated database that accepts writes on any node through a MySQL-compatible interface. It combines gossip membership, two-phase commit with ONE/QUORUM/ALL settings, last-write-wins conflict resolution, CDC-based row replication, distributed DDL, and local vector indexes. WordPress runs unchanged against local nodes, while direct SQLite reads remain possible. The project targets read-heavy edge workloads, not strong serializability, very large datasets, or single-region throughput; HN users praised its practicality but questioned scaling writes.

### Comment pulse

- Real deployments value compatibility → one user replicated an archival SQLite database across HA servers without changing the frontend.
- MySQL wire support broadens adoption → the author reports WordPress compatibility and local reads while routing writes through Marmot.
- Full replication limits write scaling → selective database replicas and transparent write proxying are roadmap items, with sharding still unresolved.

### LLM perspective

- View: Marmot’s strongest proposition is operational portability, not replacing strongly consistent distributed databases.
- Impact: Edge and WordPress operators gain local reads and familiar clients while accepting eventual-consistency tradeoffs.
- Watch next: Test partitions, concurrent conflicts, DDL recovery, cross-region latency, selective replication, and sustained production workloads.
