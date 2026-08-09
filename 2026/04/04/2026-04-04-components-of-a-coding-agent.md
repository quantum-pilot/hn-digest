# Components of a Coding Agent

- Score: 149 | [HN](https://news.ycombinator.com/item?id=47638810) | Link: https://magazine.sebastianraschka.com/p/components-of-a-coding-agent

### TL;DR

A coding agent is not just an LLM but a control loop inside a harness that gathers repository context, builds cache-friendly prompts, exposes validated tools and permissions, clips or summarizes expanding context, persists transcripts and working memory, and delegates bounded subtasks. Sebastian Raschka argues this surrounding system can explain much of the gap between plain chat and products such as Codex or Claude Code, though open-model parity is speculative. Commenters favored durable specifications as the source of truth and disputed whether production harnesses remain simple once reliability features accumulate.

### Comment pulse

- Chat history is a fragile project record → spec-first workflows preserve intent, expose contradictions, and give generation bounded inputs.
- Aggressive truncation controls cost and noise → rehydratable tool outputs can preserve detail when later needed.
- Minimal loops clarify the architecture → production safety, state, and interface layers can grow into substantial complexity.

### LLM perspective

- **View:** Harness quality is chiefly information architecture: selecting the right state, affordances, and constraints for each decision.
- **Impact:** Teams can improve agent reliability without changing models by strengthening context, validation, memory, and task boundaries.
- **Watch next:** Harness-controlled model comparisons, spec-first benchmarks, resumability failures, cache economics, and subagent conflict rates.
