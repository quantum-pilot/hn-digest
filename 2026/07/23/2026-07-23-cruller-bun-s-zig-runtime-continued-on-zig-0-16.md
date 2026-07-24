# Cruller: Bun's Zig Runtime, Continued on Zig 0.16

- Score: 149 | [HN](https://news.ycombinator.com/item?id=49017344) | Link: https://ziggit.dev/t/cruller-buns-zig-runtime-continued-on-zig-0-16/16734

### TL;DR
Cruller is a heavily stripped-down fork of the last Zig-based Bun release, ported to vanilla Zig 0.16 and focused purely on running already-built JavaScript servers in production. It keeps JavaScriptCore, Bun.serve, HTTP/1–3, WebSockets, fetch, streams, and the module resolver, but removes dev tooling like the package manager, bundler, TypeScript, test runner, and CLI extras. The result is an embeddable, smaller runtime (~18% size reduction, similar performance) aimed at Zig-based systems and single-binary deployments, not a Bun replacement.

---

### Comment pulse

- History pruning is a major concern → loses authorship, blame, and clarity for licensing; some insist this alone can scare contributors—counterpoint: author frames it as a new project, not a fork.  

- Clarification: Cruller is a production-only subset of old Bun → development still uses full Bun; this port runs on upstream Zig instead of Bun’s patched compiler.  

- Several devs reject differing dev/prod runtimes → fear subtle prod-only bugs; others see value in a tiny, embeddable JS runtime and single static binary for Zig apps.  

---

### LLM perspective

- View: Technically modest but strategically smart: preserve useful Bun runtime bits as a lean, Zig-native deployment engine instead of recreating a full platform.  

- Impact: Zig ecosystem gains a first-class JS runtime component, especially attractive for embedding, microservices, and infra tooling that already uses Zig.  

- Watch next: Native Zig I/O replacing C libs, plugin architecture (HTTP/QUIC/ZMQ), and evidence that dev/prod divergence doesn’t cause hard-to-debug production issues.
