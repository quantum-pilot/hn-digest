# Qwen3.7-Max: The Agent Frontier

- Score: 593 | [HN](https://news.ycombinator.com/item?id=48205626) | Link: https://qwen.ai/blog?id=qwen3.7

### TL;DR

Alibaba’s proprietary Qwen3.7-Max is positioned as a cloud agent foundation for coding, office automation, MCP workflows, and thousand-step execution across multiple harnesses. The team reports competitive or leading scores across coding, reasoning, multilingual, and tool-use benchmarks, plus a 35-hour autonomous kernel-optimization run using 1,158 tool calls that achieved a 10× speedup on unseen hardware. Availability is promised through Alibaba Cloud Model Studio. HN praised the numbers but questioned token efficiency, closed weights, production access outside Alibaba, benchmark cherry-picking, and comparisons that omit newer rival models.

### Comment pulse

- Benchmark quality may hide wall-clock cost → capable Chinese models often consume more tokens, so slower completion can outweigh nominal output quality.

- Max is not the local-model successor some expected → commenters clarified it is proprietary, cloud-hosted, and likely too large for personal hardware.

- Evaluation framing drew skepticism → published comparisons omit Opus 4.7, GPT-5.5, and Gemini Flash 3.5 — counterpoint: maintaining fresh baselines is costly.

### LLM perspective

- **View:** Long-horizon credibility depends less on peak scores than graceful recovery, stopping behavior, cost, and reproducibility across real harnesses.

- **Impact:** Agent builders gain another frontier backend, but proprietary hosting and jurisdiction constrain sensitive production workloads and local experimentation.

- **Watch next:** Verify pricing, latency, token consumption, rate limits, data handling, independent benchmarks, and reproduction of the 35-hour kernel result.
