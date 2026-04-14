# I ran Gemma 4 as a local model in Codex CLI

- Score: 237 | [HN](https://news.ycombinator.com/item?id=47744255) | Link: https://blog.danielvaughan.com/i-ran-gemma-4-as-a-local-model-in-codex-cli-7fda754dc0d4

### TL;DR
The author tested whether Gemma 4 can replace a cloud LLM for daily agentic coding in Codex CLI. They ran Gemma 4 locally on a 24 GB M4 Pro Mac (26B MoE via llama.cpp) and a GB10 Blackwell box (31B dense via Ollama), then compared both to GPT‑5.4 on a realistic “write code + tests” task. Both local setups eventually succeeded, but needed more retries and time. Findings: Gemma 4’s tool-calling finally makes local agents viable, model quality matters more than token speed, and cloud still wins for first-pass reliability—suggesting a hybrid local/cloud workflow.

---

### Comment pulse
- Gemma 4 26B is exceptionally strong on one-shot coding, close to frontier models → but degrades on agentic tasks, tools, and long-context reasoning—possible overfitting and scaling limits.  
- Many readers: “obviously quality > speed” → agentic failures, rabbit holes, and retries dominate wall-clock time; raw tok/s only matters for huge straightforward generations.  
- Community setups vary widely → people report success with LM Studio, GPUs, higher context, and different agents; some criticize the article’s tool-calling claims as outdated or too narrow.

---

### LLM perspective
- View: For real-world coding agents, robustness of tool use and planning beats marginal speed or parameter-count gains.  
- Impact: Local-first workflows become practical for privacy-sensitive or high-volume users, but cloud remains preferred for tricky, time-critical work.  
- Watch next: Better open models tuned for agentic reliability; standardized tool-calling benchmarks; smarter hybrid orchestrators that auto-route tasks between local and cloud.
