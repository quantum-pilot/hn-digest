# My favourite small hash table

- Score: 116 | [HN](https://news.ycombinator.com/item?id=46205461) | Link: https://www.corsix.org/content/my-favourite-small-hash-table

### TL;DR
The post walks through a compact hash table design: Robin Hood hashing with linear probing, power-of-two table size, and 64-bit slots packing key+value. Empty slots are encoded as zero, avoiding separate “empty/tombstone” markers and keeping everything in one dense array for cache efficiency. It details lookup, insert (with displacement), rehashing, and tombstone-free deletion by backward shifting. Extensions cover non-random keys via invertible 32‑bit hashes, and larger or variable-sized keys/values via separate storage arrays indexed from the hash table.

---

### Comment pulse
- Direct array indexing for 32-bit keys → would be simpler and smaller at max scale; hash table wins when key-space is sparse or memory-constrained.  
- Simple, contiguous layouts → great cache behavior in many workloads; real problems often use variable-length keys, needing extra indirection and domain-specific hashing — counterpoint: author explicitly sketches that extension.  
- Storing key+value in `uint64_t` → enables zero-check for emptiness and tight layout; some prefer split key/value arrays for even better probe locality.

---

### LLM perspective
- View: A well-explained reference implementation of Robin Hood hashing, highlighting real ISA-level tradeoffs and deletion without tombstones.  
- Impact: Useful for performance-sensitive systems code, small in-memory indexes, and as a teaching example of open addressing invariants.  
- Watch next: Empirical benchmarks vs SwissTable/Abseil, behavior under adversarial keys, and adaptations for concurrency or NUMA-aware layouts.
