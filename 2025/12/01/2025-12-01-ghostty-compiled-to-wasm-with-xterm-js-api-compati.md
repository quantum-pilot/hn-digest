# Ghostty compiled to WASM with xterm.js API compatibility

- Score: 198 | [HN](https://news.ycombinator.com/item?id=46110842) | Link: https://github.com/coder/ghostty-web

### TL;DR

Ghostty-web packages the native terminal emulator’s parser as a roughly 400 KB WebAssembly module behind an xterm.js-compatible API. The MIT-licensed library has no runtime dependencies and aims to let browser-terminal projects switch imports while gaining Ghostty’s grapheme handling and additional escape-sequence support. It currently patches upstream source but expects to consume a native WebAssembly distribution later. The authors call it an early proof of concept: functionality came first, and viewport rendering has not yet been benchmarked or optimized against xterm.js.

### Comment pulse

- Language framing was corrected → a commenter challenged calling JavaScript an approximation, and the maintainer removed that wording.
- Upstream guidance identified a performance path → Ghostty’s RenderState API can deliver delta updates instead of expensive per-row viewport reads.
- Compatibility enabled rapid reuse → one browser-shell project reportedly switched implementations without difficulty.

### LLM perspective

- View: Reusing one parser across native and web terminals can reduce duplicated compatibility work.
- Impact: Browser IDEs may gain stronger Unicode behavior without replacing familiar xterm-style integration code.
- Watch next: Benchmarks, RenderState adoption, API coverage, bundle growth, and an upstream WebAssembly build.
