# The fate of "small" open source

- Score: 125 | [HN](https://news.ycombinator.com/item?id=45947639) | Link: https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/

- TL;DR
  Lawson argues LLMs and built‑in platform features have made tiny utility libraries obsolete: developers can paste bespoke snippets instead of adding dependencies, but we lose teaching-oriented docs and shared maintenance. He suggests focusing open source on novel, harder projects LLMs can’t synthesize. HN debates whether replacing npm micro‑deps with generated code reduces supply‑chain risk or invites “vibe coding” and fragmented fixes; others note AI is itself a dependency, while some defend open‑sourcing small code for learning and copy‑pasting.

- Comment pulse
  - Replace micro-dependencies with LLM snippets → reduces bloat and supply-chain risk; bugs fragment across codebases, weakening shared fixes — counterpoint: encourages 'vibe coding' and debt.
  - AI is a dependency too → pasted code lacks updates and provenance; libraries modernize — counterpoint: snippets are narrowly scoped, easier to read, less bloat.
  - Open-sourcing remains valuable without adoption → readable implementations teach and seed reuse; culture matters (Go’s 'copying' over deps); fears of AI-fueled spam and unemployment persist.

- LLM perspective
  - View: LLMs commoditize trivial utilities; value shifts to novel research, opinionated frameworks, and performance/memory-leak expertise.
  - Impact: Maintainers of micro-libraries lose adoption; teams must track provenance and maintenance of pasted snippets to avoid drift and duplicated bugfixes.
  - Watch next: Tooling: snippet registries, SBOMs for code, linters for model patterns; benchmarks comparing LLM snippets vs libs on correctness and speed.
