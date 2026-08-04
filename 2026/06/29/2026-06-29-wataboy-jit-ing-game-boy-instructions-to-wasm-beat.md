# WATaBoy: JIT-Ing Game Boy Instructions to WASM Beats a Native Interpreter

- Score: 169 | [HN](https://news.ycombinator.com/item?id=48720190) | Link: https://humphri.es/blog/WATaBoy/

### TL;DR

WATaBoy is an undergraduate proof-of-concept Game Boy emulator that compiles SM83 basic blocks into WebAssembly at runtime, lets JavaScript compile and link them into an indirect function table, then relies on the browser’s JIT for native code. On an M2 MacBook Air, its Pokémon Blue benchmark ran 1.2× faster than the project’s native Rust interpreter and 1.5× faster than its Wasm interpreter; Safari led Chrome and Firefox. HN admired the two-stage JIT and iOS-policy workaround, while noting that beating a fetch-decode interpreter is expected and does not establish GameCube-class feasibility.

### Comment pulse

- Runtime data beats static translation → hot paths can be recompiled when control flow becomes known, while irregular code remains interpreted.
- Browser JIT becomes a policy bridge → WebAssembly reaches native compilation where iOS forbids application JITs, potentially benefiting other CPU-bound emulators.
- The speedup needs context → Wasm overhead is modest beside interpretation — counterpoint: cached interpreters and stronger baselines remain untested.

### LLM perspective

- **View:** WebAssembly can serve as a portable intermediate JIT target, trading low-level tricks for policy compatibility and cross-browser native execution.
- **Impact:** Emulator authors gain an iOS-compatible optimization path but must build bespoke code generation, linking, interrupt prediction, and fallback machinery.
- **Watch next:** Benchmark optimized cached interpreters, branch compilation, PPU interrupt prediction, larger consoles, startup cost, memory behavior, and browser-version variance.
