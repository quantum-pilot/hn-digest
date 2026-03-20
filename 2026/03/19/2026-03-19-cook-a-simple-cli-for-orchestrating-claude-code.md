# Cook: A simple CLI for orchestrating Claude Code

- Score: 284 | [HN](https://news.ycombinator.com/item?id=47434024) | Link: https://rjcorwin.github.io/cook/

### TL;DR
Cook is a small CLI and Claude Code skill that lets you orchestrate multi-step AI coding workflows using a tiny shell-like DSL. Instead of hand-coding Python/bash wrappers or repeatedly prompting Claude, you compose “work” units with loop operators (repeat, review loops, task-list progression via “ralph”) and composition operators (parallel versions, A/B “vs”, pick/merge/compare). It manages git worktrees, sandboxing, and rate-limit retries. HN discussion centers on how this differs from raw Claude CLI and similar orchestration tools.

---

### Comment pulse
- DIY scripts vs cook → Many already glue Claude via Python/subprocess; cook formalizes common loops so you don’t keep re-specifying workflows — counterpoint: simple bash could approximate this.
- What it adds over Claude CLI → Focus on coordinating multiple agents and repeatable multi-step flows; raw CLI shines for one-off, interactive sessions.
- Ecosystem and features → Similar tools (getcook.dev, ralphmania, ossature) exist; questions on merge/validation, receipts, and enthusiasm for auto-continue after rate limits.

---

### LLM perspective
- View: This is a domain-specific orchestrator, turning common “agent patterns” into reusable, composable commands instead of bespoke scripts.
- Impact: Most helpful for teams running many iterative code changes, reviews, and experiments across models and sandboxes.
- Watch next: Benchmarks vs DIY scripts, better conflict-resolution strategies, and standardized specs for multi-agent workflows across tools.
