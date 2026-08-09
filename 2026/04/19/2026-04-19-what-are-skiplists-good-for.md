# What are skiplists good for?

- Score: 255 | [HN](https://news.ycombinator.com/item?id=47806021) | Link: https://antithesis.com/blog/2026/skiptrees/

### TL;DR

Antithesis adapted skiplists into a “skiptree” to query branching fuzzer histories in BigQuery, where recursive parent lookups caused repeated full scans. Each level retained roughly half the nodes and stored skipped ancestors, letting one generated, non-recursive SQL query reconstruct history through about 40 joins. Because levels shrank geometrically, queries scanned only about twice the base data under BigQuery’s pricing. This powered test-property evaluation for six years. Commenters highlighted broader wins in concurrent indexes and ordered sets, while noting weaker cache locality than B-trees.

### Comment pulse

- Redis pairs a skiplist with a hash table for ordered ranges, ranking, iteration, and constant-time direct lookup.
- Concurrent users prefer lock-free skiplists because randomized levels avoid tree rotations and simplify compare-and-swap updates.
- Naive skiplists are adequate and flexible — counterpoint: page-oriented B-trees usually exploit memory and I/O locality better.

### LLM perspective

- Exotic structures become practical when they align with a storage engine’s cost model and planner limits.
- Generated SQL can encapsulate ugly physical plans behind a stable logical operation.
- Benchmark latency, bytes scanned, write amplification, and cache behavior against replay or specialized storage.
