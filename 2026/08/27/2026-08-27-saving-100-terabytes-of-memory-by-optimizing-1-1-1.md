# Saving 100 terabytes of memory by optimizing 1.1.1.1's DNS cache

- Score: 709 | [HN](https://news.ycombinator.com/item?id=49468083) | Link: https://blog.cloudflare.com/dns-cache-memory-optimization-1111/

### TL;DR

Cloudflare reports cutting its DNS cache entry from 953 to 420 bytes through five Rust layout changes: right-sized boxed slices, consolidated record lists, omitted duplicate owner names, boxed large enum variants, and wire-format record storage. Allocated memory fell 58%; production p99 instance RAM dropped from 9.3 to 5.3 GB, freeing roughly 100 TB fleetwide. Benchmarks also showed faster insertions and lookups. HN discussion emphasized memory layout, allocation count, cache locality, and safe abstractions over simplistic language comparisons.

### Comment pulse

- Small per-entry waste becomes fleet-scale capacity → immutable data and compact wire representations eliminated repeated overhead.
- Optimize after profiling, commenters advised → counterpoint: data-layout choices become expensive to change once hot paths mature.
- Rust enabled safe wrappers around dense layouts → custom representations still require careful indexing and invariants.

### LLM perspective

- View: The largest gain came from representing DNS data according to actual access patterns, not isolated micro-tuning.
- Impact: Higher cache capacity can improve hit rates while reducing server and memory requirements.
- Watch next: Production hit-rate changes and long-term allocator behavior will show whether the savings persist under evolving traffic.
