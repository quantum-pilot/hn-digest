# WASM 3.0 Completed

- Score: 811 | [HN](https://news.ycombinator.com/item?id=45279384) | Link: https://webassembly.org/news/2025-09-17-wasm-3.0/

### TL;DR

WebAssembly 3.0 becomes the live standard with 64-bit address spaces, multiple memories, runtime-managed garbage collection, richer typed references, tail calls, native exceptions, relaxed SIMD, deterministic execution rules, annotations, and JavaScript string built-ins. The additions improve compilation targets for high-level languages and larger non-web workloads; most major browsers already ship them. HN discussion welcomed GC and memory64 but flagged bounds-check costs, browser memory caps, embedded constraints, and the continued need to reach the DOM through JavaScript APIs.

### Comment pulse

- Memory64 enables workloads beyond 4 GiB → practical gains depend on browser caps and may incur bounds-check overhead.
- Low-level GC broadens language support → critics question allocator flexibility and suitability for constrained targets.
- Direct DOM access remains unlikely → wrappers preserve existing web APIs, while commenters dispute whether their overhead is significant.

### LLM perspective

- View: Version 3.0 strengthens Wasm as a language-neutral runtime more than as a JavaScript replacement.
- Impact: Compiler authors gain native primitives previously emulated through hosts or custom runtimes.
- Watch next: Standalone-engine parity, production memory64 costs, GC portability, and custom page-size progress.
