# Making WebAssembly a first-class language on the Web

- Score: 368 | [HN](https://news.ycombinator.com/item?id=47331811) | Link: https://hacks.mozilla.org/2026/02/making-webassembly-a-first-class-language-on-the-web/

### TL;DR

WebAssembly has matured, but on the web it remains subordinate to JavaScript: loading modules is awkward, Web APIs require language-specific JS bindings, conversion adds runtime cost, documentation assumes JS, and standard compilers cannot emit self-contained browser applications. A 2020 DOM experiment cut update time 45% by bypassing glue. The author proposes WebAssembly Components and WIT interfaces as a standardized, multi-language artifact browsers could load and bind directly to Web APIs. It remains aspirational—browser integration is undesigned and tooling early—and commenters fear complexity may merely move.

### Comment pulse

- Direct DOM access remains the test → without privileged Web API bindings, Wasm still inherits JavaScript’s conceptual and performance tax.
- Components broaden portability beyond browsers → counterpoint: choosing a new intersection-style IDL delayed WebIDL integration but enables non-web and cross-language use.
- Tooling must disappear into compilers → generated WIT scaffolding currently looks intimidating, especially outside mature Rust support.

### LLM perspective

- **View:** A first-class target needs one deployable artifact and web-native types, not another unofficial per-language distribution.
- **Impact:** Smaller teams could adopt Wasm for ordinary applications, while browsers centralize binding maintenance.
- **Watch next:** ESM integration, component standardization, native browser execution, DOM interface design, and no-glue benchmarks.
