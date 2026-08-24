# My favourite small hash table

- Score: 116 | [HN](https://news.ycombinator.com/item?id=46205461) | Link: https://www.corsix.org/content/my-favourite-small-hash-table

### TL;DR

The article builds a compact C hash table from Robin Hood open addressing, linear probing and a power-of-two slot array. Under narrow 32-bit key/value assumptions, each pair fits one 64-bit word, zero marks emptiness, lookups terminate from displacement ordering, insertions swap less-displaced occupants, and deletion shifts entries backward without tombstones. Growth begins at 75% load. HN admired cache-friendly simplicity but questioned how representative machine-word keys are, suggesting dense arrays, separate key/value storage or richer examples for real workloads.

### Comment pulse

- Cache locality is the design’s strength → compact probing avoids pointer chasing, though contention can make extra lookups unexpectedly costly.
- The assumptions invite alternatives → a 32-bit key domain permits direct indexing when memory floors are acceptable.
- Generalization adds indirection → strings and variable-size objects require hashing external data and checking equality after collisions.

### LLM perspective

- View: Specialized constraints buy unusually clear invariants and code.
- Impact: Systems programmers gain a strong small-table template, not a universal container.
- Watch next: Workload benchmarks against SIMD tables and split-array layouts.
