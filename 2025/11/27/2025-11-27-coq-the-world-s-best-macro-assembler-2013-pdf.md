# Coq: The World's Best Macro Assembler? (2013) [pdf]

- Score: 133 | [HN](https://news.ycombinator.com/item?id=46065698) | Link: https://nickbenton.name/coqasm.pdf

### TL;DR
This paper uses the Coq proof assistant not just to *reason about* x86, but to *be* a macro assembler with built‑in proofs. The authors formalize bits, memory, and a substantial x86 subset using dependent types and monads, then embed MASM‑style assembly syntax directly in Coq. Macros become ordinary Coq functions (for loops, conditionals, calling conventions, even small compilers like regex→DFA→x86). The assembler itself is proved correct: encodings round‑trip with a decoder and preserve separation‑logic specs of the source program.

---

### Comment pulse
- Safety‑critical dream stack → a proof‑oriented macro assembler + register allocator would fit domains like avionics, where verification already dominates cost—counterpoint: numerical stability and rounding errors remain hard to model/prove.
- Macro languages risk complexity creep → richer “convenience” features accrete until alternative implementations become implausible, locking ecosystems into one huge toolchain.
- Coq as pedagogy and design aid → writing a toy compiler in Coq felt daunting but tractable; suggests similar rigor could benefit AI compute-graph tooling.

---

### LLM perspective
- View: This shows how a proof assistant can double as a code generator, not just a checker, for very low-level targets.
- Impact: Most relevant to safety‑critical, HSM/TEE, and verified-compiler projects that must reason about real ISAs, not toy machines.
- Watch next: Better floating‑point models, verified numeric libraries, and more ergonomic DSLs that compile through such verified macro-assembly layers.
