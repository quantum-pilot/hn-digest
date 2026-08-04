# TypeScript 7

- Score: 433 | [HN](https://news.ycombinator.com/item?id=48833715) | Link: https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/

### TL;DR

TypeScript 7 replaces the JavaScript implementation with a structurally faithful Go port using native execution and shared-memory parallelism. Microsoft reports 7.7–11.9× faster full builds and lower aggregate memory across five large projects. The release adds an LSP server, rebuilt watch mode, configurable parallelism, stricter defaults, and removed legacy options. The main migration gap is programmatic access: 7.0 has no API, so tools and embedded-language ecosystems including Vue, Svelte, Astro, MDX, and Angular may need TypeScript 6 side-by-side until 7.1. HN praised the port, debated Go’s suitability, and probed downstream compatibility.

### Comment pulse

- Performance changes daily ergonomics → faster project loading, diagnostics, references, CI, and agent checks matter even when developers rarely invoke `tsc` manually.
- No API is the practical blocker → transpilers may be independent, but declaration tooling, linters, framework language services, and plugins still embed TypeScript.
- Go prioritized port fidelity and team velocity → readers accepted sufficient native speed — counterpoint: some wondered whether Rust could extract another modest gain.

### LLM perspective

- **View:** The architectural win is not Go alone; faithful reimplementation plus parallelism, memory sharing, and ecosystem testing produced the step-change.
- **Impact:** Large repositories regain responsive local type-checking and shorter CI queues, potentially changing workflows that previously deferred checks.
- **Watch next:** Track API delivery, framework adoption, checker determinism, resource tuning, regressions, and real-world incremental performance beyond headline full builds.
