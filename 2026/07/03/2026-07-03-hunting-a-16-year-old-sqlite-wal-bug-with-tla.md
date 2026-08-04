# Hunting a 16-year-old SQLite WAL bug with TLA+

- Score: 162 | [HN](https://news.ycombinator.com/item?id=48730953) | Link: https://ubuntu.com/blog/hunting-a-16-year-old-sqlite-bug-with-tla-is-dqlite-affected

### TL;DR

Canonical’s dqlite team modeled a rare, 16-year-old SQLite WAL checkpoint race in TLA+ to test whether dqlite shared the corruption bug. A 20-state counterexample showed a checkpoint mixing stale header data with live shared state while another connection resets the WAL, leaving a false backfill position that later skips pages. A second model found dqlite safe because one write lock serializes appends and checkpoints; SQLite’s fix checks the WAL salt. HN mainly discussed TLA+ tooling and clarified that the team verified dqlite, not discovered SQLite’s bug.

### Comment pulse

- The title overstates the role → commenters noted SQLite found and fixed the bug independently; this work tested dqlite’s exposure.
- Formal modeling drew interest → readers valued above-code state-machine reasoning but wanted friendlier TLA+ syntax and developer tooling.

### LLM perspective

- **View:** A small concurrency model can answer safety questions that rare production failures cannot reproduce reliably.
- **Impact:** Locking differences become auditable evidence, not assumptions inherited from shared SQLite code.
- **Watch next:** Publish executable models beside regression tests and synchronize them with checkpointing changes.
