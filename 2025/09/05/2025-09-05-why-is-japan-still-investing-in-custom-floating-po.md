# Why is Japan still investing in custom floating point accelerators?

- Score: 236 | [HN](https://news.ycombinator.com/item?id=45141907) | Link: https://www.nextplatform.com/2025/09/04/why-is-japan-still-investing-in-custom-floating-point-accelerators/

### TL;DR

Japan-backed Pezy Computing is preparing the SC4s, a 5-nanometer accelerator with 2,048 processing elements, 16,384 threads, 96 GB of HBM3, and 3.2 TB/s memory bandwidth for ExaScaler systems. Its SPMD architecture favors many simple cores, explicit scheduling, layered caches, and high-precision HPC rather than GPU-style lockstep execution. The article argues domestic accelerator expertise hedges GPU scarcity and export restrictions, but several power, efficiency, SC5s, and comparative-performance figures are the author's estimates or conjectures; real-world SC4s results await shipment.

### Comment pulse

- Readers emphasize HPC and FP64 workloads, noting that newer AI-focused GPUs may prioritize lower precision.
- Software maturity and cluster-scale purchasing, not merely chip performance, are seen as major barriers to broader competition with Nvidia.

### LLM perspective

- View: Pezy's strategic value is capability retention and workload diversity, even without displacing commodity GPUs.
- Impact: A viable alternative can preserve domestic accelerator skills and supply options for high-precision national computing workloads.
- Watch next: Shipped power draw, independent FP64 benchmarks, software portability, cluster availability, pricing, and FugakuNext participation.
