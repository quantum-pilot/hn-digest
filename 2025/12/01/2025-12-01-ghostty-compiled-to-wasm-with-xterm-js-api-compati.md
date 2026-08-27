# Ghostty compiled to WASM with xterm.js API compatibility

- Score: 198 | [HN](https://news.ycombinator.com/item?id=46110842) | Link: https://github.com/coder/ghostty-web

### TL;DR

ghostty-web compiles Ghostty’s terminal parser to WebAssembly and wraps it in an API intended to ease migration from xterm.js. The MIT-licensed package has no runtime dependencies, uses an approximately 400KB WASM bundle, and claims better handling of complex scripts plus escape sequences missing from xterm.js. It currently patches Ghostty to expose required functions, with plans to consume a native WASM distribution later. The author calls it a proof of concept: performance work and comparative benchmarks have not yet been done.

### Comment pulse

- A claim contrasting “proper” emulation with JavaScript was challenged as needlessly pejorative and removed.
- Ghostty’s author recommended the stateful RenderState API → current per-row viewport reads likely make rendering unnecessarily expensive.
- Demo migration appeared easy, though one tester reported commands produced no output and browser-console errors.

### LLM perspective

- View: API compatibility makes parser reuse practical, but terminal correctness and rendering performance are separate achievements.
- Impact: Browser-terminal projects could share Ghostty’s native-tested semantics without immediately rewriting xterm.js integrations.
- Watch next: Benchmarks should measure throughput, latency, memory, Unicode correctness, and delta-rendering gains against xterm.js.
