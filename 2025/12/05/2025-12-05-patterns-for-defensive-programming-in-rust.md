# Patterns for Defensive Programming in Rust

- Score: 181 | [HN](https://news.ycombinator.com/item?id=46163609) | Link: https://corrode.dev/blog/defensive-programming/

### TL;DR

The guide turns implicit Rust assumptions into compiler-enforced guarantees. It recommends slice matching instead of panic-prone indexing, explicit struct fields instead of broad defaults, exhaustive enum matches, and TryFrom for fallible conversion. Destructuring can force trait implementations to reconsider newly added fields; narrow scopes limit mutability; private seals and constructors protect validated states; must_use catches ignored values. Enums or parameter structs replace ambiguous booleans, while Clippy can deny risky patterns automatically. The author reserves stronger constructor defenses for evolving libraries, where future refactors justify added complexity.

### Comment pulse

- Readers endorsed avoiding indexing after real out-of-bounds bugs and saw compiler or Clippy feedback as useful guardrails for generated code.
- The pizza equality example drew criticism: separating comparable details from order identity was clearer than custom equality that ignores timestamps.
- Enums were preferred over boolean wrappers because named variants clarify calls and can expose methods expressing domain-specific predicates.

### LLM perspective

- View: The best patterns make invalid evolution fail compilation, but defensive structure should remain proportional to an API’s change risk.
- Impact: Library maintainers gain safer refactors; application teams may incur needless ceremony if every invariant receives maximum sealing.
- Watch next: Clippy adoption, panic reduction and maintenance outcomes comparing exhaustive designs with simpler idiomatic code.
