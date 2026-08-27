# Scm2wasm: A Scheme to WASM compiler in 600 lines of C, making use of WASM GC

- Score: 121 | [HN](https://news.ycombinator.com/item?id=45405175) | Link: https://git.lain.faith/iitalics/scm2wasm

### TL;DR

Scm2wasm is presented as a deliberately minimal Scheme-to-WebAssembly compiler, written in roughly 600 lines of C and using WebAssembly garbage collection. The sparse repository page shows a 27 KiB project with two commits, a Makefile, compiler source, and sample Scheme input. Its documented flow compiles standard input to a Wasm file, validates or prints it with wasm-tools, then invokes it through Wasmtime with garbage collection enabled. The author labels it “really bad” and does not claim standards conformance.

### Comment pulse

- Commenters pointed to Guile Hoot and other tiny Wasm language runtimes as more developed related work.
- Readers inferred that missing read and eval primitives prevent an easy REPL; one explicitly said it is not yet standard Scheme.

### LLM perspective

- View: Its value is pedagogical compression, exposing a compiler pipeline without hiding it behind a large runtime.
- Impact: Learners get a compact artifact, while real applications need language completeness, portability, and tooling.
- Watch next: Standards coverage, call/cc, REPL primitives, browser compatibility, and tests beyond the sample program.
