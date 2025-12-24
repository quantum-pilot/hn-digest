# Fabrice Bellard Releases MicroQuickJS

- Score: 332 | [HN](https://news.ycombinator.com/item?id=46367224) | Link: https://github.com/bellard/mquickjs/blob/main/README.md

### TL;DR
MicroQuickJS is a tiny JavaScript engine by Fabrice Bellard for embedded systems, running ES5‑ish “stricter mode” JavaScript in about 10 kB RAM and ~100 kB ROM. It drops dynamic oddities (holes in arrays, value boxing, local eval, non‑strict constructs), uses a tracing/compacting GC with its own allocator, stores strings as UTF‑8, and keeps the standard library in ROM. HN discussion centers on Lua vs JS for embedding, enthusiasm for these restrictions, and experiments like a WebAssembly playground.

---

### Comment pulse
- Redis scripting choice → author says this engine would have made JS plausible over Lua; replies defend Lua’s design, TCO, and distinctive syntax—counterpoint: JS semantics are often worse.
- Design praise → ex‑JSC developer loves the explicit constraints; they mirror the restrictions he wished were enforceable on the web but weren’t for compatibility.
- Ecosystem/infra → people share a WASM playground, note its much smaller payload than QuickJS, and lament the missing public commit history given its QuickJS roots.

---

### LLM perspective
- View: This is “JavaScript-as-DSL”: a disciplined subset optimized for predictability, not browser compatibility.
- Impact: Makes JS attractive where Lua/Tcl traditionally lived: MCUs, small RTOS targets, and firmware needing safe, user-editable scripts.
- Watch next: Compare against Lua/QuickJS/eLua on real boards, build bindings/RTOS ports, and standardize a “stricter JS” profile for tooling.
