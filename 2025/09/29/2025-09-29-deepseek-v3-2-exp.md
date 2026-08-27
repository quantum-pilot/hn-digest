# DeepSeek-v3.2-Exp

- Score: 295 | [HN](https://news.ycombinator.com/item?id=45412098) | Link: https://github.com/deepseek-ai/DeepSeek-V3.2-Exp

### TL;DR

DeepSeek-V3.2-Exp is an experimental 671-billion-parameter model testing DeepSeek Sparse Attention for cheaper long-context training and inference. DeepSeek says it matched V3.1-Terminus closely across public reasoning and agent benchmarks while reducing attention cost, and released model weights plus readable and optimized kernels under MIT terms. SGLang and vLLM support arrived immediately. HN discussion focused on falling inference prices, the importance of cached-input pricing for agents, possible prompt-training policies at third-party routers, and how the indexer approximates attention before selecting 2,048 tokens.

### Comment pulse

- Efficiency may broaden access → commenters considered price declines as important as capability gains for widespread model use.
- Agent economics depend on caching → repeated context dominates many workloads; DeepSeek’s API reportedly prices cache hits below misses.
- Sparse attention intrigued readers → the indexer still scans context, but full attention operates on a selected subset.

### LLM perspective

- View: This release is an architecture experiment prioritizing comparable quality at lower long-context cost, not a capability leap.
- Impact: Researchers and inference providers gain open artifacts for testing sparse-attention deployment across varied hardware.
- Watch next: Independent latency, memory, quality, cache-hit, and long-context retrieval measurements under production workloads.
