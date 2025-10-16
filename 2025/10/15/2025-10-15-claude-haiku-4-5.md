# Claude Haiku 4.5

- Score: 415 | [HN](https://news.ycombinator.com/item?id=45595403) | Link: https://www.anthropic.com/news/claude-haiku-4-5

- TL;DR
  - Anthropic’s Claude Haiku 4.5 is a “small” model claiming near-Sonnet 4 coding quality at far lower cost ($1/$5 per million tokens) and higher speed, with gains in computer-use and agentic orchestration (Sonnet 4.5 as planner, Haiku 4.5 as parallel workers). It ships broadly (API, Bedrock, Vertex) and is classified ASL‑2, with lower misalignment rates than prior models. HN reports strong real-world latency and precise code edits, but flags occasional hallucinations, product/billing confusion, and fatigue from constant model/tool switching.

- Comment pulse
  - Real-world speed wins → 180–220 tok/s, ~0.7s TTF; handles playful SVG “pelican” tests well — counterpoint: one doc-fetch task hallucinated; Sonnet answered correctly.
  - Targeted code edits → avoids touching unrelated files, making changes faster/cheaper in practice; worries about multi-minute task drift and ambiguous Claude Code billing/limits.
  - Model fatigue → developers want neutral routing and stable tooling; stopgap picks include Copilot Pro+, OpenRouter auto, or running multiple models and choosing best.

- LLM perspective
  - View: Small, fast models nearing frontier quality shift many agentic workloads to cheaper tiers.
  - Impact: Coding assistants, support bots, and multi-agent systems favor Haiku workers with a larger planner.
  - Watch next: Independent long-horizon reliability tests, prompt-agnostic benchmarks, and clear per-product quotas/billing.
