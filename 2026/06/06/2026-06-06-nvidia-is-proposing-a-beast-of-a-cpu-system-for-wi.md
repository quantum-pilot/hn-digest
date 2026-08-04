# Nvidia is proposing a beast of a CPU system for Windows PCs

- Score: 218 | [HN](https://news.ycombinator.com/item?id=48424605) | Link: https://twitter.com/lemire/status/2062880075117113739

### TL;DR

Nvidia proposes a Windows-on-Arm system with 10 performance and 10 efficiency CPU cores, 6,144 CUDA cores, and 128 GB unified memory. The pitch is affordable capacity for local models and gaming, trading dedicated-GPU bandwidth for one large CPU/GPU pool; Cortex-X925 offers SVE2, though AMD’s AVX-512 is stronger on paper. HN challenged the beast label: shared bandwidth and power may halve GPU performance, while Apple and Qualcomm offer strong alternatives. Supporters argued CUDA, fast prompt prefill, flexible allocation, and Nvidia’s ecosystem may matter more than peak specifications.

### Comment pulse

- Unified memory improves capacity utilization → one pool simplifies small systems and bulk purchasing — counterpoint: fixed memory enables expensive segmentation and eliminates upgrades.
- Bandwidth remains the limiter → 128 GB can fit large models, but Blackwell cards reportedly generate tokens 10–20 times faster.
- Ecosystems can outweigh silicon → Qualcomm leads CPU benchmarks yet struggles with Linux support, while Nvidia brings CUDA, distribution, and developer relationships.

### LLM perspective

- **View:** The decisive comparison is complete systems under sustained shared load, because headline core counts ignore contention and thermal budgets.
- **Impact:** Buyers must size capacity, bandwidth, thermals, upgradeability, operating-system support, and workload-specific CUDA dependence together.
- **Watch next:** Demand shipping-system benchmarks for prefill, decode, rasterization, CPU SIMD, power, thermals, memory contention, Linux support, and price.
