# Schedule tasks on the web

- Score: 281 | [HN](https://news.ycombinator.com/item?id=47539188) | Link: https://code.claude.com/docs/en/web-scheduled-tasks

### TL;DR

Claude Code now runs recurring prompts on Anthropic-managed infrastructure even when a user’s computer is off. Cloud schedules support hourly, daily, weekday, weekly, and CLI-customized cadences; each run freshly clones selected GitHub repositories, defaults pushes to `claude/` branches, uses a chosen environment, and creates a reviewable session. Network access, secrets, setup scripts, models, and connectors are configurable, though every existing connector is included by default unless removed. HN saw promise for reviews, CI triage, and stakeholder-driven updates, but warned that nondeterministic agents compound errors and often replace simpler cron jobs.

### Comment pulse

- Fully agentic feedback-to-deployment loops promise speed — counterpoint: each stage can multiply mistakes until no human retains a reliable system model.
- Conditional alerts need explicit definitions, tools, and evaluations; vague prompts often notify on both positive and negative cases.
- Natural-language scheduling lowers automation barriers, but deterministic rules remain cheaper and more reliable whenever the condition is formalizable.

### LLM perspective

- **View:** Scheduling solves persistence and orchestration, not judgment; reliable tasks require narrow scope, explicit criteria, and idempotent actions.
- **Impact:** Teams automate maintenance without always-on machines, while connector and secret exposure becomes a recurring unattended risk.
- **Watch next:** Run pricing, quotas, failure notifications, connector least privilege, concurrency controls, eval support, and audit retention.
