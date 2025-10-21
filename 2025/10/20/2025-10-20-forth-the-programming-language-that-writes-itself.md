# Forth: The programming language that writes itself

- Score: 307 | [HN](https://news.ycombinator.com/item?id=45639250) | Link: https://ratfactor.com/forth/the_programming_language_that_writes_itself.html

- TL;DR
  - The piece traces Chuck Moore’s pursuit of simplicity: Forth wasn’t born from abstract concatenative theory but from a need for an interactive, tiny interpreter. RPN and stacks are surface traits; the essence is extensibility—defining new words, control structures, and metaprogramming so the system “writes itself.” It contrasts Forth with Joy/combinators, situating its origins in 1950–60s constraints (IBM 704, Burroughs B5500). HN adds early-micro nostalgia, embedded successes, DSL-building use, plus caveats: cognitive stack tax and debates over lambda-calculus as universal IR.

- Comment pulse
  - Byte 1980 inspired many; Forth fit tiny RAM, fast to implement; great for embedded/slots — counterpoint: BASIC dominated for approachability.
  - Power/flexibility: grow DSLs, new control words; interactive tweaks accelerate hardware/software co-design — counterpoint: mental stack juggling hurts readability.
  - Theory vs practice: some want lambda calculus as universal IR; others note Forth maps poorly, prefer denotational semantics or domain-specific stacks.

- LLM perspective
  - View: Forth’s value is a tiny, extensible interpreter enabling on-target development and DSLs; concatenative purity is optional.
  - Impact: Best fit for embedded, games tooling, simulators; teams gain rapid iteration and inspectable machine-near code.
  - Watch next: Modern minimal VMs (uxn), Forth-on-RISC-V cores, educational “build a Forth” kits; compare against Lua/wasm for embedding.
