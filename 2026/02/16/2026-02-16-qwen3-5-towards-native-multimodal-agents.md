# Qwen3.5: Towards Native Multimodal Agents

- Score: 363 | [HN](https://news.ycombinator.com/item?id=47032876) | Link: https://qwen.ai/blog?id=qwen3.5

### TL;DR
Qwen3.5 is Alibaba’s new flagship open‑weight “native multimodal” MoE model: 397B parameters with only 17B active per token, a 1M‑token context, and built‑in tool use (search, code interpreter). It posts frontier‑level results across language, coding, vision, video, and especially agent benchmarks, emphasizing large‑scale RL in diverse environments rather than just next‑token prediction. The team also details a high‑throughput FP8 training stack and an asynchronous RL framework aimed at long‑horizon, multi‑turn, tool‑using agents.

---

### Comment pulse
- RL, not just next‑token prediction → Gains credited to scaling many RL environments; some want methods to systematically surface “embarrassing” failure cases—counterpoint: continual learning could fix specific glitches.  
- Evaluation and adversarial tests → Idea: auto‑generate novel puzzles via small program interpreters (e.g., Lua) to prevent memorization and truly measure reasoning.  
- Practical use and model sizes → Community offers MXFP4 GGUF quantizations; debate over ultra‑low‑bit vs smaller dense models and calls for 80–110B vision‑capable variants that fit 128 GB setups.

---

### LLM perspective
- View: Qwen3.5 is less about raw benchmarks and more a serious push toward robust, tool‑using, multimodal agents via scaled RL and infra.  
- Impact: Strengthens open ecosystem alternatives to proprietary GPT/Gemini/Claude, especially for vision+video agents and multilingual applications.  
- Watch next: Mid‑size multimodal releases, standardized “unseen” reasoning benchmarks, and whether RL‑scaled agents transfer well to messy real‑world workflows.
