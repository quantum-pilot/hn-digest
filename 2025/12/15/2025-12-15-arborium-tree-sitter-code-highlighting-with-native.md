# Arborium: Tree-sitter code highlighting with Native and WASM targets

- Score: 216 | [HN](https://news.ycombinator.com/item?id=46270298) | Link: https://arborium.bearcove.eu/

### TL;DR
Arborium is a Rust and WebAssembly syntax highlighter built on tree-sitter, shipping curated grammars that compile to both native and browser targets. It outputs semantic HTML via custom tags and ANSI for terminals, supports 96 languages behind feature flags, and bundles many themes. Integration is simple (Rust API, `<script>` autoload, npm), with extras for rustdoc/docs.rs and CLI error reporting. The main tradeoff: large WASM bundles because each grammar embeds a full tree-sitter runtime.

### Comment pulse
- Arborium feels unusually polished: curated grammars, fixed highlight queries, and turnkey Rust/docs.rs integration → far beyond “just wiring tree-sitter.”
- Great for static highlighting and in-browser editors via overlaying highlighted HTML on a textarea → but WASM size may be heavy for small widgets.
- Tree-sitter parsing enables AST-level, context-aware highlighting → however, docs.rs allowing arbitrary HTML/JS raises serious security concerns for such integrations.

### LLM perspective
- View: Arborium shows tree-sitter-based highlighting is ready as a practical replacement for regex engines in docs and tools.
- Impact: Rust ecosystem, documentation hosts, and CLIs gain consistent, high-quality highlighting across native binaries and the web.
- Watch next: shared WASM runtime to shrink bundles, docs.rs security posture, and comparisons against Monaco/Shiki on size and latency.
