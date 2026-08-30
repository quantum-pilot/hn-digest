# Samsung's Processing-in-Memory (PIM)

- Score: 257 | [HN](https://news.ycombinator.com/item?id=49487341) | Link: https://chipsandcheese.com/p/hot-chips-2026-samsungs-processing

### TL;DR

Samsung's LPDDR5X-PIM places multiply-accumulate units beside each of 16 DRAM banks, exposing 614 GB/s of internal bandwidth while retaining standard memory-controller compatibility. Special rows reinterpret ordinary commands to configure and trigger parallel computation, reaching a stated 2.4 TOPS per package. The analysis argues this clever compatibility creates severe software problems: PIM mode conflicts with normal accesses, caches, speculation, interrupts, multitasking, and data movement between banks. Commenters saw niche vector and AI potential but noted decades of unsuccessful PIM proposals.

### Comment pulse

- Co-locating fixed-weight computation reduces external traffic → bandwidth-heavy, regular workloads could benefit disproportionately.
- Standard DDR commands avoid controller replacement → mode overloading instead complicates isolation, coherence, scheduling, and debugging.
- Specialized accelerators often fail commercially → counterpoint: large inference demand may finally justify redesigning the surrounding architecture.

### LLM perspective

- View: Samsung demonstrates feasible DRAM-side arithmetic, not transparent acceleration for today's general-purpose systems.
- Impact: Adoption would require coordinated CPU, memory-controller, operating-system, compiler, and workload changes.
- Watch next: Demand end-to-end benchmarks including isolation, cache effects, context switches, energy, utilization, and software complexity.
