# Just talk to it – A way of agentic engineering

- Score: 167 | [HN](https://news.ycombinator.com/item?id=45588689) | Link: https://steipete.me/posts/just-talk-to-it

- TL;DR
  - Peter Steinberger outlines a “just talk to it” setup: GPT-5 Codex CLI, 3–8 parallel agents, atomic commits, minimal harnessing, and tight control of change “blast radius.” He prefers subscriptions (~$1k/month) over APIs, uses screenshots, queues tasks, tmux for long jobs, frequent refactors, and tests after each feature. He dismisses subagents/MCPs/RAG as overhead and notes Codex quirks. HN splits: critics see slop, cost, and limited autonomy; defenders cite his track record; others say AI fits CRUD, not compiler-like work.

- Comment pulse
  - Slop/bloat and $1k/month to herd agents → maintainability risk, fragile skills — counterpoint: Author’s pedigree (PDFKit) suggests he can steward AI-written code.
  - Good for CRUD/integrations; fails on compilers/optimizers → needs holistic design, performance tradeoffs; agents prefer maximal diffs over minimal fixes.
  - Most can’t reach 50% AI-written; require line-by-line reviews → unwanted behavior changes, regressions; “incantations” feel charade; waiting for stable workflows.

- LLM perspective
  - View: Lightweight, conversation-first orchestration beats heavy harnesses; results depend on developer intuition and tight feedback loops.
  - Impact: If viable, solo devs can ship faster, but quality drifts without strict tests, refactor budgets, and controlled “blast radius.”
  - Watch next: Independent benchmarks on code churn/defects, reproducible workflow streams, background-task support in codex, and policy on subscription “unlimited tokens.”
