# Functional programming and reliability: ADTs, safety, critical infrastructure

- Score: 141 | [HN](https://news.ycombinator.com/item?id=46406901) | Link: https://blog.rastrian.dev/post/why-reliability-demands-functional-programming-adts-safety-and-critical-infrastructure

### TL;DR
The article argues that highly reliable systems—especially in banking, telecom, and payments—should encode business rules directly in the type system using algebraic data types, immutability, and pure functions. By modeling lifecycles as explicit sum types, using Option/Result instead of null/exceptions, smart constructors for units, and a “pure core, effectful shell” architecture, entire classes of bugs become unrepresentable. Concrete OCaml/TypeScript examples show how this prevents double settlements, ghost billing, and config bugs, plus a pragmatic migration checklist for existing codebases. HN debates static typing vs “functional,” correctness vs fault tolerance, and evidence for reliability gains.

---

### Comment pulse
- Strong static types constrain both humans and LLMs → clearer ADTs and pure functions give compilers/LLMs tight rails, improving generated code quality and safety.
- Reliability strategy debate → some emphasize fault tolerance and reconciliation over “perfect correctness” — counterpoint: explicit state machines still reduce failure modes inside tolerant designs.
- FP vs types vs reliability → disagreement over evidence; some cite empirical studies and simple logic, others stress dynamic FP and immutability can also yield reliability.

---

### LLM perspective
- View: Rich ADTs plus purity are excellent scaffolding for LLM-assisted coding, turning vague prompts into compiler-checked, domain-safe implementations.
- Impact: Teams in high-risk domains can offload boilerplate to LLMs while keeping critical invariants encoded in types, not prose.
- Watch next: Benchmarks comparing LLM output quality across Haskell/OCaml/Rust/Python when given equivalent type-level specifications and test suites.
