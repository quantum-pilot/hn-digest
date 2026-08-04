# Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k

- Score: 426 | [HN](https://news.ycombinator.com/item?id=48883275) | Link: https://systima.ai/blog/claude-code-vs-opencode-token-overhead

### TL;DR

A logging-proxy benchmark found Claude Code’s first request carried about 33,000 tokens of instructions, tool schemas, and scaffolding before a prompt, versus roughly 7,000 for OpenCode on the same model. Instruction files, MCP schemas, unstable cache prefixes, and especially subagents multiplied costs; two subagents raised one task from 121,000 to 513,000 tokens. Claude sometimes recovered through tool batching, but results varied by model. Both passed simple quality tests, leaving harder-task value unresolved. HN emphasized limiting fan-out and measuring completed-work quality, round trips, and cache stability—not prompt size alone.

### Comment pulse

- Subagents are the dominant multiplier → each replays a bootstrap and reacquires context — counterpoint: parallel exploration can justify the expense when exhaustive discovery matters.
- Large prompts are not automatically inefficient → aggressive batching can beat lean serial loops, so request count and tool design determine whole-task cost.
- Prompt size is only the floor → quality, tool reliability, and completed-work efficiency matter; simple benchmarks cannot price orchestration benefits on harder engineering.

### LLM perspective

- **View:** Agent efficiency multiplies baseline size, request count, parallel sessions, and cache misses; conversation growth compounds every turn.
- **Impact:** Hidden harness overhead consumes context as well as money, causing earlier compaction and reducing capacity for repository-specific evidence.
- **Watch next:** Independent reproductions, harder quality-controlled tasks, prefix stability, model-conditioned prompts, adaptive tool selection, and explicit budgets for subagent fan-out.
