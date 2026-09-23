# How did AMD Ryzen get 50% faster in two years?

- Score: 464 | [HN](https://news.ycombinator.com/item?id=49758709) | Link: https://lemire.me/blog/2026/09/18/how-did-amd-ryzen-get-50-faster-in-two-years/

### TL;DR

Comparing AMD’s eight-core X3D desktop chips released from 2022 through 2024, Geekbench 6 scores rose 47% single-core and 58% multi-core. A 15% boost-clock increase explains only part of it: Zen 5 widened dispatch, ALUs, SIMD execution, loads, stores, caches, and the reorder buffer, enabled by roughly 50% more transistors. HN readers praised real-workload performance but noted the framing compresses architectural history because Zen 3 first shipped in 2020, despite the 5800X3D arriving later.

### Comment pulse

- Zen 5 rewards optimized workloads → one reader reported sustained 6 IPC per core alongside exceptional branch-prediction and L2-hit rates.
- Wider cores delivered more than clock gains → doubled SIMD width and larger scheduling structures expose more instruction-level and data parallelism.
- The two-year headline is product-specific → X3D release timing makes generations appear closer than their underlying architecture debuts.

### LLM perspective

- View: CPU progress continues through wider execution and better scheduling, not merely higher frequencies or core counts.
- Impact: Vectorizable, cache-friendly workloads benefit most; ordinary applications depend on compilers and code exposing available parallelism.
- Watch next: Compare Zen 6 desktop width, latency, efficiency, and application benchmarks rather than headline scores alone.
