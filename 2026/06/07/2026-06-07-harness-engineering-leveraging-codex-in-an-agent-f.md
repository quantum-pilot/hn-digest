# Harness engineering: Leveraging Codex in an agent-first world

- Score: 280 | [HN](https://news.ycombinator.com/item?id=48416264) | Link: https://openai.com/index/harness-engineering/

## TL;DR
OpenAI built an internal product whose ~million-line codebase was written entirely by Codex agents; humans focused on architecture, docs, and feedback loops instead of typing code. The repo is the single system of record, with strict layered architecture enforced by custom linters and rich in-repo plans/specs. Agents can spin up per-branch environments, inspect UI and observability data, and now often debug, fix, and merge features autonomously. HN readers are intrigued but question LOC-heavy productivity claims, quality, and long-term maintainability.

## Comment pulse
- AI-driven throughput metrics excite management → commenters distrust LOC/PR counts, see code bloat and scant evidence of proportionally better products—counterpoint: release cadence does feel faster.  
- Several engineers mirror this setup → keep docs/plans in-repo, give agents observability and tests; report promising results but hit cost, CI, and autonomy limits.  
- Reviewing AI PRs feels like vape-factory sampling → analogy fails, say others; a single bad PR can be catastrophic unless impact is bounded by tests.

## LLM perspective
- View: Treating the repo as an agent-readable operating manual shifts engineering from code authorship to environment and constraint design.  
- Impact: If generalizable, this favors teams strong in architecture, tooling, and documentation over raw individual coding speed.  
- Watch next: Open-sourced harnesses, long-term coherence metrics for agent-built systems, and comparative studies of defect rates versus human-written code.
