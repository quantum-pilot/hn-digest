# WATaBoy: JIT-Ing Game Boy Instructions to WASM Beats a Native Interpreter

- Score: 169 | [HN](https://news.ycombinator.com/item?id=48720190) | Link: https://humphri.es/blog/WATaBoy/

- TL;DR  
An undergraduate project builds a Game Boy emulator that JIT-compiles CPU instructions directly to WebAssembly, beating a conventional native interpreter while still running entirely in the browser. By leaning on browsers’ existing JS/WASM JITs, it even works on iOS, where apps cannot normally JIT. HN discussion connects this to earlier static recompilation work, highlights why JIT is better for tricky console ROMs, and notes cross-browser performance gaps, with Firefox lagging Chrome and Safari.  
*Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - JITting hot paths from Game Boy bytecode to WASM outperforms interpreters → interpreter dispatch dominates; WASM gets near-native, ~20% overhead instead of ~1000%.  
  - Static recompilation of old console ROMs is brittle → handwritten assembly, self-modifying tricks; JIT with runtime knowledge better identifies hot blocks and safe translations.  
  - Using browser WASM JIT sidesteps iOS JIT ban for emulators → WebKit already JITs JS/WASM; similar tricks could aid apps—counterpoint: portability and policy risks remain.

- LLM perspective  
  - View: JIT-to-WASM emulation shows browsers as viable high-performance consoles, especially on locked-down platforms like iOS.  
  - Impact: Emulator authors may target WebAssembly first, then share cores across web, desktop, and potentially app-embedded runtimes.  
  - Watch next: head-to-head benchmarks versus established emulators, memory overhead analysis, and exploration of multi-system JIT frameworks atop WASM.
