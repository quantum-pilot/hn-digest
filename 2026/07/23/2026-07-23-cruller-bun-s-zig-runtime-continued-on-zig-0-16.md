# Cruller: Bun's Zig Runtime, Continued on Zig 0.16

- Score: 149 | [HN](https://news.ycombinator.com/item?id=49017344) | Link: https://ziggit.dev/t/cruller-buns-zig-runtime-continued-on-zig-0-16/16734

### TL;DR

Cruller repackages the last Zig-based Bun release as a Linux x64 runtime for pre-built production JavaScript, ported from Bun’s patched toolchain to upstream Zig 0.16. It retains JavaScriptCore, Bun.serve, HTTP/1–3, WebSockets, fetch, streams, and module resolution, while removing development tools such as the package manager, bundler, transpiler, shell, and test runner. A stripped build is 73 MiB versus Bun’s 88.5 MiB, with benchmark parity. HN welcomed an embeddable Zig runtime but questioned dev–production divergence, lost Git history, maintenance prospects, and the reduced feature set’s value.

### Comment pulse

- Deployment-only scope divided readers → supporters saw a lean embeddable JavaScript engine — counterpoint: others feared production-only behavior absent from the full development runtime.
- Squashed history drew the sharpest criticism → lost authorship, blame context, bisectability, and licensing provenance could obstruct debugging, compliance, and future contributors.
- Upstream Zig is the technical opening → removing Bun’s compiler fork enables cleaner builds and future incremental-compilation experiments, though code generation still bootstraps through Bun.

### LLM perspective

- **View:** Cruller is closer to a deployable JavaScriptCore distribution than a Bun fork competing for end users.
- **Impact:** Zig applications gain a possible embedded server runtime; operators assume compatibility testing across two materially different execution environments.
- **Watch next:** Track reproducible clean builds, restored provenance, cross-platform support, production compatibility suites, memory behavior, and a stable embedding API.
