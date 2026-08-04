# GC and Exceptions in Wasmtime

- Score: 151 | [HN](https://news.ycombinator.com/item?id=48981665) | Link: https://bytecodealliance.org/articles/wasmtime-gc

### TL;DR

Wasmtime 47 enables WebAssembly GC and exception handling by default, letting high-level languages use runtime-managed structs, arrays, subtyping, and native `throw`/`try`/`catch` instead of embedding collectors or checking status returns after every call. Its new Cheney-style copying collector stores 32-bit references in sandboxed linear memory, targets many short-lived instances, and has extensive specialized fuzzing. The team prioritizes correctness over current throughput or latency and plans GC-aware compiler optimizations plus component-model integration. HN welcomed the milestone but questioned language compatibility and missing generalized effects.

### Comment pulse

- GC semantics limit immediate reach → Go and .NET reportedly do not plan adoption; Java via TeaVM fits better but lacks full compatibility.
- Exceptions are narrower than effects → stack switching could unify exceptions, async, generators, and continuations — counterpoint: generalized mechanisms are harder to optimize and fund.
- Runtime boundaries remain visible → commenters questioned bounds-check claims and requested JavaScript-object interop, threads, JIT, and interior pointers; the latter is unsupported.

### LLM perspective

- **View:** GC instructions do not standardize collector semantics; portability improves where a language’s object model already matches the runtime.
- **Impact:** Toolchains can ship smaller modules and faster exception paths, while embedders inherit collection policy and its performance tradeoffs.
- **Watch next:** Benchmark long-lived heaps, publish pause distributions, validate additional languages, complete component integration, and monitor stack-switching sponsorship.
