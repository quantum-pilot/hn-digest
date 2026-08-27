# Arborium: Tree-sitter code highlighting with Native and WASM targets

- Score: 216 | [HN](https://news.ycombinator.com/item?id=46270298) | Link: https://arborium.bearcove.eu/

### TL;DR

Arborium packages 96 curated Tree-sitter grammars with updated parsers, working highlight queries, and feature-gated Rust crates targeting native platforms and WebAssembly. It produces compact custom-element HTML or true-color ANSI, supports themes, and offers Rust, script-tag, npm, rustdoc, and diagnostic integrations. A custom WASM sysroot supplies libc functionality needed by generated C parsers. The trade-off is bundle size because each grammar embeds the Tree-sitter runtime; commenters also distinguish static highlighting from the harder problem of building a full editor.

### Comment pulse

- Developers praise the curated grammars and missing-query repairs → that maintenance is normally the hardest part of adopting Tree-sitter.
- Browser users like the simple script integration but worry grammar bundles are heavy and editable overlays introduce many edge cases.

### LLM perspective

- View: Arborium’s real product is a maintained compatibility layer, not merely another highlighting API.
- Impact: Rust documentation and web tools gain consistent parsing without independently repairing grammars or WASM builds.
- Watch next: Shared-runtime size reductions, editor-grade behavior, grammar update cadence, and security boundaries for injected documentation scripts.
