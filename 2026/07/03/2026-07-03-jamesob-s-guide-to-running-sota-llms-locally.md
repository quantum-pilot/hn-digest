# Jamesob's guide to running SOTA LLMs locally

- Score: 256 | [HN](https://news.ycombinator.com/item?id=48775921) | Link: https://github.com/jamesob/local-llm

### TL;DR

The guide offers two local-inference tiers: roughly $2,000 for dual RTX 3090s running Qwen3.6-27B and Whisper, or a four-card, 384GB-VRAM rig serving a pruned, mixed 8/4-bit GLM-5.2 derivative. The latter actually totals about $52,000 before custom effort, using an EPYC base, Gen4 PCIe switch, BIOS/kernel P2P tuning, Docker runners, and aggressive power caps. HN valued privacy, unlimited usage, and independence, but warned that quantization and removed experts can degrade long-horizon coding, published parent-model benchmarks no longer apply, and cloud or 128GB unified-memory systems may be saner.

### Comment pulse

- Compression claims need workload benchmarks → removing roughly 22% of experts and quantizing weights can compound small errors across long-context tasks.
- Ownership economics depend on utilization → $52,000 dwarfs $200 monthly plans — counterpoint: enterprise API volumes can exceed $4,000 monthly.
- Middle tiers exist → 128GB unified-memory machines, single 24GB GPUs, cloud rentals, or SSD offload trade speed, cost, heat, and control differently.

### LLM perspective

- **View:** Local SOTA is a systems project, not a purchase: model transformation, interconnect, power, software, and evaluation jointly determine usefulness.
- **Impact:** Privacy-sensitive solo users gain autonomy; teams needing concurrency, peak quality, or low maintenance still favor hosted capacity.
- **Watch next:** Publish task-level evaluations for each quant, energy-per-token, concurrent throughput, context limits, and total ownership cost including depreciation.
