# A pure scheme web programming tool

- Score: 131 | [HN](https://news.ycombinator.com/item?id=48877314) | Link: https://goeteia.dev

### TL;DR

Goeteia is an MIT-licensed, self-hosting Scheme toolkit that compiles full R6RS and syntax-case to Wasm GC in the browser. Its roughly 50KB-gzipped compiler supports hygienic macros, exact arithmetic, continuations, tail calls, reactive s-expression HTML/CSS, custom text layout, GPU shaders, and s-expression networking; the same source can generate a JavaScript fallback. The live homepage demonstrates compilation and graphics end to end. HN admired the technical breadth but questioned novelty beside Hoot, claims that Scheme improves AI reliability, and launch-demo polish after a cursor-offset bug.

### Comment pulse

- Prior art matters → Hoot already brings Scheme to WebAssembly through Spritely, making Goeteia’s differentiators the integrated compiler, web stack, and graphics.
- Reliability claims split readers → s-expressions may suit macros — counterpoint: Scheme is not statically verified, and compilation cannot ensure AI-written correctness.
- Demo credibility took a hit → Chrome/macOS users saw edits land one row above the cursor, though compilation still worked.

### LLM perspective

- **View:** Goeteia’s strongest idea is one-language continuity across macros, UI, shaders, serialization, and server control flow.
- **Impact:** Scheme developers gain a compact browser-native stack; broader adoption depends on tooling, interoperability, and debugging quality.
- **Watch next:** Compare Hoot, ClojureScript, and Goeteia on bundle size, startup, standards coverage, editor stability, and real applications.
