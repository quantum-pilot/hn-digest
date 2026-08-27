# Rust--: Rust without the borrow checker

- Score: 115 | [HN](https://news.ycombinator.com/item?id=46453062) | Link: https://github.com/buyukakyuz/rustmm

### TL;DR

Rust-- is a forked Rust compiler that disables borrow checking, allowing examples such as use-after-move, overlapping mutable references, and conflicting mutable and immutable borrows to compile. Prebuilt binaries and deliberately invalid examples frame it as an experiment rather than a safety-preserving Rust variant. HN largely treated the project as educational or humorous, while emphasizing that rejected programs may trigger undefined behavior because generated code can rely on Rust’s aliasing and ownership rules. The checker’s absence removes diagnostics, not the language’s semantic obligations.

### Comment pulse

- Ownership discipline transfers beyond Rust → explicit cloning and mutation boundaries can prevent distant side effects.
- Disabling checks does not legalize invalid code → aliasing assumptions may still enable unsafe compiler optimizations.
- Borrow-checker friction often declines with experience → lifetimes remain the harder conceptual input for some learners.

### LLM perspective

- View: Rust-- is a revealing negative-space demonstration of what borrow checking guarantees, not a practical escape hatch.
- Impact: Learners can distinguish conservative compile-time rejection from actual undefined behavior by testing counterexamples.
- Watch next: Examine emitted LLVM alias metadata and sanitizer or Miri results for the repository’s showcased programs.
