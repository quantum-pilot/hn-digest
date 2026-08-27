# Gemini CLI Tips and Tricks for Agentic Coding

- Score: 162 | [HN](https://news.ycombinator.com/item?id=46060508) | Link: https://github.com/addyosmani/gemini-cli-tips

### TL;DR

Addy Osmani’s power-user guide presents Gemini CLI as an open-source terminal agent that can inspect context, run commands, edit files, and execute multi-step plans. Its most reusable practices are hierarchical GEMINI.md instructions, custom slash commands, explicit file context, checkpoints, saved sessions, constrained tool access, and MCP integrations. The guide warns that YOLO mode removes modification confirmations. Commenters report sharply mixed reliability, quota, and billing experiences, and note the author’s Google affiliation, so the piece is guidance rather than an independent benchmark.

### Comment pulse

- Persistent context and reusable commands can standardize workflows → checkpoints provide a recovery path when edits go wrong.
- User experiences range from fast and reliable to error-prone → account limits and billing opacity complicate comparison.

### LLM perspective

- View: Repeatable context and reversible execution matter more than any single agent’s feature count.
- Impact: Teams can codify repository conventions while preserving review gates around shell and file mutations.
- Watch next: Version-specific reliability tests, quota transparency, and reproducible comparisons against competing coding agents.
