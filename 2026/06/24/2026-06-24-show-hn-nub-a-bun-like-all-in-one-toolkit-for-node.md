# Show HN: Nub – A Bun-like all-in-one toolkit for Node.js

- Score: 192 | [HN](https://news.ycombinator.com/item?id=48660267) | Link: https://github.com/nubjs/nub

### TL;DR

Nub is an MIT-licensed Rust toolkit that layers a Bun-like workflow onto stock Node.js rather than introducing a runtime or proprietary APIs. One binary runs TypeScript and JSX, watches dependency graphs, dispatches scripts and packages, installs dependencies, provisions project-pinned Node and package-manager versions, and reads existing npm, pnpm, Yarn, or Bun configuration. Its published macOS benchmarks show 14.7-ms script dispatch, 11-ms local package execution, and faster warm installs than Bun, pnpm, or npm. HN liked the compatibility-first design while probing ESM preload choices, transpilation needs, and unusually rapid adoption claims.

### Comment pulse

- Avoiding a new runtime reduces lock-in → Nub adds no globals, modules, config keys, lockfiles, or environment variables bearing its name.
- CommonJS preload is a deliberate optimization → the author measured 0.5 ms for `--require` versus 4.6 ms for `--import`, without changing user ESM.
- Early adoption evidence drew skepticism → one commenter claimed a zero-issue monorepo migration within an hour, prompting questions about timing.

### LLM perspective

- **View:** Nub’s differentiated bet is compatibility plus orchestration, not runtime semantics; speed comes largely from removing repeated JavaScript startup.
- **Impact:** Teams can consolidate fragmented tooling while retaining Node behavior and incumbent project metadata, lowering migration and rollback costs.
- **Watch next:** Validate benchmarks across operating systems, cold caches, large monorepos, ESM-heavy projects, lifecycle scripts, and adversarial dependency graphs.
