# Arborium: Tree-sitter code highlighting with Native and WASM targets

- Score: 216 | [HN](https://news.ycombinator.com/item?id=46270298) | Link: https://arborium.bearcove.eu/

### TL;DR

Arborium packages 96 hand-selected Tree-sitter grammars with working highlight queries for native Rust and WebAssembly. It outputs compact custom-element HTML or true-color ANSI, offers feature-gated languages and bundled themes, and supports direct Rust, npm, script-tag, rustdoc, and miette integrations. A custom WASM sysroot supplies libc dependencies that C-based parsers expect. The principal tradeoff is size: each grammar embeds the Tree-sitter runtime despite aggressive optimization. Commenters praised the easy static-highlighting path but questioned payload weight and interactive-editor ergonomics.

### Comment pulse

- Developers valued curated, repaired grammars because assembling compatible parsers and highlight queries independently had proved difficult.
- The editable demo overlays highlighted output on a textarea; commenters noted production editing still brings many synchronization corner cases.
- Arbitrary HTML and JavaScript in hosted rustdoc pages raised security concern beyond Arborium itself.

### LLM perspective

- View: Arborium turns fragmented Tree-sitter components into a coherent, unusually approachable highlighting distribution.
- Impact: Rust, browser, terminal, and documentation tools gain one parser-backed highlighting stack across targets.
- Watch next: Shared WASM runtime work, per-language download sizes, editor integration, and response to rustdoc security concerns.
