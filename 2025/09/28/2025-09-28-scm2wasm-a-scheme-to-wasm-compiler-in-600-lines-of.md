# Scm2wasm: A Scheme to WASM compiler in 600 lines of C, making use of WASM GC

- Score: 121 | [HN](https://news.ycombinator.com/item?id=45405175) | Link: https://git.lain.faith/iitalics/scm2wasm

- TL;DR
  - A tiny (~600 LOC) C compiler lowers a minimal subset of Scheme to WebAssembly using the Wasm GC type system. The repo demonstrates a simple compile/run flow with wasmtime -Wgc; it’s a teaching toy, not a standards‑compliant Scheme. HN highlights related Wasm-GC experiments, Guile Hoot as a fuller Scheme→Wasm option, and questions about practicality (REPL, call/cc). Commenters note it’s not an interpreter replacement; the fast‑evolving Wasm spec remains a challenge for targets.

- Comment pulse
  - Wasm is a moving target vs asm.js → Asm.js ran everywhere immediately; Wasm GC still stabilizing, hurting portability — counterpoint: Chrome/Firefox/Wasmtime ship GC; Safari lags.
  - Guile Hoot offers mature Scheme→Wasm with Wasm GC → supports REPL-like needs better; Safari bugs noted.
  - This project is minimal → lacks read/eval and probably call/cc; not a standards-compliant Scheme or drop-in interpreter.

- LLM perspective
  - View: Clean proof-of-concept showing Wasm GC from a tiny compiler rather than via C/C++ toolchains.
  - Impact: Helps language implementers prototype GC’d targets; validates Wasm GC primitives for tagged data and heap-allocated objects without JS glue.
  - Watch next: GC spec adoption across engines, baseline performance vs Hoot/wasm-gc, feasibility of tail calls/continuations, REPL, and module interop.
