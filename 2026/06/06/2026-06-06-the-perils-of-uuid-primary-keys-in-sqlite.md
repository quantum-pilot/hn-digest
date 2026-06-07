# The perils of UUID primary keys in SQLite

- Score: 150 | [HN](https://news.ycombinator.com/item?id=48419571) | Link: https://andersmurphy.com/2026/06/05/the-perils-of-uuid-primary-keys-in-sqlite.html

### TL;DR
Author benchmarks SQLite with different primary-key strategies. With `WITHOUT ROWID`, using random UUID4 as the primary key turns the clustered index into a random write pattern, causing heavy B-tree rebalancing and making inserts roughly 14–16× slower than the default integer `rowid`. Time-ordered UUID7 restores locality and gets close to rowid performance, still slightly slower from 16‑byte keys. UUID4 with `rowid` is better than UUID4 `WITHOUT ROWID` but worse than UUID7. Discussion focuses on when UUIDs are worth their costs versus bigint keys.

---

### Comment pulse
- UUIDs overused; prefer bigint except distributed/opaque IDs; beware JS rounding; UUIDs help client‑generated IDs, optimistic UIs, but enlarge indexes and hurt joins.  
- Post seen as argument for UUIDv7: near-rowid performance yet globally mergeable IDs for multi-device sync; random PKs on clustered indexes stay pathological.  
- UUIDv7 leaks time; integers leak sequence; UUIDv4 hides both but slows inserts; some argue real culprit is using WITHOUT ROWID with random keys.

---

### LLM perspective
- View: Pick primary keys by workload: write-heavy SQLite tables want monotonic, compact keys; hideable IDs can live in secondary columns.  
- Impact: Mobile apps, embedded tools, and sync engines using SQLite should revisit ORM defaults that blindly choose UUIDv4 as clustered primary key.  
- Watch next: Need mixed read/write benchmarks, varying row sizes and page sizes, plus guidance on combining rowid with UUIDv7 for external references.
