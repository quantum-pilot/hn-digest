# GC and Exceptions in Wasmtime

- Score: 151 | [HN](https://news.ycombinator.com/item?id=48981665) | Link: https://bytecodealliance.org/articles/wasmtime-gc

### TL;DR
Wasmtime 47 enables WebAssembly GC and exceptions by default, letting languages with managed memory and exceptions target Wasm without shipping custom runtimes. Wasmtime implements a Cheney semi-space collector on top of Wasm linear memory for safety, portability, and simple, fast allocation, but it’s tuned for many short-lived instances rather than single long-lived heaps and isn’t yet as optimized as V8/SpiderMonkey. HN discussion centers on missing advanced control-flow (effects/stack switching), limited fit for Go/.NET GC models, and technical GC details.

### Comment pulse
- Effects generalize exceptions → commenters want wasmfx-style stack switching; proposal stalled awaiting sponsorship — counterpoint: some call Wasm “perpetual progress” and ignore it for now.  
- Wasm GC MVP suit Java/JS-like models → Go and .NET teams say semantics don’t match their collectors; Java AOT tools like TeaVM already target it.  
- Runtime uses 32-bit indices into linear memory → readers debate which bounds checks disappear, whether i31 aids interop, and note lack of interior pointers.  

### LLM perspective
- View: With GC and exceptions, Wasm increasingly competes with JVM/CLR as a general-purpose execution layer, not merely a browser plugin.  
- Impact: Compiler writers for Java, Kotlin, Clojure, etc. gain a realistic browser/server target without bundling heavyweight custom collectors.  
- Watch next: concrete perf benchmarks vs V8/SpiderMonkey, progress on stack switching/effects, and whether major runtimes reconsider Wasm GC adoption.
