# Superpowers: How I'm using coding agents in October 2025

- Score: 335 | [HN](https://news.ycombinator.com/item?id=45547344) | Link: https://blog.fsck.com/2025/10/09/superpowers/

- TL;DR
  - Jesse’s “Superpowers” outlines orchestrating Claude-based coding agents via modular skills, subagents, and usage rules, auto-installing abilities as plugins. HN finds it ambitious but questions whether skills beat custom commands/sub-agents or Research→Plan→Implement on large codebases. Commenters ask for concrete, measured productivity wins, not anecdotes. Prompt dramatization is called outdated; clear instructions suffice. Minor nits target filesystem hygiene. A debugging anecdote highlights failure modes (agents “gameshow” quizzing) and argues for realistic simulations and evaluation.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - Skills-based agents beat classic flows? → Ambitious, composable “skills” praised; others prefer R→P→I or custom commands for large codebases — counterpoint: skills broaden abilities.
  - We’re still tinkering → Few repeatable workflow wins; calls for head-to-head metrics: PR throughput, bug rate, latency, and large-repo correctness.
  - Prompt theatrics are obsolete → Emotional framing and ALL-CAPS add little; clear instructions and evaluation harnesses matter more; cited persuasion research was misapplied.

- LLM perspective
  - View: Prioritize structured skills, permissions, and tests over roleplay; measure deltas on real repos, not toy tasks.
  - Impact: If reliable, agents shift dev time to review and integration; infra must support traceability, rollback, and policy-guarded execution.
  - Watch next: Open benchmarks on multi-module codebases; ablations: skills vs commands vs R→P→I; filesystem/XDG compliance; realistic simulations catching game-show behaviors.
