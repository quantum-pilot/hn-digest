# Deploying DeepSeek on 96 H100 GPUs

- Score: 285 | [HN](https://news.ycombinator.com/item?id=45064329) | Link: https://lmsys.org/blog/2025-05-05-large-scale-ep/

### TL;DR

The SGLang team describes serving DeepSeek-V3 across twelve eight-H100 nodes using separate prefill and decode servers, expert parallelism, DeepEP, DeepGEMM, load balancing, and two-batch overlap. It reports 52.3k input and 22.3k output tokens per second per node for 2,000-token inputs, with up to 5.2× decode throughput over its tensor-parallel baseline. The authors stress remaining latency, sequence-length, workload-shift, and hardware limitations. Commenters disputed whether headline token costs survive utilization, contracts, regional demand, depreciation, and failures.

### Comment pulse

- The engineering result is reproducible and open → cost conclusions depend on deployment economics beyond peak throughput.
- Batch tiers may absorb off-peak capacity → regional constraints and demand peaks can still leave expensive GPUs idle.

### LLM perspective

- View: Phase-specific scheduling turns MoE complexity into throughput, but economics remain workload-specific.
- Impact: Large inference operators gain an open blueprint; smaller operators still face utilization and capital risk.
- Watch next: Test production distributions, end-user latency, longer contexts, and measured total cost at realistic utilization.
