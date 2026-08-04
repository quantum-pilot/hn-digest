# Qwen 3.6 27B is the sweet spot for local development

- Score: 549 | [HN](https://news.ycombinator.com/item?id=48721903) | Link: https://quesma.com/blog/qwen-36-is-awesome/

### TL;DR

The author recommends dense Qwen 3.6 27B as a local coding sweet spot: slower but more instruction-following and capable than the 35B-A3B mixture-of-experts variant. An 8-bit llama.cpp setup with multi-token prediction reached 32 tokens/second using 42 GB on a 128 GB M5 Max; 4-bit weights fit below 18 GB. One-shot app demos and benchmarks suggested mid-2025 frontier quality. HN disputed the conclusion: greenfield clones under-test long-context repository work, quantization can degrade it, premium hardware is hot and expensive, and APIs often cost less—while local users value privacy, permanence, and control.

### Comment pulse

- Demo selection inflates capability → zero-shot clones resemble training examples; niche codebases, architectural exploration, and long contexts expose looping and weak decisions.
- Local economics depend on sunk hardware → APIs win against a $6,699 laptop — counterpoint: existing GPUs make marginal cost mostly electricity.
- Thermals reshape deployment → sustained inference makes laptops hot and loud, favoring a headless workstation accessed over LAN or VPN.

### LLM perspective

- **View:** Local models win on sovereignty and guaranteed availability, not absolute capability or acquisition-cost efficiency.
- **Impact:** Developers with sensitive code gain an offline assistant; teams expecting autonomous monolith work still need stronger remote models.
- **Watch next:** Benchmark real repository edits, 100K-context retention, quantization loss, energy per task, thermal throttling, and total ownership cost.
