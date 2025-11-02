# GHC now runs in the browser

- Score: 229 | [HN](https://news.ycombinator.com/item?id=45782981) | Link: https://discourse.haskell.org/t/ghc-now-runs-in-your-browser/13169

- TL;DR
  - GHC, Haskell’s main compiler, now runs fully client-side in the browser via its WASM backend, offering a playground that parses, typechecks, and executes via the bytecode interpreter. Because browsers lack a C toolchain and process support, third‑party packages must be precompiled. HN welcomes frictionless onboarding for teaching/demos, probes performance versus QEMU-based approaches, debates bootstrappability for high‑trust use, and questions WasmGC’s fit for laziness. Upstream patches target dynamic loading to broaden capabilities.

- Comment pulse
  - Cold-start costs are high → ~50 MB rootfs, worker fallback warnings; Brave recovers, Safari keeps Run disabled; expected to beat QEMU‑WASM.
  - Bootstrappability is a trust blocker → no end-to-end path; sandboxed browser is safer — counterpoint: Hugs/MicroHs show possible historical bootstrap.
  - WasmGC clashes with laziness → closures/thunks need flexible representation and finalizers; extra indirections or defunctionalization would be expensive.

- LLM perspective
  - View: Browser-native GHC lowers barriers, but interpreter-only and precompiled packages limit parity with local development.
  - Impact: Eases education and demos; could drive wasm dynamic loading tooling and Haskell-on-web ecosystem maturity.
  - Watch next: Performance head-to-heads, package inclusion workflow, Safari/WebKit fixes, reproducible bootstrapping path, and feasibility of WasmGC for laziness.
