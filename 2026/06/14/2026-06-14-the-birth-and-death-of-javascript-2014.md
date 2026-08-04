# The Birth and Death of JavaScript (2014)

- Score: 228 | [HN](https://news.ycombinator.com/item?id=48526661) | Link: https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript

### TL;DR

Gary Bernhardt’s 2014 PyCon talk uses science fiction and comedy to trace JavaScript and programming from 1995 through an imagined 2035. It criticizes JavaScript’s flaws while arguing its industry impact becomes strongly positive, especially as the language evolves from something developers write into a ubiquitous compilation substrate. Rewatching in 2026, HN readers saw partial validation in TypeScript, Electron, WebAssembly, and widespread transpilation. Others said the forecast remains overstated: developers still write extensive JavaScript, WebAssembly lacks direct DOM access, and predicted runtime changes never occurred.

### Comment pulse

- Substrate status arrived partially → JavaScript became a common target for transpilers and desktop wrappers, while TypeScript often supplies the source language.
- WebAssembly has not displaced JavaScript → missing direct DOM manipulation preserves glue code, and JavaScript remains easier to inspect, debug, and modify.
- Cross-platform shipping favors compromise → Electron’s weight draws criticism — counterpoint: small teams value one codebase across macOS, Windows, and Linux.

### LLM perspective

- **View:** A language can die socially while winning infrastructurally: abstraction layers obscure it even as compatibility locks it underneath.
- **Impact:** Developers gain portable tooling but inherit browser-era constraints, duplicated runtimes, and long-lived dependence on JavaScript semantics.
- **Watch next:** Track Wasm DOM integration, application adoption, TypeScript defaults, Electron alternatives, and whether browsers expose first-class non-JavaScript execution paths.
