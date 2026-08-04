# Elixir v1.20: Now a gradually typed language

- Score: 474 | [HN](https://news.ycombinator.com/item?id=48388324) | Link: https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/

### TL;DR

Elixir 1.20’s compiler now infers set-theoretic types for every program without annotations, using unions, intersections, negations, guards, pattern matches, and control flow to report dead code and only type errors guaranteed to crash if executed. Its `dynamic()` type preserves a range of possible values and narrows through use, rather than discarding information like a permissive `any`. The implementation passes 12 of 13 type-narrowing benchmark categories. HN welcomed the migration-free rollout but tested its claims against Dialyzer, runtime overhead, and earlier retrofitted type systems.

### Comment pulse

- No runtime asymptotic penalty → sound static–dynamic boundaries avoid inserted casts, leaving emitted bytecode semantically identical to untyped execution.
- Dialyzer is the adoption benchmark → veterans want evidence that verified-bug inference catches more useful defects than success typing.
- Retrofitting need not feel bolted-on → pattern matching, guards, and existing specs already make Elixir programs type-conscious.

### LLM perspective

- **View:** Trust depends less on annotation expressiveness than whether early warnings stay rare, actionable, and provably correct.
- **Impact:** Existing Elixir projects gain compiler diagnostics immediately, letting teams evaluate typing before changing public APIs.
- **Watch next:** Compile-time regressions, real-codebase bug yield, recursive and parametric types, typed structs, then function signatures.
