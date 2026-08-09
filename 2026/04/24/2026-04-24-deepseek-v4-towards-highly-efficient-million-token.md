# DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence

- Score: 157 | [HN](https://news.ycombinator.com/item?id=47885014) | Link: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro

### TL;DR

DeepSeek-V4 introduces two million-token Mixture-of-Experts models: Pro has 1.6 trillion total parameters with 49 billion activated per token, while Flash has 284 billion total and 13 billion active. Hybrid compressed attention is claimed to cut Pro’s one-million-token single-token inference FLOPs to 27% of V3.2 and its KV cache to 10%; training used more than 32 trillion tokens plus specialist reinforcement learning and distillation. Published evaluations show strong open-model coding and reasoning, though not universal frontier leadership. HN praised price-performance but corrected assumptions that active parameters determine memory fit.

### Comment pulse

- Routing activates different experts per token, so all weights still need storage; disk streaming is theoretically possible but painfully slow.
- One Flash user reported excellent Common Lisp code after feeding back an initial runtime error.
- Some estimate a two-month frontier gap — counterpoint: benchmark parity may not transfer to specific production tools or workflows.

### LLM perspective

- Independent tests should measure full one-million-token retrieval, reasoning degradation, latency, memory, and cost.
- Distilled or quantized derivatives may matter more locally than hosting the full 1.6-trillion-parameter model.
- Publish serving details and comparable reasoning budgets before interpreting cross-vendor benchmark differences.
