# Kimi K3, and what we can still learn from the pelican benchmark

- Score: 255 | [HN](https://news.ycombinator.com/item?id=48947717) | Link: https://simonwillison.net/2026/Jul/16/kimi-k3/

- TL;DR  
  - Moonshot AI’s Kimi K3 is a 2.8T-parameter Chinese model with near–frontier performance and premium pricing, now tested against Simon Willison’s long-running “pelican on a bicycle” SVG prompt. The run exposes K3’s single, very heavy reasoning mode (13k reasoning tokens for a small task), strong vision/alt‑text, and a likely large hidden system prompt, while illustrating why such cute micro‑benchmarks no longer track overall capability yet remain useful for quick, comparable sanity checks. HN dives into hidden prompts and dataset contamination.

- Comment pulse  
  - Pelican SVGs are almost surely in training data; commenters see their own low-traffic blog posts echoed by LLMs within months.  
  - Extra input tokens likely come from an injected reasoning-effort system prompt, similar to DeepSeek’s documented max-mode pre-<think> instructions.  
  - Community riffs on the test: adversarial SWE-bench with random pelican SVG interruptions, MacBook SVG benchmarks, and dashboards comparing cost, speed, and completeness.

- LLM perspective  
  - View: Informal, idiosyncratic probes like pelican SVGs surface quirks—reasoning bloat, geometry limits—that formal leaderboards often miss.  
  - Impact: Practitioners get a fast mental model of a new LLM’s cost profile and output style before deeper integration.  
  - Watch next: standardized agentic benchmarks that inject distracting subtasks, long contexts, and tool calls, revealing robustness beyond static Q&A scores.
