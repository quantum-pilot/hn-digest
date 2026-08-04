# Show HN: Firefox in WebAssembly

- Score: 241 | [HN](https://news.ycombinator.com/item?id=48926939) | Link: https://developer.puter.com/labs/firefox-wasm/

### TL;DR

A Puter Labs experiment compiles Firefox’s Gecko engine and full interface to WebAssembly, allowing Firefox to run and render entirely inside an existing browser tab. Web content reaches the nested browser through a configurable Wisp WebSocket proxy hosted by Puter, with networking supplied by Puter.js. Optional WebGL acceleration handles page rendering, while an experimental JavaScript-to-WebAssembly JIT can be enabled with an explicit warning about instability. The result demonstrates desktop-browser portability, but no benchmarks, compatibility matrix, privacy details, or resource requirements are provided.

### Comment pulse

- Nested execution works but strains stability → commenters reportedly launched Firefox inside itself, though deeper nesting often froze or loaded only once.
- Locked-down devices inspire practical demand → a TV owner hoped to gain extension-based ad blocking — counterpoint: one-to-two-gigabyte systems may exhaust memory.
- The development cost is unclear → readers disputed whether the cited 25k represented tokens, dollar-equivalent usage, or subscription-accounted consumption.

### LLM perspective

- **View:** This proves systems portability: a browser runtime can become an application payload inside another browser.
- **Impact:** It could bring modern rendering to restricted platforms, but proxy dependence, memory overhead, performance, and extension support constrain usefulness.
- **Watch next:** Measure startup time, RAM, nested stability, standards coverage, JIT correctness, extension support, proxy privacy, and self-hosted networking.
