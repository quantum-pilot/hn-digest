# SQLite Is a Library of Congress Recommended Storage Format

- Score: 596 | [HN](https://news.ycombinator.com/item?id=48042434) | Link: https://sqlite.org/locrsf.html

### TL;DR

A 2018 SQLite note says the Library of Congress listed SQLite alongside XML, JSON, and CSV as recommended dataset-preservation formats. The designation favors documented, widely adopted, transparent, self-describing formats with few external dependencies and minimal patent or access barriers; it is about long-term accessibility, not database performance. HN commenters praised SQLite’s reliability and practical single-writer model, while noting operational risks: an innocuous-looking file can become an unmanaged store of sensitive data, and single-node storage still needs backups or replication. Others highlighted smaller specialized formats for read-only archives.

### Comment pulse

- Preservation endorsement evaluates survivability and inspectability → it does not certify application architecture, concurrency, or infrastructure resilience.
- SQLite’s file form simplifies deployment → the same portability can enable shadow databases, uncontrolled copies, and overlooked PII.
- Single-writer limits are often acceptable → optimized WAL handles many applications — counterpoint: losing the host still loses unreplicated data.

### LLM perspective

- **View:** Format durability and system durability are separate; teams need both an accessible file and a recovery plan.
- **Impact:** Small applications can avoid database servers while treating SQLite files as governed production assets.
- **Watch next:** Current LoC recommendations, migration tooling, backup tests, integrity checks, and archival documentation.
