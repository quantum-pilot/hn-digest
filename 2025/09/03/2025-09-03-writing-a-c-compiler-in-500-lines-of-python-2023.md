# Writing a C compiler in 500 lines of Python (2023)

- Score: 246 | [HN](https://news.ycombinator.com/item?id=45117668) | Link: https://vgel.me/posts/c500/

- TL;DR
    - An engineer built a surprisingly functional C compiler in ~500 lines of Python by doing single-pass codegen to WebAssembly. It maintains a manual C stack, uses a typedef-aware lexer hack, and tracks place vs value to emit correct loads/stores. It supports ints, pointers, arrays, functions, and typedefs; omits structs, floats, preprocessor, 64-bit types; and passes 34/220 c-testsuite cases. WASM’s structured control flow forces tricks like re-parsing for-loops’ increment. HN debates C’s complexity and single-pass vs AST trade-offs.

- Comment pulse
    - C’s full spec is elusive → standard trails implementations; headers hard; compilers vary; MSVC lags — counterpoint: many still happily target C89 simplicity.
    - Single-pass surprise → easier when skipping optimization and constrained memory; C designed for it; Python ASTs are verbose vs ML-family.
    - Wasm as target → clean stack machine, but structured control flow complicates for/goto; book and C4 suggested for deeper multi-pass compilers.

- LLM perspective
    - View: Single-pass + WASM shows constraints drive design; hacks (lexer cloning, place/value) replace IR.
    - Impact: Great teaching/stage0 compilers; not production—missing preprocessor, structs, FP, diagnostics.
    - Watch next: Add structs/floats, retarget to x86-64/RISC-V, or insert tiny IR to kill reparse hacks; measure c-testsuite gains.
