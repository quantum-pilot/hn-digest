# Saying goodbye to asm.js

- Score: 299 | [HN](https://news.ycombinator.com/item?id=48206340) | Link: https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html

### TL;DR

Firefox 148 disables SpiderMonkey’s special asm.js optimizations by default, with full removal planned. Existing asm.js will still execute as ordinary JavaScript through the normal JIT, but maintainers should recompile to WebAssembly for smaller binaries and faster execution. Mozilla credits the 2013 technology with bringing Unity, Unreal, and C/C++ applications to browsers and proving near-native web performance, directly paving the way for WebAssembly. HN viewed retirement as successful obsolescence, though some lamented WebAssembly’s slow ecosystem maturation and the web’s drift toward bulky Electron applications rather than lightweight client-side sandboxes.

### Comment pulse

- asm.js won by being small and deployable → its standards-compatible JavaScript subset reached production before the more ambitious NaCl/PNaCl stack.
- Figma illustrates bridge value → asm.js proved a C++ browser product viable before revenue, while WebAssembly later cut parsing and load costs.
- Sandbox potential feels underused → counterpoint: WebAssembly survives the original vision, but mature universal tooling and safe local AI execution remain incomplete.

### LLM perspective

- **View:** Removing a compatibility fast path after migration is maintenance when semantics remain intact and the successor is measurably better.
- **Impact:** SpiderMonkey loses maintenance and attack surface; remaining asm.js publishers keep compatibility but surrender specialized compilation performance.
- **Watch next:** Removal release, residual-usage telemetry, migration regressions, WebAssembly benchmarks, and browser support for sandboxed local workloads.
