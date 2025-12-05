# PGlite – Embeddable Postgres

- Score: 482 | [HN](https://news.ycombinator.com/item?id=46146133) | Link: https://pglite.dev/

- TL;DR  
  - PGlite is a compact WebAssembly build of PostgreSQL that runs fully in the browser or local runtimes, under 3MB gzipped. It exposes standard Postgres features plus extensions like pgvector, adds reactive data loading and live-sync primitives, and is dual-licensed Apache/PostgreSQL. HN readers highlight uses in devtools, in-browser development servers, and CI where real Postgres semantics matter, and request native libraries, non-JS bindings, and performance/SQLite comparisons. There is also curiosity about http-vfs-style datasets and positioning PGlite versus SQLite or DuckDB for embedded workloads.

- Comment pulse  
  - Real Postgres semantics client-side → Great for tests, CI, devtools, and browser-based DB servers when production uses PostgreSQL, avoiding SQLite mismatch.  
  - Broader runtime support → Developers want official Go/Rust/Flutter bindings and native libs; — counterpoint: WASM-first design may hinder simple non-JS integration.  
  - Advanced scenarios → Interest in http-vfs-style read-only datasets, performance vs native Postgres, and using PGlite as a SQLite or DuckDB alternative.

- LLM perspective  
  - View: Browser- and CLI-embedded Postgres narrows the gap between local development stores and production databases more than SQLite-based workflows can.  
  - Impact: Makes offline-first, reactive apps with real Postgres features feasible without backend setup, benefiting SaaS, data tools, and education platforms.  
  - Watch next: Native builds, stable multi-language bindings, performance benchmarks versus SQLite/Postgres, and patterns for syncing embedded instances with central servers.
