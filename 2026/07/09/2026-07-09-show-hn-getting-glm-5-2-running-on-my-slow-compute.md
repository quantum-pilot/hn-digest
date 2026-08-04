# Show HN: Getting GLM 5.2 running on my slow computer

- Score: 301 | [HN](https://news.ycombinator.com/item?id=48842459) | Link: https://github.com/JustVugg/colibri

### TL;DR

Colibrì is an Apache-licensed pure-C inference engine that runs mixture-of-experts models by treating VRAM, RAM, and NVMe as one hierarchy. For GLM-5.2, only about 40B of 744B parameters activate per token: dense weights remain resident, while 19,456 experts stream from a 372 GB int4 model through LRU caching, learned hot pins, prefetch, batched reads, and CPU/GPU overlap. Performance ranges from 0.05–0.1 token/s on a 25 GB box to 6.8 token/s across six RTX 5090s. The project prioritizes semantic fidelity and measured end-to-end gains over silent model changes or microbenchmark claims.

### Comment pulse

- Usability turns on throughput → 0.05 token/s is impractical for chat — counterpoint: overnight ticket-style agents could tolerate slower local generation.
- The storage-first idea resonated → readers accepted reading routed experts per token rather than buying enough memory for full residency.
- Independent implementations are emerging → commenters described Metal, mmap, Medusa, unified-memory, and llama.cpp experiments targeting affordable personal hardware.

### LLM perspective

- **View:** Sparse activation converts an impossible capacity problem into a difficult placement, bandwidth, caching, and scheduling problem.
- **Impact:** Local frontier inference improves ownership and experimentation, but low-end latency still limits practical interaction and energy efficiency.
- **Watch next:** Compare kernel-managed mmap versus explicit tiers, dual-SSD scaling, cache generalization, speculation break-even, quality, power, and cost per token.
