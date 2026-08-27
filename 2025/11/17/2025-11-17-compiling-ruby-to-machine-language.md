# Compiling Ruby to machine language

- Score: 148 | [HN](https://news.ycombinator.com/item?id=45957629) | Link: https://patshaughnessy.net/2025/11/17/compiling-ruby-to-machine-language

### TL;DR

An excerpt from a forthcoming Ruby internals book explains how YJIT detects hot Ruby code and translates YARV instructions into native machine instructions. Each function or Ruby block accumulates calls; after a threshold, YJIT compiles smaller basic blocks rather than the whole function. Branch stubs defer type-specific work until runtime values appear, allowing separate optimized versions for observed operand types. An ARM64 example maps local-variable loads to registers. The larger chapter will contrast this basic-block-versioning design with the developing ZJIT approach, so this excerpt intentionally stops mid-explanation.

### Comment pulse

- Readers connected the work to earlier native Ruby projects and asked how compiled versions handle changing runtime types.
- The author explained that YJIT waits for observed types and retains separate block versions selected as needed.

### LLM perspective

- View: YJIT’s strength is specializing from observed execution without pretending Ruby’s dynamic types disappeared.
- Impact: Fine-grained compilation avoids spending work on cold paths and permits multiple optimized type histories.
- Watch next: Guard failures, version limits, recompilation costs, and how ZJIT’s method-level strategy differs.
