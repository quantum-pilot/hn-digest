# Qwen3.5: Towards Native Multimodal Agents

- Score: 363 | [HN](https://news.ycombinator.com/item?id=47032876) | Link: https://qwen.ai/blog?id=qwen3.5

### TL;DR

Alibaba’s open-weight Qwen3.5-397B-A17B combines native vision-language training, sparse mixture-of-experts, and hybrid linear/full attention: 397 billion total parameters but 17 billion active per pass. Qwen claims competitive frontier performance across reasoning, coding, tools, documents, video, and GUI agents, alongside 201 languages and much faster long-context decoding than earlier Qwen models. The hosted Plus version defaults to one million tokens and adaptive tools. Discussion welcomes RL scaling and quantized releases, but wants smaller vision models and contamination-resistant tests that distinguish learned capability from memorized viral puzzles.

### Comment pulse

- Gains reportedly come from scaling diverse RL environments → post-training, not next-token pretraining alone, increasingly shapes agent behavior.
- Passing the car-wash riddle proves little after it went viral → evaluation needs generated, novel variants and repeated sampling.
- The 397B model strains local hardware → users request 80–110B multimodal releases and debate aggressive quantization versus smaller higher-precision models.

### LLM perspective

- **View:** Qwen3.5’s main contribution is capability density, not outright benchmark leadership.
- **Impact:** Open-weight users gain multimodal agents, but practical deployment still requires unusually large memory.
- **Watch next:** Independent benchmarks, smaller checkpoints, long-context reliability, tool safety, and real throughput on commodity systems.
