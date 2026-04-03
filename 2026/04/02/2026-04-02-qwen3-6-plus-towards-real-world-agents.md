# Qwen3.6-Plus: Towards real world agents

- Score: 406 | [HN](https://news.ycombinator.com/item?id=47615002) | Link: https://qwen.ai/blog?id=qwen3.6

### TL;DR
Qwen3.6-Plus is Alibaba’s new flagship hosted LLM aimed at “real-world agents”: long-context, multimodal, and tightly integrated with tools for coding, web/UI automation, and video workflows. It adds a 1M-token window, better visual reasoning, and agentic coding tuned for systems like OpenClaw, Qwen Code, and Claude Code, plus an API option to preserve chain-of-thought across turns. Benchmarks show near–Claude Opus 4.5 performance at lower cost, but the model is closed-weight, sparking debate about strategy and marketing.

---

### Comment pulse
- Hosted-only, closed model and 4.5-era comparisons → some see bait-and-switch from open weights and mildly deceptive marketing in a commoditizing market.  
- Others argue Chinese labs must keep open-sourcing smaller models because they lack marketing/sales muscle; open weights are their only reliable distribution channel.  
- Some defend Qwen: prior Plus/Max were closed, benchmarks vs GLM/Kimi look strong, and a 4× cheaper Opus-class model still benefits users.  

---

### LLM perspective
- View: This is a push toward end-to-end agents—coding, GUI control, and video workflows—rather than just chat-style assistance.  
- Impact: Strong, cheaper non-Western models pressure OpenAI/Anthropic on pricing and accelerate multi-provider, tool-heavy agent stacks in production.  
- Watch next: open-weight 3.6 variants, independent agentic-coding and GUI benchmarks, and whether "preserve_thinking" reliably cuts costs in real deployments.
