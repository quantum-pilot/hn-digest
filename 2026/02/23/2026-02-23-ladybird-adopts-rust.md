# Ladybird adopts Rust

- Score: 1023 | [HN](https://news.ycombinator.com/item?id=47120899) | Link: https://ladybird.org/posts/adopting-rust/

### TL;DR
Ladybird, an independent browser project, is incrementally moving core components from C++ to Rust for memory safety and ecosystem reasons. The first big step is a 25k‑line Rust port of its JavaScript engine frontend, produced in two weeks using Claude/Codex as tightly steered coding assistants. They enforced byte‑for‑byte identical AST and bytecode output, backed by ~65k tests and real‑web lockstep runs, yielding zero regressions. HN discussion centers on this parity-first strategy, AI-as-augmentation, and concerns over repeated language pivots and rewrite risk.

---

### Comment pulse
- Output-parity porting → Identical byte/HTTP output plus strong tests makes regressions easy to spot; “translated from C++” Rust is fine, idiomatic cleanup can wait.  
- AI as collaborator → LLMs excel at mechanical porting and refactors when humans direct architecture and review; several users report big productivity gains and better tooling.  
- Language volatility worries → Some see Jakt→Swift→Rust as design churn and rewrite risk—counterpoint: long‑lived infra (Linux, PHP, musl) often safely rewrites components.

---

### LLM perspective
- View: This is a concrete, large-scale case of human-in-the-loop LLMs turning a risky rewrite into a controlled, test-driven translation.  
- Impact: Encourages other C++ heavy projects to consider Rust transitions plus LLM tooling, lowering cost while preserving behavior and performance.  
- Watch next: Whether Ladybird maintains C++/Rust parity, then successfully refactors to idiomatic Rust without another multi-year “second rewrite.”
