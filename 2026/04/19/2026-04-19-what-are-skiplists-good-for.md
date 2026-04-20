# What are skiplists good for?

- Score: 255 | [HN](https://news.ycombinator.com/item?id=47806021) | Link: https://antithesis.com/blog/2026/skiptrees/

### TL;DR
Skiplists are a randomized alternative to balanced search trees with similar asymptotic behavior but much simpler concurrency and implementation tradeoffs. Antithesis used a generalization called a “skiptree” to represent huge execution trees inside BigQuery, which is terrible at pointer‑chasing but great at wide scans. By storing sampled tree levels as separate tables with ancestor “express lanes,” they turned ancestor lookups into fixed-join SQL scans, avoiding a second OLTP system. HN adds real‑world uses (Redis, SingleStore) and debates performance vs B/B+ trees.

---

### Comment pulse
- Real-world use → Redis sorted sets and SingleStore indexes use skiplists for ordered iteration and range queries; lock-free variants are simpler than balanced trees under contention.  
- Performance tradeoff → B/B+ trees win on cache locality and pointer count; skiplists shine for range intersections and postings lists—counterpoint: naive implementations can look unfairly slow.  
- Alternative designs → Some propose replaying fuzz runs from seeds; Antithesis notes multi-minute, multi-container workloads and non-deterministic inputs make this far too expensive for queries.

---

### LLM perspective
- View: Skiplists/skiptrees are especially valuable when your storage engine can only do wide scans, not efficient pointer traversals.  
- Impact: Analytics and observability systems can encode tree structure into scan-friendly layouts instead of bolting on a second transactional store.  
- Watch next: Better benchmarks comparing modern cache-aware skiplists vs B/B+ trees and native tree-query support in cloud warehouses.
