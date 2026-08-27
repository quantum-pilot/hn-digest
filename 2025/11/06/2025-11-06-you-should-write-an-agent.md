# You should write an agent

- Score: 175 | [HN](https://news.ycombinator.com/item?id=45840088) | Link: https://fly.io/blog/everyone-write-an-agent/

### TL;DR

Thomas Ptacek argues that developers should build a small LLM agent before judging the technology because the core is only a stateless model call, a replayed context, and a loop that executes requested tools. His Python example grows from terminal chat into an agent choosing several ping targets without an explicit workflow. He argues custom agents make context limits, tool isolation, subagents, cost, nondeterminism, and verification concrete programming problems, while MCP is mainly useful for extending software developers do not control. Commenters largely shared positive experiments.

### Comment pulse

- Commenters described early agents built with minimal code and likened LLM calls to composable Unix text-processing tools.
- Tool granularity prompted debate: tiny deterministic commands aid security, but too many descriptions consume context and complicate selection.

### LLM perspective

- View: The tutorial’s strongest claim is pedagogical: a minimal loop exposes where agent behavior actually comes from.
- Impact: Building one can replace product mythology with inspectable tradeoffs in tools, state, cost, and verification.
- Watch next: Ground-truth checks, permission boundaries, context compression, tool granularity, and reproducible comparisons between agent designs.
