# The C3 Programming Language

- Score: 264 | [HN](https://news.ycombinator.com/item?id=46478647) | Link: https://c3-lang.org

### TL;DR
C3 is a C-like systems language that keeps C’s ABI and mental model while adding modern features: modules instead of headers, slices, generics via generic modules, semantic/compile-time macros, limited operator overloading, contracts, reflection, and “zero-overhead” optional-based error handling. It aims for “evolution, not revolution”: you can drop C3 files directly into existing C builds and interoperate seamlessly. HN discussion focuses on ABI compatibility as the killer feature, the contract system’s semantics, and how C3’s “optional” return type maps to Result/Option patterns.

---

### Comment pulse
- C3 as an easy C upgrade → Full C ABI, no headers, drop-in to existing builds; praised for disciplined, non-C++-like design.
- Old problems, old answers → Pascal/Delphi/Ada already solve many “better C” goals; C3 seen as one more entrant—counterpoint: C-like syntax/ABI matter for adoption.
- Contracts and optionals debated → Contracts express invariants for optimization or runtime checks in “safe” mode; “optional” is T-or-int-error, matching C-style codes but confusingly named.

---

### LLM perspective
- View: C3 is a pragmatic “better C” aimed at incremental adoption in large existing C codebases.
- Impact: Most useful to C shops needing safer, more expressive code without rewriting libraries or abandoning C tooling.
- Watch next: Real-world ports (e.g., games, embedded), compiler maturity, and whether tooling (linters, IDEs) exploits contracts and reflection.
