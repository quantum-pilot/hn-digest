# A couple million lines of Haskell: Production engineering at Mercury

- Score: 401 | [HN](https://news.ycombinator.com/item?id=47991802) | Link: https://blog.haskell.org/a-couple-million-lines-of-haskell/

### TL;DR
Mercury, a fintech processing hundreds of billions of dollars, runs ~2M lines of Haskell written largely by generalist engineers trained in-house. They treat Haskell’s type system less as a correctness proof and more as an operational tool: encode institutional knowledge and dangerous invariants in types, so the “right” behavior is the only behavior APIs allow. They balance this with restraint (not every rule goes in types), strong observability and introspection hooks, and durable execution via Temporal to keep long-running workflows robust under failures.

---

### Comment pulse
- Encoding invariants in types → Works across many languages (Rust, TS, OCaml, even dynamic with wrappers); Haskell just makes it most ergonomic. — counterpoint: TS’s structural types make this clumsy.
- Haskell vs Rust productivity → Some engineers feel 2x faster in Rust due to Haskell’s pitfalls/tooling; others report the opposite, citing Rust refactors and higher‑order functions as painful.
- Haskell’s role at Mercury → Many see language choice plus culture as a real advantage; others argue execution and fintech focus matter more than FP purity.

---

### LLM perspective
- View: This is a blueprint for “pragmatic FP”: purity as boundaries, types for critical invariants, everything else judged by operational value.
- Impact: Most relevant to teams running high-risk, high-integrity backends (fintech, healthcare, infra) where refactors and correctness are expensive.
- Watch next: More libraries adopting observability hooks and “records of functions,” plus stronger Temporal-like durable-execution stories across ecosystems.
