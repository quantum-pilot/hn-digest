# SQLite in Production: Optimizing WAL Mode, Concurrency, and VFS Layers

- Score: 223 | [HN](https://news.ycombinator.com/item?id=49094346) | Link: https://micrologics.org/blog/sqlite-in-production-optimizing-wal-mode-concurrency-and-vfs-layers-for-low-latency-app-servers

### TL;DR

The article recommends production SQLite for read-heavy, single-server workloads: enable WAL, schedule checkpoints, use a busy timeout and immediate write transactions, enlarge caches, map files into memory, and replicate local storage. It argues this removes database network latency while retaining simple operations, but keeps PostgreSQL for geographically distributed writes or multi-terabyte data. Commenters challenge both authorship and advice, warning that NORMAL synchronization can lose committed rows, multiple writers may need application-level serialization, and schema migrations, type enforcement, attached databases, administration, and ephemeral disks require deliberate handling.

### Comment pulse

- Durability wording matters → NORMAL avoids corruption but can lose recent committed transactions; one user stopped row loss by switching to FULL.
- Writer contention needs architecture → busy timeout delays failure, while an application lock can serialize MQTT ingestion and pruning transactions.
- SQLite’s production tradeoffs extend beyond speed → critics cite weak schema alteration, loose typing, migration friction, and remote inspection challenges.

### LLM perspective

- View: SQLite succeeds when the application embraces single-writer ownership rather than pretending WAL creates a client-server concurrency model.
- Impact: Teams trade network latency and operational simplicity for more responsibility around durability, migrations, observability, and failover.
- Watch next: Benchmark workload-specific lock wait, checkpoint latency, crash loss, recovery, and replica lag before choosing pragmas.
