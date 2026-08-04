# Claude Code as a Daily Driver: Claude.md, Skills, Subagents, Plugins, and MCPs

- Score: 348 | [HN](https://news.ycombinator.com/item?id=48289950) | Link: https://arps18.github.io/posts/claude-code-mastery/

### TL;DR

The guide argues that Claude Code becomes useful when operated as a configurable agent rather than a chat prompt: plan before multi-file work, provide deterministic verification, keep `CLAUDE.md` short and mistake-driven, encode repeated workflows as skills, isolate reviews in subagents, and limit MCP servers. It recommends fresh-context reviewers and parallel worktrees while requiring tests or screenshots before success. HN readers challenged the overlapping abstractions, resource-heavy LSP advice, vendor specificity, and repetitive prose; practitioners still reported meaningful gains with strong project instructions and human review.

### Comment pulse

- Commands, skills, subagents, and plugins overlap as canned-prompt delivery mechanisms → Claude Code’s team says review workflows will consolidate into one built-in skill.
- LSP plugins may consume substantial memory without agent use → counterpoint: automatic diagnostics, not explicit tool calls, may be their intended value.
- Experienced users report large gains on tedious work but retain 3–4 human-feedback rounds → autonomy remains limited despite better instruction files.

### LLM perspective

- **View:** The durable pattern is not any named feature; it is externalizing context, constraints, feedback loops, and independent review.
- **Impact:** Teams gain consistency and parallelism, but configuration sprawl and platform-specific conventions create maintenance and lock-in costs.
- **Watch next:** Abstraction consolidation, measured LSP usage, portability across agents, and defect rates before versus after accumulated project rules.
