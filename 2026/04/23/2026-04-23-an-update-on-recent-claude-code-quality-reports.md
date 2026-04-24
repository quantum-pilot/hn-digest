# An update on recent Claude Code quality reports

- Score: 525 | [HN](https://news.ycombinator.com/item?id=47878905) | Link: https://www.anthropic.com/engineering/april-23-postmortem

## TL;DR
Anthropic investigated widespread reports that Claude Code had gotten worse and found three product-layer causes, not an API-level model regression. Lowering the default “reasoning effort” to cut latency, a buggy cache optimization that repeatedly discarded prior “thinking” on idle sessions, and a system prompt enforcing strict brevity together reduced code quality, memory, and reliability. All have been reverted or fixed, usage limits reset, and Anthropic promises broader evals, tighter prompt controls, and more dogfooding, but users remain wary and compare results with OpenAI.

## Comment pulse
- Idle-session cache tweak feels like cost-cutting disguised as latency optimization, breaking long-lived “coworker” workflows and trust. — counterpoint: some see token-cost constraints as unavoidable reality.  
- Others appreciate the detailed postmortem, yet still criticize opaque billing, hidden context policies, and constant prompt churn that users can’t reliably observe or control.  
- Reports of Opus 4.7 regressions, self-referential “prompt injection” chatter, and rule-flouting scripts push some power users toward GPT‑5.x or back to older Claude models.  

## LLM perspective
- Anthropic’s issues highlight how minor product-layer tweaks—effort defaults, caching, prompts—can rival model training in impact on perceived intelligence.  
- Developers must treat UI effort settings, context eviction rules, and system prompts as production dependencies, not cosmetic knobs.  
- Watch for tooling that surfaces context size, cache status, and prompts so users can correlate quality shifts with configuration changes.
