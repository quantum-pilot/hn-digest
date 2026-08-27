# GHC now runs in the browser

- Score: 229 | [HN](https://news.ycombinator.com/item?id=45782981) | Link: https://discourse.haskell.org/t/ghc-now-runs-in-your-browser/13169

### TL;DR

A brief project update says most of the GHC library now compiles to WebAssembly and can parse, typecheck, and desugar Haskell in a browser. Dynamically linking and executing compiled Haskell remains the difficult part, though draft patches point toward a fully client-side playground. The current demo has a multi-second startup freeze while downloading and extracting an approximately 50 MB root filesystem and linking dependencies, and Safari still has problems. The supplied evidence is a promising technical milestone, not a finished browser toolchain.

### Comment pulse

- Commenters saw potential for teaching and easier experimentation, while noting mobile usability and startup-performance problems.
- Discussion of QEMU-Wasm, bootstrap trust, and WasmGC consisted largely of hypotheses rather than demonstrated results.

### LLM perspective

- View: Browser-hosted GHC is compelling for zero-install learning, provided startup and execution become predictably usable.
- Impact: Client-only tooling could lower onboarding friction without requiring a remote compilation service.
- Watch next: Measure cold starts, caching, Safari compatibility, linker completeness, and execution behavior on ordinary devices.
