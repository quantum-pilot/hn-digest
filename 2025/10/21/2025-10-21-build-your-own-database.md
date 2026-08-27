# Build your own database

- Score: 344 | [HN](https://news.ycombinator.com/item?id=45657827) | Link: https://www.nan.fyi/database

### TL;DR

This interactive tutorial derives a key-value database from basic constraints. It begins with append-only records, adds offsets for faster lookup, then sorts records so a sparse in-memory index can trade memory for search time. New writes enter a sorted memtable and append-only recovery log before flushing into immutable sorted files; updates and deletes become newer records, with compaction removing obsolete entries. The result is an LSM tree. Commenters praised the visualization while flagging attribution, misleading scale claims, and animations that appear to write unsorted output.

### Comment pulse

- Learning by reconstruction works → the progression makes storage-engine tradeoffs approachable even when production users should choose established databases.
- Attribution was requested → one reader called it an interactive rendering of chapter three of Designing Data-Intensive Applications.
- Scale needs qualification → node-level LSM storage alone does not explain DynamoDB's distributed request throughput.

### LLM perspective

- View: The tutorial succeeds by making each data structure answer a concrete limitation introduced immediately before it.
- Impact: Readers gain a mental model for write-ahead logs, memtables, sparse indexes, immutable segments, tombstones, and compaction.
- Watch next: Correct the sorting animations, add source acknowledgments, and distinguish local storage performance from distributed scaling.
