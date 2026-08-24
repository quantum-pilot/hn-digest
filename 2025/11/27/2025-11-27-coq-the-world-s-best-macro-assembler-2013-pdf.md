# Coq: The World's Best Macro Assembler? (2013) [pdf]

- Score: 133 | [HN](https://news.ycombinator.com/item?id=46065698) | Link: https://nickbenton.name/coqasm.pdf

### TL;DR

A 2013 paper turns Coq into an executable environment for modeling a subset of x86, writing Intel-style assembly, emitting machine bytes, and proving the assembler preserves program meaning. Dependent types describe fixed-width words and valid instructions; scoped labels and ordinary definitions become macros for loops, procedures, and calling conventions. A verified regular-expression pipeline reuses a Coq DFA library to generate x86. HN discussion admired the integration while testing its practical limits for safety-critical work.

### Comment pulse

- Integrated proof changes low-level economics → one safety-critical developer said demonstrating correctness already costs more than writing code.
- A proof inherits its model's boundaries → commenters asked how quantization, rounding, hardware behavior, and system assumptions enter correctness claims.
- Rich macros can recreate language complexity → abstractions ease proofs — counterpoint: feature growth may reduce stability and independent implementations.

### LLM perspective

- View: Co-locating semantics, code generation, and proofs makes compatibility itself a theorem.
- Impact: Systems engineers can trade compiler layers for explicit assumptions and machine-level evidence.
- Watch next: Rocq-era successors, broader ISA coverage, native computation, solver integration, and verified numerical case studies.
