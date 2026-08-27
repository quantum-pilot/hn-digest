# Coq: The World's Best Macro Assembler? (2013) [pdf]

- Score: 133 | [HN](https://news.ycombinator.com/item?id=46065698) | Link: https://nickbenton.name/coqasm.pdf

### TL;DR

This 2013 paper embeds a concrete subset of x86 inside Coq, using dependent types, type classes, notation, and computable bit-vector semantics. Familiar Intel-style assembly, scoped labels, loops, procedures, and ordinary Coq definitions act as a macro language that assembles into machine bytes. Proofs relate encoders, decoders, emitted code, and program specifications; a verified regular-expression compiler demonstrates reuse of formal mathematics. The authors acknowledge clunky tooling, inefficient internal computation, opaque definitions, and uncertain scalability. Commenters highlighted safety-critical potential while questioning numerical and whole-system correctness.

### Comment pulse

- Verification promise → assembly-level semantic proofs could justify their cost in avionics, automotive, and other high-assurance systems.
- Boundary problem → proving software properties does not automatically prove sensors, numerical models, hardware, or complete system behavior.
- Complexity warning → a rich macro layer can itself accumulate features and threaten long-term comprehensibility.

### LLM perspective

- View: Co-locating semantics, code generation, and proofs makes low-level abstractions auditable in one formal environment.
- Impact: High-assurance developers gain stronger guarantees while accepting substantial proof engineering and tooling costs.
- Watch next: Compare modern Rocq alternatives, supported architectures, extraction performance, numerical reasoning, and industrial case studies.
