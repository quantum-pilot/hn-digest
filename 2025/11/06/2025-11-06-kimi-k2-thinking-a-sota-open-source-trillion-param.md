# Kimi K2 Thinking, a SOTA open-source trillion-parameter reasoning model

- Score: 533 | [HN](https://news.ycombinator.com/item?id=45836070) | Link: https://moonshotai.github.io/Kimi-K2/thinking.html

- TL;DR
  - Moonshot’s Kimi K2 Thinking is an open‑weight “thinking agent” that interleaves 200–300 tool calls with step‑by‑step reasoning, scoring SOTA on HLE 44.9% (with tools), BrowseComp 60.2%, and SWE‑bench Verified 71.3%. It scales test‑time “thinking tokens” and tool use; chat mode is live, full agentic mode coming, API available. HN debates focus on practicality: trillion‑parameter branding vs MoE ~32B active compute, real‑world costs and OpenRouter pricing, “open source” vs open weights, and a push for smaller, specialized local agents.

- Comment pulse
  - Smaller local agents vs giant models; others say small models underperform; K2 is MoE, ~32B active parameters per token.
  - Chinese labs release strong open-weight models; US/EU prioritize monetization and privacy concerns — counterpoint: OpenAI’s GPT-OSS exists, but openness varies.
  - OpenRouter pricing appears low; likely near bare hardware cost or subsidized; closed providers’ margins exclude training amortization.

- LLM perspective
  - View: Tool-augmented test-time scaling plus MoE reduces per-token activation; trillion-parameter branding hides ~32B active compute.
  - Impact: Stronger autonomous browsing/coding agents; lower-cost inference pressures closed models on price-performance.
  - Watch next: Full agentic mode, reproducibility artifacts, benchmark settings, and long-horizon reliability under 200–300 sequential tool calls.
