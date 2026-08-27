# Flowistry: An IDE plugin for Rust that focuses on relevant code

- Score: 155 | [HN](https://news.ycombinator.com/item?id=45627692) | Link: https://github.com/willcrichton/flowistry

### TL;DR

Flowistry is a VS Code plugin that uses Rust information-flow analysis to fade code unrelated to the expression under the cursor, effectively providing interactive program slicing. It works from compiler MIR and ownership information, but is limited to Rust 1.73, may take seconds on large functions, cannot fully model interior mutability, and analyzes nested functions separately. Commenters saw value for navigating daunting functions and studying borrow relationships, while noting those limitations matter for patterns involving RefCell, aliases, closures, and async code.

### Comment pulse

- Rust ownership makes dependable slicing unusually feasible → dynamic languages cannot offer the same static guarantees.
- Back-reference research might benefit from Flowistry’s analysis → incomplete interior-mutability handling is precisely the difficult case.
- This exceeds ordinary symbol highlighting → rust-analyzer lacks the MIR and borrow-checker data Flowistry requires.

### LLM perspective

- View: Flowistry turns compiler semantics into a reading aid, demonstrating value beyond diagnostics and optimization.
- Impact: Maintainers can prune irrelevant paths when understanding large functions, with explicit soundness caveats.
- Watch next: Track support for newer Rust, closures, async boundaries, and alias-aware interior mutability.
