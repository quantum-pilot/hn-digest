# io_uring is faster than mmap

- Score: 284 | [HN](https://news.ycombinator.com/item?id=45132710) | Link: https://www.bitflux.ai/blog/memory-is-slow-part2/

TL;DR
Author benchmarks a single-threaded scan for “10s” over 50 GB. A simple mmap loop hits ~3.7 GB/s; vectorized loop ~5.5 GB/s. A custom io_uring + O_DIRECT pipeline with 6 worker threads reaches ~5.8 GB/s, beating the mmap path because soft page faults and per-page mappings serialize progress. A pure in-RAM buffer shows memory can do 13 GB/s on one NUMA node (7.9 GB/s across 50 GB). HN debates fairness: pre-touch/MAP_POPULATE/hugepages, and caching trade-offs vs O_DIRECT’s user-managed pipeline.

Comment pulse
- mmap stalls on soft faults → per-page mapping latency throttles scans; pre-touch/MAP_POPULATE/hugepages or prefetch likely match io_uring. — counterpoint: readahead helps but not mapping costs.
- O_DIRECT/io_uring shifts caching to user space → better pipelining, worse sharing; Linux lacks an API to share those buffers with the page cache.
- Bandwidth talk: desktop DDR5 per-channel ≥64 GB/s; PCIe x16 ≈64 GB/s; servers may exceed via many lanes/CXL, but DRAM still lower-latency.

LLM perspective
- View: The benchmark highlights path-dependent costs; async I/O hides latency while mmap’s per-page mapping serializes work.
- Impact: Workloads scanning large files or columnar datasets can benefit from direct, pipelined I/O with NUMA-aware, vectorized processing.
- Watch next: Compare against mmap with MAP_POPULATE, madvise, THP/hugetlb, pre-touch, tuned readahead; measure minor faults, TLB misses, NUMA traffic, CPU vectors.
