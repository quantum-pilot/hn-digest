# MegaTrain: Full Precision Training of 100B+ Parameter LLMs on a Single GPU

- Score: 248 | [HN](https://news.ycombinator.com/item?id=47689174) | Link: https://arxiv.org/abs/2604.05091

### TL;DR

MegaTrain reframes one GPU as a transient compute engine while keeping model parameters and optimizer state in CPU memory. It streams each layer onto the device and gradients back out, using double-buffered CUDA pipelines to overlap transfer and compute, plus stateless layer templates to avoid persistent autograd metadata. On an H200 paired with 1.5 TB of host RAM, the authors report full-precision training up to 120B parameters, 1.84× DeepSpeed ZeRO-3 throughput at 14B, and 512K-context training for a 7B model on GH200.

### Comment pulse

- Home users saw a path beyond VRAM limits → commenters cautioned that bandwidth, context memory, and training time remain severe constraints.
- Novelty was disputed → similar offloading is intuitive, but undocumented private implementations are not reproducible evidence.
- “Single GPU” sounded accessible until hardware details appeared → an H200 with 1.5 TB RAM is still specialized, expensive infrastructure.

### LLM perspective

- **View:** MegaTrain expands feasible model size by spending host memory and time, not by making giant training cheap.
- **Impact:** Researchers with one accelerator can attempt experiments formerly requiring clusters, provided they can tolerate slower throughput.
- **Watch next:** Code release, end-to-end training times, consumer-GPU tests, energy costs, and scaling behavior with eight GPUs.
