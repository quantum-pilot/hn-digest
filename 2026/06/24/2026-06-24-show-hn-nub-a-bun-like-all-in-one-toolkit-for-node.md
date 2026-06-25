# Show HN: Nub – A Bun-like all-in-one toolkit for Node.js

- Score: 192 | [HN](https://news.ycombinator.com/item?id=48660267) | Link: https://github.com/nubjs/nub

### TL;DR
Nub is a Bun-style, all‑in‑one toolkit built on top of plain Node.js, aiming for Bun-like developer experience without introducing any Nub-specific runtime APIs or globals. It hooks into Node via `--require` for performance, preferring CommonJS for the preload path while preserving full ESM and top‑level‑await behavior as provided by Node itself. Early adopters report painless monorepo migration and big speed gains, while some question the need for Nub’s transpiler given Node’s growing TypeScript support.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Design goal: Bun-like speed and tooling while staying 100% Node-native → no custom globals, no special config fields, everything is regular npm dependencies.
- Implementation detail: uses `--require` preload over `--import` → ~0.5 ms vs 4.6 ms overhead; Node’s newer `module.registerHooks()` API was key.
- Adoption: one team migrated a whole monorepo quickly and saw big wins → skepticism about such rapid switch—counterpoint: small friction suggests strong compatibility.

---

### LLM perspective
- View: Nub targets developers who want Bun’s ergonomics but must stick with standard Node semantics and ecosystem.
- Impact: could normalize “drop-in DX upgrades” that don’t fragment runtimes with custom globals or nonstandard module prefixes.
- Watch next: benchmarks versus Bun/Node, TypeScript pipeline details, and how Nub tracks future Node features without introducing lock-in.
