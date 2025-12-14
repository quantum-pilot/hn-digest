# A Lisp Interpreter Implemented in Conway's Game of Life (2021)

- Score: 85 | [HN](https://news.ycombinator.com/item?id=46251620) | Link: https://woodrush.github.io/blog/posts/2022-01-12-lisp-in-life.html

## TL;DR

A developer built a full Lisp interpreter that literally runs inside Conway’s Game of Life. The Lisp is first written in C, compiled by ELVM into QFTASM for a custom CPU implemented in an 8-state cellular automaton (VarLife), then “metafied” so each VarLife cell becomes a huge OTCA metapixel running on standard Life. Programs are fed in as ASCII in RAM; the system supports closures, macros, and nontrivial examples (OO-style code, Z combinator). Heavy multi-layer optimizations make small Lisp programs finish in minutes (VarLife) or hours (pure Life) on a modern PC.

---

## Comment pulse

- This fits a tradition of “extreme compilation targets” → compared to Chaitin’s LISP interpreter compiled into a single Diophantine equation.  
- ELVM context → 8cc-to-IR-to-weird-backends toolchain, including QFTASM and λ-calculus; same author previously built C and Lisp machinery expressed purely in λ-calculus.  
- Meta-note → this project has multiple prior HN threads; commenters see it as part of a growing niche of computation-in-esoteric-media demos.

---

## LLM perspective

- View: Demonstrates an end-to-end stack from C to high-level Lisp evaluation embedded in a Turing-complete cellular automaton, stressing practical engineering, not just theory.  
- Impact: Useful as a teaching and research artifact for compilation pipelines, PL implementation, and cellular automata–based computing.  
- Watch next: Tooling that generalizes this approach—automated backends from IRs/VMs to other physical or symbolic substrates (CAs, circuits, proof assistants).
