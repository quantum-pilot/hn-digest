# OpenAI Jalapeño: Better than Nvidia Blackwell

- Score: 575 | [HN](https://news.ycombinator.com/item?id=49434378) | Link: https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia

### TL;DR

OpenAI’s first inference ASIC, Jalapeño, reportedly beats Blackwell and early Rubin results on tokens per watt using single-token prediction. Its clean-sheet design combines HBM4, 15.4TB/s bandwidth, low-overhead memory movement, homogeneous prefill/decode capacity, and AI-written Gluon kernels. A0 engineering samples ran several open models, while production ramps through 2027. HN found the engineering pace notable but distrusted SemiAnalysis’s glowing framing, provider-supplied numbers, easier 8k/1k tests, missing AgentX results, and comparisons against differently mature hardware.

### Comment pulse

- Benchmark credibility remains unsettled → in-person verification covered InferenceX runs, not the full suite, while all reported numbers came from OpenAI.
- General inference hardware may age better than baked-in weights → model-specific silicon promises efficiency — counterpoint: long design cycles invite software obsolescence.
- Specialized accelerators appear durable → efficiency incentives favor them, but foundries, memory vendors, and Broadcom may capture dominance beneath competing designs.

### LLM perspective

- View: Jalapeño’s most consequential claim is rapid hardware-software co-design, not a premature victory over Nvidia’s shipping ecosystem.
- Impact: Successful deployment would lower OpenAI’s power constraint and vendor dependence while pressuring merchant accelerators on inference economics.
- Watch next: Require independent AgentX benchmarks, Rubin parity comparisons, B0 validation, production yields, reliability data, and real speculative-decoding results.
