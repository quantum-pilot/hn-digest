# Cerebras Code now supports GLM 4.6 at 1000 tokens/sec

- Score: 175 | [HN](https://news.ycombinator.com/item?id=45852751) | Link: https://www.cerebras.ai/code

- TL;DR
    - Cerebras adds GLM‑4.6 to its Code service, delivering ~1,000 tok/s with Free, $50 Pro (24M tokens/day) and $200 Max (120M) tiers. It targets code generation via existing editors and claims top tool‑calling. HN reports: the speed materially boosts productivity, especially for web dev; GLM 4.6 is “good enough” but trails Claude Sonnet’s polish; some prefer Z.ai’s cheaper plan. Token use grows cumulatively in chats; occasional congestion occurs. On Z.ai, GLM lacks web search/image; users route those to other models.
- Comment pulse
    - Speed shifts workflow → 1000 tok/s enables rapid iteration; use Claude/GPT as planner, GLM as actor — counterpoint: non‑web tasks still need careful, line‑by‑line review.
    - Quality tradeoff → GLM 4.6 is good enough; Sonnet/Codex produce cleaner code but are slower.
    - Integration/limits → Cline works best; other agents hit per‑minute limits. Chat history consumes tokens fast; occasional API congestion; unclear if prefix caching helps.
- LLM perspective
    - View: Speed is now the differentiator; code quality parity matters less when latency drops 10×.
    - Impact: Agentic IDEs become usable; token quotas, not thinking time, gate work; vendors compete on caching and streaming.
    - Watch next: Prefix/state caching, reliable 1k tok/s under load, and standardized planning‑acting pipelines with cost/latency dashboards.
