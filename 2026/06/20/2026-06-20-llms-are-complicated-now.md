# LLMs Are Complicated Now

- Score: 160 | [HN](https://news.ycombinator.com/item?id=48605355) | Link: https://ianbarber.blog/2026/06/19/llms-are-complicated-now/

### TL;DR

Modern LLMs have moved beyond uniform Transformer stacks into attention variants, expert routing, integrated vision/audio encoders, and multi-GPU communication. This makes optimized kernels load-bearing: a new component may look inferior because its incumbent is fused, yet hand-optimizing every experiment is too costly and generated kernels require trusted baselines. The author says architectures and tooling must be composable and verifiable upfront, citing PyTorch FlexAttention. HN agreed complexity is rising but split between diminishing easy gains and an incumbent optimization moat; llama.cpp’s incomplete support for newer models offered practical evidence.

### Comment pulse

- Incremental gains now cost more engineering → commenters framed architectural elaboration as the mature phase after scaling, data, and straightforward application gains flatten.
- Optimization creates incumbent advantage → heavily fused existing components set unfair baselines for promising alternatives — counterpoint: small-scale experiments can partially reduce software’s moat.
- Architecture comparisons need careful controls → Llama 3 versus Nemotron shows divergence, but GLM 5.2 suggests some modern families remain structurally similar.

### LLM perspective

- **View:** Research flexibility is now a systems property; model ideas cannot be evaluated independently of compilers, kernels, communication, and implementations.
- **Impact:** Smaller teams face rising entry costs, while framework authors become gatekeepers to which architectural ideas can be tested credibly.
- **Watch next:** Benchmark FlexAttention-style abstractions on compile time, fusion quality, numerical parity, distributed scaling, debugging ergonomics, and time-to-first-valid experiment.
