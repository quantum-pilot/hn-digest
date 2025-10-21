# Alibaba Cloud says it cut Nvidia AI GPU use by 82% with new pooling system

- Score: 322 | [HN](https://news.ycombinator.com/item?id=45643163) | Link: https://www.tomshardware.com/tech-industry/semiconductors/alibaba-says-new-pooling-system-cut-nvidia-gpu-use-by-82-percent

TL;DR
Alibaba Cloud’s Aegaeon pools GPUs across many LLMs via token-level scheduling, packing multiple models per Nvidia H20 and boosting “goodput” up to 9×. In a multi-month beta for long‑tail models, required GPUs fell from 1,192 to 213 (−82%). Results lean on Alibaba’s integrated stack (eRDMA, serving system) and may not generalize fully. HN notes the savings target cold models (17.7% of GPUs for 1.35% of requests), so fleet‑wide gains are smaller; others see export controls nudging China toward software‑driven efficiency.

Comment pulse
- 82% cut applies to unpopular models → 17.7% GPUs served 1.35% requests; naive extrapolation: ~37.5% cold-model savings, ~6.6% across 30k-GPU fleet.
- Idle isn’t issue; pinning wastes capacity → Token-level multiplexing shares one GPU across models, avoids reload thrash, raises utilization — counterpoint: depends on fast fabrics.
- Export controls spur efficiency innovation → Scarcity of H20s pushes Chinese teams toward software/resource scheduling gains; some expect broader open-sourcing to benefit others.

LLM perspective
- View: Token-level GPU pooling makes the long tail economical by multiplexing bursts across models with autoscaling.
- Impact: Cloud providers cut capex and idle time; model marketplaces can host more variants without dedicated GPUs.
- Watch next: Reproducible cross-cloud benchmarks, open-source release, portability to Blackwell/MI300, and sensitivity to network latency and KV-cache sharding.
