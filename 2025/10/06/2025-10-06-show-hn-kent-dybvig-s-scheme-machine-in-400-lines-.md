# Show HN: Kent Dybvig's Scheme Machine in 400 Lines of C (Heap-Memory Model)

- Score: 180 | [HN](https://news.ycombinator.com/item?id=45491609) | Link: https://gist.github.com/swatson555/8cc36d8d022d7e5cc44a5edb2c4f7d0b

- TL;DR
    - A compact, ~400-line C reimplementation of Dybvig’s heap-based Scheme machine: it reads S-expressions, compiles them to a tiny instruction set, and runs them on a heap VM with lexical closures and first-class continuations (call/cc). It includes a minimal REPL, fixed-size cons heap, and focuses on clarity over completeness (e.g., limited primitives, no GC). HN highlights Dybvig’s influence (Chez, Racket CS), debates MIT Scheme’s alleged C backend, and asks about this demo’s relevance and performance vs other “400-line” Schemes.

- Comment pulse
    - Chez’s speed/design → Racket’s switch to Chez improved performance and maintainability; nanopass architecture praised.
    - MIT Scheme C-backend claim → Some recall switch/goto C output; others note native code/bytecode only — counterpoint: SICP shows simple C-style compilation ideas.
    - Relevance → Direct coding of the dissertation’s heap machine; alumni praise Dybvig; curiosity about speed vs prior 400‑line compilers.

- LLM perspective
    - View: Shows end-to-end pipeline from read to bytecode to VM state transitions; unusually concise for continuations-capable Scheme.
    - Impact: Lowers barrier to experimenting with control operators and stack models; good lab material and baseline for DSL runtimes.
    - Watch next: Instrument step counts, add GC and mutation correctness, define primitive ops, then benchmark versus Chez, Racket CS, tiny-scheme variants.
