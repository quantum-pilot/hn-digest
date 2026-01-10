# What happened to WebAssembly

- Score: 321 | [HN](https://news.ycombinator.com/item?id=46551044) | Link: https://emnudge.dev/blog/what-happened-to-webassembly/

- TL;DR  
WebAssembly didn’t fail; it quietly succeeded in a different role than hype suggested. The article argues Wasm is a secure, portable bytecode—more like JVM than an app framework—now powering Figma, Godot, Squoosh, Cloudflare Workers, plugin systems and many browser libraries. Its strengths are sandboxing, portability and reuse of native code, not replacing HTML/CSS/JS. HN commenters largely agree, but highlight weak DOM access, fragmented standards and immature tooling as major brakes on broader, “write-your-whole-app” adoption.

- Comment pulse  
  - Expectation mismatch: many imagined Wasm replacing JS/HTML; instead it powers codecs, emulators, plugins and build tools behind the scenes, which practitioners consider genuine success.  
  - DOM access: lack of fast, first-class bindings forces virtual-DOM shims and JS bridges; some predict fixing this could sideline JS—counterpoint: most developers avoid assembly-like layers.  
  - Tooling drag: commenters cite fragile Emscripten/wasi-sdk stacks, weak optimizers, poor debugging, awkward module loading and threading headers, plus stalled Rust support, as serious adoption friction.

- LLM perspective  
  - View: See Wasm as a stable ABI for multi-language plugins, sandboxed compute and serverless, not a replacement presentation layer.  
  - Impact: Platform owners standardizing WASI/component model and shipping ergonomic JS/TS interop will shape real-world usefulness more than raw performance gains.  
  - Watch next: Debugger quality, cross-runtime component tooling, and credible DOM/canvas integration will signal whether Wasm is ready for application-layer use.
