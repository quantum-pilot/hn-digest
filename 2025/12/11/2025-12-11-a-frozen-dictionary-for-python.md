# A “frozen” dictionary for Python

- Score: 180 | [HN](https://news.ycombinator.com/item?id=46229467) | Link: https://lwn.net/SubscriberLink/1047238/25c270b077849dc0/

## TL;DR
Python is considering adding a truly immutable dictionary (“frozendict”) type, mainly to make code and concurrency easier to reason about: callers could rely on mappings that cannot be mutated after construction. HN commenters compare this to languages like Rust that encode mutability in the type system, debate whether a blanket freeze is too blunt versus proper persistent data structures, and note that ad‑hoc alternatives (MappingProxyType, custom libraries like pyrsistent) already exist but lack a standard, ergonomic solution.

*Content unavailable; summarizing from title/comments.*

---

## Comment pulse
- Culture shift toward immutability → 2006 views dismissed frozen dicts as niche; today, concurrency and reasoning about state make them attractive, especially for API contracts.
- Frozendict seen as crude → it forces all‑or‑nothing immutability, likely driving copying; pyrsistent offers structural sharing and richer persistent collections — counterpoint: structural sharing avoids most deep copies anyway.
- Existing tools partly fill the gap → MappingProxyType, Mapping hints, and pyrsistent work now, but either allow backdoors to mutation or are third‑party, not standard and universal.

---

## LLM perspective
- View: A built‑in frozendict formalizes a common pattern, but doesn’t address mutability at the type-system level like Rust or Kotlin.
- Impact: Library authors gain stronger invariants for configs, defaults, and cache keys; concurrent and async code becomes easier to reason about.
- Watch next: How frozendict integrates with typing, pattern matching, and existing libs like pyrsistent, and whether persistent variants reach the standard library.
