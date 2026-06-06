# Qwen3.7-Max: The Agent Frontier

- Score: 593 | [HN](https://news.ycombinator.com/item?id=48205626) | Link: https://qwen.ai/blog?id=qwen3.7

### TL;DR
Qwen3.7-Max is Alibaba’s new proprietary “agent-first” LLM targeting long-horizon, tool-using workflows: coding, office automation, and multi-hour autonomous tasks. Benchmarks show it near or slightly ahead of current frontier models on coding agents, general agents, hard reasoning (GPQA Diamond, HMMT, Apex), multilingual tasks, and kernel optimization. A headline demo: a 35‑hour fully autonomous CUDA-style kernel optimization on unseen hardware, achieving 10× speedup via 1,100+ tool calls. HN discussion focuses on throughput/token efficiency, US-friendly hosting, and benchmark cherry-picking vs. real-world performance.

---

### Comment pulse
- Strong benchmarks and low hallucination rates → excitement about SOTA Chinese models, but concern that “non-hallucination” just measures agreement with a possibly flawed test set.  
- Local users → Qwen 3.6 is already a good Claude Code alternative, but speeds on consumer hardware are marginal; Qwen “Max” models remain closed/cloud-only.  
- US production use → people want a US-domiciled endpoint; others argue for reciprocity in cross-border access—counterpoint: some access via Fireworks/Alibaba DCs partly mitigates this.  
- Benchmarks → skepticism about omitting newest rivals (Opus 4.7, GPT5.5, Gemini Flash 3.5); many expect cherry-picking and benchmark-optimized tuning vs. lived quality.

---

### LLM perspective
- View: Qwen3.7-Max pushes hardest on long-horizon, tool-rich workflows rather than raw chat quality alone.  
- Impact: Strong pressure on Western closed models in coding, agents, and kernel optimization, especially for cost‑sensitive or China‑centric ecosystems.  
- Watch next: Independent end‑to‑end agent benchmarks, real-world latency/throughput data, and whether any open-weights variant inherits these agent capabilities.
