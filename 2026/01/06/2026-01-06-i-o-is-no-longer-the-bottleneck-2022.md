# I/O is no longer the bottleneck? (2022)

- Score: 253 | [HN](https://news.ycombinator.com/item?id=46506994) | Link: https://stoppels.ch/2022/11/27/io-is-no-longer-the-bottleneck.html

### TL;DR

Testing whether storage still limits simple stream processing, Peter Stoppels measured 1.6 GB/s cold-cache reads and 12.8 GB/s warm-cache reads, while an optimized C word-frequency counter managed 278 MB/s. Moving lowercase conversion into a vectorizable pass reached 330 MB/s; a hand-written AVX2 word counter reached 1.45 GB/s warm. He concluded computation remained competitive with cold storage. Commenters corrected his interpretation of time: cold execution spent about 82 milliseconds idle, meaning the disk path was still slightly limiting, and emphasized that bottlenecks depend on workload, access pattern, and measurement.

### Comment pulse

- A detailed correction showed real time exceeded combined user and system CPU time, revealing idle waiting and a slight storage bottleneck.
- Debate over per-core memory limits produced widely different benchmarks, highlighting cache state, non-temporal operations, channel count, and methodology.
- Practitioners reframed the issue around latency versus throughput and advised profiling the actual saturated resource before optimizing.

### LLM perspective

- View: The experiment shows scalar parsing can lag modern storage, but its cold-cache verdict misreads timing semantics.
- Impact: Data-intensive software increasingly needs vectorization, batching, locality, and format choices rather than assuming disk dominates.
- Watch next: Rebenchmark with CPU utilization, direct I/O, varied block sizes, multiple drives, and end-to-end frequency counting.
