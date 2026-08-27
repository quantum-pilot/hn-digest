# My favourite small hash table

- Score: 116 | [HN](https://news.ycombinator.com/item?id=46205461) | Link: https://www.corsix.org/content/my-favourite-small-hash-table

### TL;DR

The article implements a compact Robin Hood hash table for random 32-bit keys and 32-bit values, packing each pair into one 64-bit slot and reserving zero for emptiness. Power-of-two sizing enables masked linear probing; Robin Hood displacement scores allow unsuccessful lookups to stop early. Insertions swap with less-displaced entries, deletion shifts subsequent entries backward without tombstones, and growth occurs near 75% load. The author also sketches invertible hashing and indirection for larger keys, while explicitly excluding concurrent lock-free use.

### Comment pulse

- Compact arrays reduce pointer chasing and favor caches → contention and redundant probes can still dominate real workloads.
- The example’s word-sized random keys feel contrived → extensions cover larger values, but variable-length keys require additional storage and equality checks.
- Packed 64-bit slots simplify empty tests and loads → separate key/value arrays may make probing cache lines denser.

### LLM perspective

- View: The design’s appeal comes from aligned constraints; changing key shape or concurrency requirements changes the winner.
- Impact: Systems programmers get a small, explainable baseline whose invariants support lookup, insertion, and deletion cleanly.
- Watch next: Benchmark realistic distributions, deletion-heavy workloads, cache pressure, architecture differences, and alternative layouts.
