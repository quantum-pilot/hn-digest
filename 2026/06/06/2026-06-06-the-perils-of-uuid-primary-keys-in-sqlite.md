# The perils of UUID primary keys in SQLite

- Score: 150 | [HN](https://news.ycombinator.com/item?id=48419571) | Link: https://andersmurphy.com/2026/06/05/the-perils-of-uuid-primary-keys-in-sqlite.html

### TL;DR

In SQLite, ordinary tables cluster rows by a sequential 64-bit `rowid`; `WITHOUT ROWID` instead clusters on the declared primary key. Benchmarking million-row insert batches, an integer key stayed near 0.7 seconds, random 16-byte UUIDv4 keys degraded to 12.6 seconds, and time-ordered UUIDv7 held near 1.26 seconds. Profiling attributed UUIDv4’s 14–16× slowdown to random B-tree insertion, rebalancing, and I/O; retaining `rowid` plus a UUIDv4 index still reached 7.1 seconds. HN favored integers locally and UUIDv7 for cross-device creation, while noting UUIDv4 hides sequence and timestamps.

### Comment pulse

- Choose IDs from coordination needs → integers suit one local database; UUIDv7 simplifies offline creation, device sync, merges, splits, and deduplication.
- Every identifier leaks differently → integers reveal counts and neighbors, UUIDv7 reveals time — counterpoint: UUIDv4 sacrifices locality to hide both.
- SQLite’s alias is exact → `INTEGER PRIMARY KEY`, not `INT PRIMARY KEY`, becomes `rowid` and avoids a separate index.

### LLM perspective

- **View:** The core variable is insertion locality, not UUID branding; key order, width, and index role interact.
- **Impact:** Sync-heavy apps can retain client-generated IDs without UUIDv4’s worst write costs by choosing ordered identifiers.
- **Watch next:** Benchmark reads, deletes, joins, database size, row widths, and multi-device merge workloads alongside insert speed.
