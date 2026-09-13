# Stabilizing Rust's Never Type

- Score: 197 | [HN](https://news.ycombinator.com/item?id=49625056) | Link: https://lwn.net/SubscriberLink/1091015/d9e48318ed242b41/

### TL;DR

Rust 1.99 will stabilize `!`, the never type for computations that cannot produce a value, and alias `Infallible` to it. Because `!` coerces into other types, it simplifies generic APIs and inference around divergent code. Stabilization also changes fallback behavior, potentially breaking ambiguous calls that previously inferred unit. Crater testing initially found 3,300 affected crates but only seven directly broken; backports reduced dependency fallout. Commenters favor the pragmatic compatibility tradeoff, discuss syntax readability, and correct the article’s claims about `Infallible` optimization and grammar.

### Comment pulse

- Rare breakage is acceptable → warnings, crater testing, backports, and straightforward annotations make the language simplification proportionate.
- `Infallible` was already optimized → commenters say compiler recognition of uninhabited user types, not dead-code removal, distinguished the gap.
- The `!` syntax divides readers → historical continuity supports it, while `Never` could communicate intent more clearly.

### LLM perspective

- View: The rollout demonstrates compatibility as managed risk rather than an absolute prohibition on correcting long-planned type behavior.
- Impact: Generic APIs can express impossible branches directly, while a small set of ambiguous calls will require explicit types.
- Watch next: Monitor Rust 1.99 regressions, ecosystem patch adoption, diagnostics quality, and whether a readable alias becomes conventional.
