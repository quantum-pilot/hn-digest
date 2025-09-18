# WASM 3.0 Completed

- Score: 811 | [HN](https://news.ycombinator.com/item?id=45279384) | Link: https://webassembly.org/news/2025-09-17-wasm-3.0/

- TL;DR
    - Wasm 3.0 lands with Memory64, multi-memory, low‑level GC with typed references, tail calls, native exceptions, relaxed SIMD plus a deterministic profile, annotations, and JS string builtins. It targets larger datasets and more languages while shipping across major browsers and standalone engines. HN welcomes 64‑bit for heavy web apps (e.g., editors) but notes bounds‑check costs and mobile/tab caps. GC support excites high‑level language users, though embedded/allocator fit is debated. Direct DOM access remains via JS interop; 3.0 functions as a feature bundle many engines already implement.
- Comment pulse
    - Memory64 unlocks heavier web apps → removes 4GiB ceiling; but introduces bounds-check overhead and mobile/OS per‑tab caps may still limit usable memory.
    - Low-level GC + typed refs boost high-level languages → compilers control layouts; — counterpoint: generic GC may ill-fit embedded targets or language-specific allocation strategies.
    - Direct DOM from Wasm is unlikely → would require restandardizing a lower-level DOM; current path is JS interop, not “killing JavaScript.”
- LLM perspective
    - View: 3.0 shifts Wasm from “C/Rust sandbox” to a general multi-language runtime with optional GC and deterministic profile.
    - Impact: Browsers and runtimes gain larger heaps; Java/Kotlin/OCaml compilers mature; performance tuning around Memory64 overheads and GC behavior becomes central.
    - Watch next: Measure Memory64 overheads, GC pauses, relaxed SIMD gains; track deterministic profile adoption, mobile caps, and non-browser shipping (e.g., Wasmtime).
