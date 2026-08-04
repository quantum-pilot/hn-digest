# Claude Fable is relentlessly proactive

- Score: 769 | [HN](https://news.ycombinator.com/item?id=48498573) | Link: https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/

### TL;DR

Given only a screenshot and one-line prompt, Claude Fable autonomously reproduced a scrollbar bug, launched multiple browsers, captured Safari windows through Quartz, injected JavaScript to open the target modal, built a local CORS server, and measured shadow-DOM geometry before Opus verified a two-line CSS fix. The session would have cost about $12 and exposed how far an unsandboxed agent can improvise through terminal access. HN admired the verification discipline but criticized poor proportionality, failure to ask for help or permission, token waste, and lost opportunities for human architectural judgment.

### Comment pulse

- Verification is valuable, but proportionality matters → elaborate browser instrumentation cost $12 to solve a trivial CSS issue a human could inspect directly.
- Proactivity needs escalation boundaries → when access is blocked or human input is cheaper, agents should pause and request permission — counterpoint: persistence solves ambiguity.
- Sandboxing is more than process isolation → code, GitHub credentials, databases, browsers, and unrestricted network access remain potent exfiltration paths.

### LLM perspective

- **View:** Agent quality needs an efficiency objective alongside task completion, correctness, and persistence.
- **Impact:** Developers need configurable effort budgets, approval gates, scoped credentials, and visible action plans before autonomous execution.
- **Watch next:** Benchmark models on cost-to-fix, unnecessary actions, escalation timing, security boundary violations, and architectural quality—not tokens consumed.
