# Maximizing the value of your Claude Code sessions

- Score: 192 | [HN](https://news.ycombinator.com/item?id=49300800) | Link: https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions

### TL;DR

The guide explains Claude Code session cost through model price, fresh input, cached history, and output, with output roughly five times input and cache reads one-tenth of input. Because every file and command result stays in context and is resent each turn, long or noisy sessions waste money and attention. It recommends choosing model and effort before starting, clearing between tasks, attaching relevant files, quieting commands, inspecting startup context, isolating noisy work in subagents, and compacting before cache expiration. Commenters prefer portable handoff files and question the optimization burden.

### Comment pulse

- Portable handoff documents preserve project memory across fresh sessions and even different agent systems, often outperforming opaque compaction.
- File mentions save discovery calls—counterpoint: large or changing files may waste context, and desktop search reportedly differs from the CLI.

### LLM perspective

- View: Token efficiency and reasoning quality align when context contains only durable, task-relevant evidence; cache mechanics make that discipline cheaper.
- Impact: Developers must manage session boundaries like build artifacts, trading workflow structure for lower cost and less context pollution.
- Watch next: Measure handoff versus compact, large-file mentions, desktop parity, cache expiry, and task outcomes—not tokens alone.
