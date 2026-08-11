# Arm's Cortex X925: Reaching Desktop Performance

- Score: 258 | [HN](https://news.ycombinator.com/item?id=47229344) | Link: https://chipsandcheese.com/p/arms-cortex-x925-reaching-desktop

### TL;DR

Testing Nvidia’s GB10 at 4GHz, the review finds Arm’s 10-wide Cortex-X925 roughly matches desktop AMD Zen 5 and Intel Lion Cove cores in SPEC CPU2017 integer performance. Its strong branch predictor, approximately 525-instruction out-of-order window, high IPC, 64KB L1 caches, and 2MB L2 offset lower clocks. Zen 5 retains a clear floating-point lead, partly because X925’s 128-bit vectors require more instructions, sometimes over twice as many. HN called missing power data a major gap and wanted comparisons with Apple cores, newer Arm C1 Ultra, and fully vectorized AVX-512 workloads.

### Comment pulse

- X925 reaches parity through IPC rather than frequency, but results vary with instruction count, memory behavior, and compilation.
- Six vector pipes look broad — counterpoint: four load units and narrow registers can starve arithmetic and magnify Zen 5’s width advantage.
- Weak Arm memory ordering may expose concurrency bugs; language memory models and compilers already require portable synchronization on x86 too.

### LLM perspective

- **View:** Desktop-class core performance is established, but platform competitiveness still depends on efficiency, memory, software, and implementer execution.
- **Impact:** Arm partners gain credible workstation silicon; AMD and Intel face stronger architectural competition beyond mobile.
- **Watch next:** Package power, process node, Apple and C1 comparisons, AVX-512 workloads, gaming, and larger-L3 designs.
