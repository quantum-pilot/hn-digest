# Show HN: A real-time strategy game that AI agents can play

- Score: 188 | [HN](https://news.ycombinator.com/item?id=47149586) | Link: https://llmskirmish.com/

### TL;DR

LLM Skirmish benchmarks five models by having each write and revise code that controls a one-on-one real-time strategy bot across five rounds. Its 50-match tournament placed Claude Opus 4.5 first at 85–15 and Elo 1778, followed by GPT-5.2 at 68–32. Claude and GLM improved most over later rounds, while Gemini collapsed after a strong opening, possibly from context overload or a harness issue. Separate scripted simulations and cost data suggest GPT offered strong value, while inexpensive Grok traded substantial quality for price.

### Comment pulse

- Some readers questioned calling revisions learning, since models write scripts and receive match logs rather than perceive a live visual game.
- Viewers criticized unnamed units and weak inspection tools; counterpoint: the benchmark’s main artifact is agent code, not spectator polish.
- Others welcomed a reproducible arena resembling earlier programming contests and wanted broader games, maps, and repeated runs.

### LLM perspective

- **View:** Iterative code adaptation is measurable here, but it is narrower than general real-time strategy reasoning.
- **Impact:** The arena exposes tradeoffs among capability, context management, brittleness, and inference cost.
- **Watch next:** More seeds, maps, opponents, and checks for harness-specific failure modes.
