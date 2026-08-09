# How to make a fast dynamic language interpreter

- Score: 241 | [HN](https://news.ycombinator.com/item?id=47843194) | Link: https://zef-lang.dev/implementation

### TL;DR

Starting from a string-and-hashtable-heavy AST walker, the author makes the Zef dynamic-language interpreter 16.6× faster without bytecode, SSA, a JIT, or garbage-collector tuning. The largest gain—4.55× alone—comes from replacing per-object hash tables with offset-based storage, then adding inline caches and watchpoints by rewriting AST nodes in place. Smaller wins include interned symbols, direct operator nodes, cheaper argument representations, specialized getters and setters, improved slow paths, and build flags. Across four benchmarks, optimized Fil-C++ Zef remains roughly 2.1× slower than CPython 3.10.

### Comment pulse

- Readers highlighted optimization #6 as decisive: naive dynamic property dispatch dominated almost everything else.
- Some noted language design can eliminate expensive dynamism before implementation work begins.
- The benchmark isolation drew praise — counterpoint: specialized `sqrt` gains suggest the suite may overweight particular hot paths.

### LLM perspective

- Profile-driven optimization works best when representation changes remove entire classes of repeated work.
- Interpreter inline caches can mutate AST nodes directly, trading simplicity for immutability and concurrency constraints.
- The Yolo-C++ result is illustrative, not production-ready, because its temporary allocator never frees memory.
