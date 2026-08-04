# The new rules of context engineering for Claude 5 generation models

- Score: 121 | [HN](https://news.ycombinator.com/item?id=49051361) | Link: https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models

### TL;DR

Anthropic says Claude 5-class models need less scaffolding: deleting over 80% of Claude Code’s system prompt caused no measurable loss on its coding evaluations. The recommended shift is from rigid rules, examples, repetition, and all-upfront context toward model judgment, expressive tool interfaces, progressive disclosure, auto-memory, and rich code or artifact references. Keep CLAUDE.md lightweight and focused on repository-specific gotchas. Hacker News partly welcomed simpler prompting, but users reported regressions, opaque memory behavior, higher verbosity, accidental edits, and concerns that Anthropic-specific tooling increases lock-in.

### Comment pulse

- Simple collaboration can beat elaborate harnessing → human-in-the-loop users prefer brief conversation and small manual fixes over endlessly tuning prohibitions.
- Reported behavior contradicts the evaluation headline → users cited deletions, ignored hooks, longer outputs, repeated mistakes, and fixation on sandbox limits.
- Auto-memory trades control for convenience → it can surface helpful history — counterpoint: hidden, weakly configurable assumptions make decisions difficult to audit.

### LLM perspective

- **View:** Context minimization should be treated as model-specific optimization, not a universal migration rule.
- **Impact:** Teams must rebalance instruction maintenance against supervision costs; autonomous workflows carry more downside than pair-programming sessions.
- **Watch next:** Publish ablations across real repositories, tool violations, destructive actions, token consumption, and comparable Claude 4.8 baselines.
