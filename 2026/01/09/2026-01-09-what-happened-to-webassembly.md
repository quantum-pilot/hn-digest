# What happened to WebAssembly

- Score: 321 | [HN](https://news.ycombinator.com/item?id=46551044) | Link: https://emnudge.dev/blog/what-happened-to-webassembly/

### TL;DR

WebAssembly did not disappear; it became infrastructure that users rarely notice. The article presents it as a compact, sandboxed compilation target that bridges languages, enables safe in-process isolation, and powers products such as Figma, Ruffle, Squoosh, StackBlitz, Godot, and plugin systems. It is unlikely to replace JavaScript or the DOM, and host-boundary costs, binary size, threading, I/O, cold starts, and uneven tooling constrain broader use. HN readers largely call it successful, though some say ecosystem fragmentation and debugging remain serious adoption barriers.

### Comment pulse

- Success view → Wasm quietly powers performance-sensitive libraries and native-code reuse; invisibility is evidence of infrastructure maturity, not failure.
- Frontend limit → absent efficient DOM integration, Wasm frameworks often add complexity without displacing JavaScript, HTML, or CSS.
- Tooling complaint → fragmented standards, weak debugging, awkward imports, stale guidance, and inconsistent engine support keep routine development difficult.

### LLM perspective

- View: Wasm’s strongest role is constrained, portable computation embedded inside larger systems, not wholesale application replacement.
- Impact: Library authors and plugin platforms gain language choice; frontend teams still absorb integration and tooling costs.
- Watch next: Benchmark Component Model adoption, DOM boundaries, debugging quality, binary size, cold starts, and cross-engine portability.
