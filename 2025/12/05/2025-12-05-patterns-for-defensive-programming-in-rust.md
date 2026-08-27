# Patterns for Defensive Programming in Rust

- Score: 181 | [HN](https://news.ycombinator.com/item?id=46163609) | Link: https://corrode.dev/blog/defensive-programming/

### TL;DR

Rust's memory safety does not prevent business-logic errors, so the article recommends patterns that make invalid states and future changes harder to miss. Examples include slice patterns instead of indexing, exhaustive destructuring and matching, `TryFrom` for fallible conversions, scoped temporary mutability, private fields and constructors for invariants, `#[must_use]`, and enums instead of boolean parameters. Many practices deliberately turn later schema changes into compiler or Clippy failures. Commenters also warned that stronger types should reflect the domain rather than create needless machinery.

### Comment pulse

- One commenter preferred separating pizza details from orders instead of inventing partial equality semantics.
- Discussion highlighted exhaustive enum handling and Clippy as useful guardrails for human- and agent-written code.

### LLM perspective

- View: Defensive Rust works best when compiler failures mark broken assumptions, not merely stylistic preferences.
- Impact: Explicit invariants shift some review burden from runtime behavior to compile-time feedback.
- Watch next: Whether these patterns simplify domain models or accumulate abstractions that obscure them.
