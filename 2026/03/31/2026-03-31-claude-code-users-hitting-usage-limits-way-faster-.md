# Claude Code users hitting usage limits 'way faster than expected'

- Score: 263 | [HN](https://news.ycombinator.com/item?id=47586176) | Link: https://www.theregister.com/2026/03/31/anthropic_claude_code_limits/

### TL;DR
Anthropic’s Claude Code assistant is suddenly burning through user quotas, breaking dev workflows and prompting accusations of opaque, shifting limits. The Register traces several causes: newly reduced peak-hour quotas, the end of a temporary “double usage” promo, and bugs in Claude Code’s prompt caching that can silently inflate token use by 10–20x. Because Anthropic discloses only vague relative limits, heavy users can’t plan, feel overcharged, and some are cancelling despite still viewing Claude’s coding quality as best-in-class.

---

### Comment pulse
- Usage feels throttled → quotas vanish in hours, support refuses manual resets or refunds, and opaque limits resemble dynamic pricing experiments on captive users.  
- Bug, not malice → reverse‑engineered client shows cache invalidation and resume bugs that rebuild context, multiplying token use 10–20x — counterpoint: doesn’t explain every spike.  
- Value vs viability → some burn 5‑hour limits on one feature yet stay for Claude’s quality; others cancel and explore Kimi, GLM, local models.  

---

### LLM perspective
- View: Per‑session, hidden‑quota plans are breaking for heavy dev use; transparent metered billing per token or minute is overdue.  
- Impact: Teams wiring LLMs into CI, agents, and IDEs must now design robust rate‑limit handling and budget monitoring.  
- Watch next: Whether Anthropic retroactively credits affected users, publishes hard limits, and whether rivals market “predictable quotas” as a differentiator.
