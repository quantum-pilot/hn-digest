# Pro Max 5x quota exhausted in 1.5 hours despite moderate usage

- Score: 511 | [HN](https://news.ycombinator.com/item?id=47739260) | Link: https://github.com/anthropics/claude-code/issues/45756

- TL;DR  
Anthropic Claude Code Max users report 5x quotas draining in ~1.5 hours of moderate coding. Detailed logs first suggested cached prompts were billed at full rate; later community analysis finds cache reads likely don’t hit quota. Instead, a silent regression in cache TTL (1h→5m), frequent cache misses, 1M-token contexts and background agents make each step far more expensive. Anthropic acknowledges UX/efficiency issues, testing smaller default contexts. HN commenters see deliberate service degradation and the end of cheap AI compute.

- Comment pulse  
  - Perception of bait‑and‑switch on quotas → abrupt TTL change, opaque rate-limit math, nagging to shrink context feels like intentional degradation, not a bug.  
  - Many switch tools → Codex, Cursor, Gemini CLI, or local LLMs seen as cheaper, more predictable, even if rougher UX or personality.  
  - Power users share coping tactics → manual compaction, limiting context, avoiding idle sessions; — counterpoint: these only paper over systemic cache bugs.

- LLM perspective  
  - View: This exposes how fragile agentic IDEs are when caching, context growth and hidden automation aren’t tightly instrumented.  
  - Impact: Solo developers and small teams on fixed-price plans feel volatility most; enterprises can absorb costs or negotiate custom quotas.  
  - Watch next: Clear docs on cache/quota math, telemetry surfacing in clients, and “budget mode” models prioritizing predictable spend over raw capability.
