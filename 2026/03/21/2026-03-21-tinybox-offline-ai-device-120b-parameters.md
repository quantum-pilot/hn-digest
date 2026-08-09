# Tinybox- offline AI device 120B parameters

- Score: 247 | [HN](https://news.ycombinator.com/item?id=47470773) | Link: https://tinygrad.org/#tinybox

### TL;DR

Tiny Corp’s tinybox line packages multi-GPU machines around tinygrad for local training and inference. The $12,000 red v2 combines four Radeon 9070 XTs and 64GB VRAM; the $65,000 green v2 uses four RTX Pro 6000 Blackwell cards and 384GB VRAM. Both are fixed configurations ordered by wire transfer, while a roughly $10 million exabox is planned for 2027. The site markets performance per dollar and framework simplicity. Commenters questioned the headline’s 120B practicality, memory balance, chassis size, and value versus custom builds.

### Comment pulse

- Heavy quantization may fit a 120B model on red, but context cache and quality constraints undermine the simple parameter-count claim.
- Green buyers gain ample accelerator memory — counterpoint: critics expect stronger CPUs, more system RAM, or better electrical provisioning at $65,000.
- Tinygrad’s alpha exit target—twice PyTorch on common papers—prompted requests for precise workloads and hardware-utilization baselines.

### LLM perspective

- **View:** The useful product is a reproducible local appliance; raw model-size marketing obscures workload-specific throughput and latency.
- **Impact:** Privacy-sensitive organizations gain an alternative to rented inference, provided they can operate specialized hardware.
- **Watch next:** Tokens-per-second by quantization, long-context tests, power measurements, support quality, and independent total-cost comparisons.
