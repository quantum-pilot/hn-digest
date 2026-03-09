# Notes on writing Rust-based Wasm

- Score: 195 | [HN](https://news.ycombinator.com/item?id=47295837) | Link: https://notes.brooklynzelenka.com/Blog/Notes-on-Writing-Wasm

### TL;DR

The post is a field guide to making Rust→Wasm→JS interop less painful when using `wasm-bindgen`. The author’s main rules: treat the JS/Wasm boundary as dangerous; pass handles by reference and use `Rc<RefCell<T>>`/`Arc<Mutex<T>>` instead of `&mut` to avoid reentrancy bugs and broken pointers; never `Copy` exported handle types; enforce strict naming (`Wasm*` for Rust exports, `Js*` for JS imports) to clarify ownership; use duck-typed JS imports plus `wasm_refgen` to move exported types inside collections safely; and convert Rust errors into real JS `Error` objects. They also recommend embedding Git build info in the Wasm bundle for debugging version mismatches.

---

### Comment pulse

- Component Model in browsers may simplify APIs and improve string marshalling → skeptics see high complexity and limited wins, especially for WebGPU/WebGL data paths.  
- Async mutexes in Rust are seen as a code smell → easy to misuse across await points; some recommend avoiding Tokio and using tools like `shadow-rs` for build info.  
- Auto-bindings (wasm-bindgen/embind) add bloat and complexity → some prefer a thin, C-style API and hand-written JS, minimizing boundary crossings — counterpoint: article argues carefully-structured bindgen yields strong compile-time guarantees.

---

### LLM perspective

- View: These patterns normalize treating JS↔Wasm as an FFI boundary with explicit ownership, not a transparent language bridge.  
- Impact: Most useful for library/framework authors exposing Rust to the web; less critical for pure compute kernels with minimal JS interaction.  
- Watch next: Browser-level Component Model support, richer tooling like `tsify`/`wasm_refgen`, and profiling of boundary costs on real-world apps.
