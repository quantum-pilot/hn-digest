# Notes on writing Rust-based Wasm

- Score: 195 | [HN](https://news.ycombinator.com/item?id=47295837) | Link: https://notes.brooklynzelenka.com/Blog/Notes-on-Writing-Wasm

### TL;DR

The author treats Rust-to-JavaScript WebAssembly as coordination between incompatible memory models, not a transparent function call. With wasm-bindgen, JavaScript often holds handles to Rust-owned values, so consuming an exported object can free it while leaving a broken JS pointer. Recommended defaults include references, interior mutability, non-Copy wrappers, explicit Wasm*/Js* naming, wasm_refgen for collections, real JavaScript Error conversion, and logged build identity. HN commenters value the guide but warn that async mutexes and automatic rich-type bindings add hazards; some prefer a narrow C-like boundary with handwritten JavaScript.

### Comment pulse

- Keep boundary crossings coarse: mapping every Rust getter and setter into JavaScript multiplies glue, semantic mismatch, and runtime overhead.
- Async mutexes demand restraint; holding them across yield points conflicts with structured concurrency and can create subtle failure modes.
- Component-model browser APIs may reduce marshalling — counterpoint: complexity may outweigh benefits beyond string-heavy DOM access.

### LLM perspective

- **View:** Make object lifetime and every cross-runtime call visible; ownership clarity is the strongest rule.
- **Impact:** Teams trade ergonomic purity for fewer stale handles, re-entrancy failures, and opaque errors.
- **Watch next:** Component-model adoption, binding safety, wasm_refgen maturity, and coarse-versus-rich boundary benchmarks.
