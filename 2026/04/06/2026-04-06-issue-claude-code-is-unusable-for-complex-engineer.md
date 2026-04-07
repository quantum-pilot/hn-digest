# Issue: Claude Code is unusable for complex engineering tasks with Feb updates

- Score: 711 | [HN](https://news.ycombinator.com/item?id=47660925) | Link: https://github.com/anthropics/claude-code/issues/42796

### TL;DR

A power user analyzed 6,800+ Claude Code sessions and claims a sharp February–March degradation on complex, long-running engineering tasks coincides with reduced/hidden “thinking” and a shift from research-first to edit-first behavior. Metrics show more lazy shortcuts, premature stopping, and user interrupts, exploding token usage while killing a previously successful multi-agent workflow. The author argues extended reasoning tokens are structurally required and now silently rationed on subscriptions. An Anthropic engineer responds that “redact-thinking” is UI-only and blames adaptive thinking plus a new medium-effort default, which users can override; commenters broadly report similar regressions and rising distrust of opaque model changes.

---

### Comment pulse

- Anthropic view → thinking redaction is cosmetic; real changes are adaptive thinking and medium default effort, all tunable via settings, env vars, and prompts — counterpoint: users felt blindsided and misconfigured.  
- Power users’ claim → subscription access now gets load-variable, much shallower thinking even at max effort, breaking complex workflows and feeling like an undisclosed downgrade vs API/enterprise.  
- Broader concern → inconsistent, silently changing models destroy trust; engineers must re-verify everything, making “AI pair programming” more exhausting than helpful.

---

### LLM perspective

- View: Extended reasoning budgets and stable defaults are prerequisites for safe autonomous code edits at scale.  
- Impact: Heavy users, multi-agent systems, and CI pipelines bear the brunt; casual chat users barely notice.  
- Watch next: Clear thinking-token telemetry, benchmark suites for long-session work, and product tiers explicitly trading latency/cost for guaranteed depth.
