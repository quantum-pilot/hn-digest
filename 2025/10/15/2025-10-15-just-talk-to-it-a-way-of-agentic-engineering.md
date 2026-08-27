# Just talk to it – A way of agentic engineering

- Score: 167 | [HN](https://news.ycombinator.com/item?id=45588689) | Link: https://steipete.me/posts/just-talk-to-it

### TL;DR

Peter Steinberger says GPT-5 Codex now writes nearly all code for his 300,000-line solo project. He runs three to eight agents concurrently in one working tree, scopes tasks by “blast radius,” lets agents make atomic commits, interrupts them for status, iterates through conversation and screenshots, and spends about 20% of time on agent-led refactoring. He favors direct dialogue over elaborate harnesses, plugins, MCPs, worktrees, and rigid specs. HN readers questioned code quality, transferability, $1,000 monthly tooling costs, and absent line-by-line review.

### Comment pulse

- Shallow integrations and established patterns suit agents → parsers, performance-sensitive systems, and novel semantics require deeper oversight.
- Parallel agents increase throughput → shared-tree complexity and accumulated generated code can magnify hidden mistakes.
- The workflow rejects elaborate rituals yet uses extensive instructions and multiple subscriptions → critics saw contradiction rather than simplicity.

### LLM perspective

- View: This is an expert operator’s high-throughput personal workflow, not general evidence that autonomous coding is solved.
- Impact: Engineering shifts toward decomposition, supervision, testing, and debt management when generation becomes cheap.
- Watch next: Publish code, defect history, maintenance effort, human review depth, and comparable non-agent baselines.
