# Elixir v1.20: Now a gradually typed language

- Score: 474 | [HN](https://news.ycombinator.com/item?id=48388324) | Link: https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/

- TL;DR  
Elixir 1.20 ships a research-grade, set-theoretic gradual type system that infers types for all code without annotations and without runtime overhead. It introduces a `dynamic()` type that narrows as values are used, only flagging “verified bugs” that would definitely crash, greatly reducing false positives. Guards, pattern matching, and clauses now feed precise inference, while compilation gets faster. HN discussion focuses on typed vs untyped tradeoffs, Dialyzer comparisons, performance guarantees, and retrofitting types into dynamic languages.

- Comment pulse  
  - Dynamic languages seen as tech debt → Rails-era companies shifted to typed stacks for scaling and safety — counterpoint: success depends on teams and tooling.  
  - Elixir devs welcome built-in typing → hope it’s more actionable than Dialyzer’s success typing, which often missed real issues or felt low-value.  
  - Researchers clarify asymptotics → new system avoids runtime casts at static/dynamic boundaries, matching untyped bytecode semantics and countering fears about “bolted-on” types.

- LLM perspective  
  - View: Inferred gradual types plus low false positives fit Elixir’s fault-tolerant ethos better than aggressive, annotation-heavy static typing.  
  - Impact: Editors and AI assistants can use compiler types for safer completions, refactors, and bug localization in growing Elixir services.  
  - Watch next: How recursive/parametric types and typed structs land will decide Elixir’s appeal versus OCaml, Haskell, or Rust backends.
