# PGlite – Embeddable Postgres

- Score: 482 | [HN](https://news.ycombinator.com/item?id=46146133) | Link: https://pglite.dev/

### TL;DR

PGlite packages a complete Postgres build into WebAssembly under 3 MB gzipped, enabling local browser databases with dynamic extensions such as pgvector, reactive loading, synchronization, and live queries. Its maintainer reports nearly four million weekly downloads and adoption inside Firebase and Prisma developer tooling. Discussion sees strongest value in matching production Postgres during tests or moving from embedded to networked use, while asking for official Go, Rust, Flutter, React Native, native-library, protocol, and remote-file support.

### Comment pulse

- Production fidelity drives interest → SQLite-based tests can diverge from deployed Postgres semantics.
- Language reach remains the gap → users want maintained bindings beyond JavaScript and WASM.
- Native and mobile paths are preliminary → a React Native package is experimental; a native library remains planned.

### LLM perspective

- View: Its differentiator is Postgres compatibility in-process, not merely another lightweight relational engine.
- Impact: Browser apps and CLIs can share schemas and extensions with server deployments.
- Watch next: Benchmark performance, persistence, protocol fidelity, extension coverage, and official non-JavaScript bindings.
