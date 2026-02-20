# Anthropic officially bans using subscription auth for third party use

- Score: 606 | [HN](https://news.ycombinator.com/item?id=47069299) | Link: https://code.claude.com/docs/en/legal-and-compliance

### TL;DR
Anthropic’s updated Claude Code legal docs explicitly forbid using consumer Claude subscriptions (Free/Pro/Max) as authentication for any third‑party apps or tools, including the Agent SDK. OAuth tokens from those plans must only be used with Claude’s own products; external developers are told to use metered API keys instead, and Anthropic may enforce this without notice. HN discussion sees this as classic lock‑in and growing API hostility, while others frame it as rational economics to prevent subscription arbitrage and fund long‑term model development.

---

### Comment pulse
- Lock‑in critique → Claude Code seen as an Apple‑style ecosystem grab to capture future profits and control defaults—counterpoint: businesses must retain some value to survive.  
- Model fungibility worry → Commenters expect many comparable models; a too‑closed, opinionated Claude Code could bleed users to more open, API‑friendly competitors.  
- Subscription economics → Flat‑rate plans are loss leaders; banning OAuth reuse blocks arbitrage, unlike OpenAI/Copilot which currently encourage third‑party access to increase stickiness.  

---

### LLM perspective
- View: Clear separation of consumer subscriptions vs API is logical, but abrupt enforcement erodes goodwill among power‑user developers.  
- Impact: Expect shrinkage of unofficial CLIs/editors; more projects standardize on vendor‑neutral APIs or competitors with sanctioned OAuth flows.  
- Watch next: Whether OpenAI, Google, GitHub tighten usage, and if Anthropic offers discounted API tiers for tool-makers replacing wrappers.
