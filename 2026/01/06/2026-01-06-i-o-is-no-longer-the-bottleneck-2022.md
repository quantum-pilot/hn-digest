# I/O is no longer the bottleneck? (2022)

- Score: 253 | [HN](https://news.ycombinator.com/item?id=46506994) | Link: https://stoppels.ch/2022/11/27/io-is-no-longer-the-bottleneck.html

### TL;DR
The author revisits the claim that “I/O is no longer the bottleneck” using a word-count benchmark. A straightforward C implementation reaches only a few hundred MB/s, far below sequential read rates. After heavy manual AVX2 vectorization and bit‑twiddling, a custom `wc` hits ~1.5 GB/s on one core, roughly matching cold-disk throughput but still far under warm-cache bandwidth. The exercise illustrates that modern workloads are typically CPU/memory‑bound, and that compilers rarely auto‑vectorize irregular, branchy parsing code.

---

### Comment pulse
- Bottleneck location is nuanced → some argue per‑core memcpy is limited to single‑digit GB/s; others show much higher single‑core bandwidth with tuned AVX/neon. — counterpoint: workload details and measurements differ.
- `time` output was misread → combining user+sys shows the AVX2 version briefly outpaces disk, but a large fraction of CPU is now in kernel I/O paths.
- Performance diagnosis is contextual → bottleneck is whichever resource saturates first; real‑world slowness is often latency/serialization (tiny reads, scattered data) rather than raw disk bandwidth.

---

### LLM perspective
- View: Treat parsing and analytics as CPU/memory‑bound; invest in SIMD‑friendly formats and algorithms rather than over‑optimizing raw disk I/O.
- Impact: Systems handling logs, text, and serialization gain most from zero‑copy layouts, fewer branches, and explicit vectorization.
- Watch next: Benchmarks of end‑to‑end pipelines (I/O + parse + compute), newer ISA features (AVX‑512, SVE2), and profiling tools that surface per‑core bandwidth ceilings.
