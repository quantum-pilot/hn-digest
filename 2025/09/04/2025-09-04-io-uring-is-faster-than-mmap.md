# io_uring is faster than mmap

- Score: 284 | [HN](https://news.ycombinator.com/item?id=45132710) | Link: https://www.bitflux.ai/blog/memory-is-slow-part2/

### TL;DR

On a 50GB integer-counting benchmark, the author measured an unrolled, vectorized `mmap` scan of cached data at 5.51GB/s and a six-worker `io_uring` plus `O_DIRECT` pipeline from two striped SSDs at 5.81GB/s. A preloaded buffer reached 7.90GB/s across the full NUMA system and 13.04GB/s on a smaller local dataset, showing memory itself was not slower. The claimed advantage comes from overlapping direct I/O while `mmap` incurs serial page-fault and mapping overhead. Commenters dispute the fairness, suggesting prefaulting, `MAP_POPULATE`, huge pages, or equivalent parallel preparation.

### Comment pulse

- Critics say the comparison gives `io_uring` background workers while leaving `mmap` to fault pages synchronously.
- Another tradeoff is cache ownership: direct I/O buffers lose automatic reclamation and sharing provided by the page cache.

### LLM perspective

- View: The experiment demonstrates a pipeline advantage over one `mmap` access pattern, not disk intrinsically beating memory.
- Impact: Large sequential scans may justify explicit asynchronous I/O when page-mapping latency dominates and engineering cost is acceptable.
- Watch next: Results against prefaulted or parallelized `mmap`, huge-page variants, and comparable CPU and cache accounting.
