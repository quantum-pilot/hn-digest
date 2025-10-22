# Build your own database

- Score: 344 | [HN](https://news.ycombinator.com/item?id=45657827) | Link: https://www.nan.fyi/database

TL;DR
An interactive walkthrough builds a key‑value store from a single append‑only file to segments with compaction, in‑memory indexing, sorted on‑disk tables, and a memtable+SST with a write‑ahead log—ending in an LSM tree and contrasting with B‑trees. HN praises the design and clarity, but notes strong overlap with DDIA ch.3 and asks for attribution. Commenters also flag that DynamoDB’s 80M rps reflects distributed scaling beyond the LSM engine, point out unsorted flush examples, and endorse the “build one to learn” approach.

Comment pulse
- Large overlap with DDIA ch.3 → interactive restatement; attribution requested.
- Beautiful, approachable; good exercise to learn tradeoffs → teaches why SQL/BTrees exist — counterpoint: do not ship DIY DBs.
- Accuracy/bugs: LSM is not sole reason for DynamoDB 80M rps; flush examples unsorted; lorem ipsum reduces clarity.

LLM perspective
- View: Solid LSM primer; interactivity lowers barrier, but omit durability nuances (fsync, checksums), compaction strategies, and concurrency.
- Impact: Students and junior engineers grok storage tradeoffs; teams can prototype WAL+SST designs before adopting LevelDB/RocksDB.
- Watch next: Benchmark vs RocksDB; add crash-recovery tests, Bloom filters, leveled/tiered compaction; measure write amplification and tail latency.
