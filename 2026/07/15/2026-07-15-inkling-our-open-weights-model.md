# Inkling: Our Open-Weights Model

- Score: 585 | [HN](https://news.ycombinator.com/item?id=48924912) | Link: https://thinkingmachines.ai/news/introducing-inkling/

### TL;DR
Inkling is an open‑weights Mixture‑of‑Experts model (975B total, 41B active) with up to 1M context and native text‑image‑audio reasoning, trained on 45T multimodal tokens. It emphasizes controllable “thinking effort” to trade cost for quality, strong agentic coding, solid multimodal/forecasting performance, and comparatively robust safety. A self‑fine‑tuning demo (lipogram behavior) showcases their Tinker platform; Inkling‑Small offers similar quality at lower latency. HN discussion centers on its role as a US open alternative, the fine‑tuning‑infra business model, and rising complexity of model development.

---

### Comment pulse
- US finally has a competitive, non‑Chinese open model → people want a “DeepSeek/Zhipu for America”; Inkling might fill that niche — counterpoint: Arcee, AllenAI, Meta also compete.
- Open weights + hosted fine‑tuning API is attractive → enterprises can own specialized checkpoints while Thinking Machines sells infra, tooling, and managed training.
- Modern LLMs demand huge, multi‑stage pipelines → dozens of specialized steps favor larger teams; individual “clever trick” research now rarely suffices.

---

### LLM perspective
- View: Inkling targets “best customizable base” rather than leaderboard dominance, leaning on effort control, multimodality, and open weights.
- Impact: Strong candidate for agentic coding, forecasting, and audio‑centric workflows needing long context and owned finetuned models.
- Watch next: Real‑world long‑context behavior, audio quality vs omni models, Tinker adoption metrics, and full Inkling‑Small release/benchmarks.
