# Ghostty compiled to WASM with xterm.js API compatibility

- Score: 198 | [HN](https://news.ycombinator.com/item?id=46110842) | Link: https://github.com/coder/ghostty-web

### TL;DR
Ghostty‑web compiles Ghostty’s native terminal emulator core to WebAssembly and wraps it in an xterm.js‑compatible API, so web apps can swap `@xterm/xterm` for `ghostty-web` with minimal code changes. It aims to fix long‑standing xterm.js issues (e.g., complex-script rendering, XTPUSHSGR/XTPOPSGR) by reusing the same VT100 engine as the desktop Ghostty app. HN discussion centers on wording (“proper implementation”), performance vs xterm.js, and new demos using Wasmer and in-browser shells.

---

### Comment pulse
- “Proper VT100” wording is seen as dismissive of xterm.js → maintainer agrees and removes the “JavaScript approximation” phrase from the README.  
- Ghostty’s architecture is praised → native, cross‑platform core showcases that polished Mac/Linux apps need not be tied to Swift/Obj‑C.  
- Performance and API future → Mitchell Hashimoto suggests using Ghostty’s RenderState API for fast delta rendering; current build is PoC with benchmarks and better demos planned—counterpoint: users already hit demo bugs.

---

### LLM perspective
- View: Treat this as an xterm.js‑compatible “engine swap” that prioritizes correctness and reuse of a well‑tested emulator core.  
- Impact: Browser IDEs, cloud dev platforms, and remote shells gain better Unicode and escape‑sequence behavior without a full terminal rewrite.  
- Watch next: Benchmarks vs xterm.js, adoption in major tools, and standardized WASM terminal APIs emerging around Ghostty/libghostty.
