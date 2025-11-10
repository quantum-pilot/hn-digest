# Grok 4 Fast now has 2M context window

- Score: 167 | [HN](https://news.ycombinator.com/item?id=45862833) | Link: https://docs.x.ai/docs/models

- TL;DR
    - xAI’s Grok 4 Fast ships a 2,000,000‑token context window with reasoning and non‑reasoning variants, pitched as lightning‑fast and low‑cost; rate limits listed at 4M tokens/min and 480 rpm, with server‑side tool calls free until Nov 21, 2025. HN debates whether huge context beats overall model quality: many prize tokens/sec for productivity, while others doubt today’s models retain or prioritize information across long windows and ask for hard benchmarks. Users report strong practical value—X integration, lax safety, code/data extraction—though brand politics affect adoption.

- Comment pulse
    - Speed and cost → faster tokens/sec preserves focus; cheap “low-intelligence” coding tasks get automated.
    - Long context utility → many models forget or show primacy bias; demand needle‑in‑haystack proofs — counterpoint: whole‑codebase prompts reduce RAG misses.
    - Adoption factors → some avoid Musk’s products; others like X integration and permissive safety; usage rankings show Grok Fast models heavily used.

- LLM perspective
    - View: 2M context is compelling, but utility hinges on retention, salience ranking, and navigation across 1M+ tokens.
    - Impact: Enables fewer retrieval/tool hops, faster agents; may shift IDE assistants toward whole‑repo prompting for refactors and audits.
    - Watch next: Publish long‑context leaderboard, latency and tokens/sec, safety controls, and transparent pricing for reasoning vs completion token mix.
