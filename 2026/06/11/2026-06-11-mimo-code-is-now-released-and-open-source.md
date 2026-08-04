# MiMo Code is now released and open-source

- Score: 553 | [HN](https://news.ycombinator.com/item?id=48490826) | Link: https://mimo.xiaomi.com/mimocode

### TL;DR

Xiaomi’s MiMoCode is a terminal-native coding agent built on OpenCode, with MIT-licensed source and separate use restrictions. It supports mainstream and custom LLM providers, code and Git operations, persistent SQLite-backed memory, context reconstruction, task trees, parallel subagents, judge-enforced goals, reusable skills, and deterministic multi-agent workflows. MiMo Auto offers zero-configuration access temporarily, while users can bring other credentials. HN welcomed an inspectable, portable harness that reduces switching costs, but questioned how much is new versus bundled extensions and warned that uneven model capabilities make tokens non-interchangeable.

### Comment pulse

- Open harnesses reduce lock-in → inspectable context handling and broad provider support let users migrate without replacing their entire workflow.
- Derivative value is contested → counterpoint: critics see familiar plugins, while persistent memory, orchestration, and fixed workflows extend upstream OpenCode.
- Models remain non-fungible → portability helps solved tasks, but frontier performance varies enough to require continuous task-specific evaluation.

### LLM perspective

- **View:** Checkpoints, goals, and deterministic phases turn a chat loop into durable execution rather than merely adding commands.
- **Impact:** Teams can standardize one agent interface across providers while keeping project memory and custom workflows locally inspectable.
- **Watch next:** Benchmark completion quality, context-recovery fidelity, workflow resume behavior, and upstream divergence under identical repositories and models.
