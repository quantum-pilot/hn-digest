# A 10 year old Xeon is all you need

- Score: 667 | [HN](https://news.ycombinator.com/item?id=48353348) | Link: https://point.free/blog/gemma-4-on-a-2016-xeon/

### TL;DR

An experiment runs quantized Gemma 4 26B-A4B at reading speed on a 2016 eight-core Xeon with 128GB system memory and no GPU. Using ik_llama.cpp, the author combines an MTP speculative drafter, CPU-aware MoE routing, fused projections, runtime weight repacking, memory locking, Flash Attention, and compressed KV caching; a 262K context consumes about 82GB. The lesson is that local inference is often memory-bound and software-limited, not merely silicon-limited. HN applauded the result while debating hardware details, electricity economics, and whether local open models threaten hosted AI.

### Comment pulse

- Refurbished servers can democratize private inference → several users reported useful 8–12 token/second setups costing under $500 with ample RAM.
- Total cost remains workload-dependent → electricity, noise, and maintenance can exceed cheap hosted tokens — counterpoint: 85W estimates and 4U cooling soften objections.
- Reproducibility needs scrutiny → commenters questioned the stated DDR3 support, SMT rationale, and whether cache-routing explanations match expert sizes.

### LLM perspective

- **View:** The real moat is operational knowledge: optimized local models exist, but 25 obscure flags and specialized forks limit accessibility.
- **Impact:** Homelab users gain privacy and predictable costs; mainstream users still benefit more from managed APIs and supported runtimes.
- **Watch next:** Published token rates, wall-power measurements, quality across quantizations, automated tuning, and upstream support for MTP graph splitting.
