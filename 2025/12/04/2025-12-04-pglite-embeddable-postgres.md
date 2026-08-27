# PGlite – Embeddable Postgres

- Score: 482 | [HN](https://news.ycombinator.com/item?id=46146133) | Link: https://pglite.dev/

### TL;DR

PGlite packages a full PostgreSQL build into under 3 MB gzipped WebAssembly for local browser and application use. It supports dynamic extensions including pgvector, reactive queries, data loading, synchronization, and live sync without requiring a database server. A maintainer reports nearly four million weekly downloads and adoption inside Firebase and Prisma development tools. Commenters were enthusiastic about browser-based development and PostgreSQL-compatible testing, while repeatedly asking for native libraries, official Go or Rust bindings, Flutter support, HTTP range-backed storage, and comparisons with SQLite.

### Comment pulse

- Developers valued matching production PostgreSQL semantics in tests instead of substituting SQLite.
- Demand extended beyond JavaScript toward Go CLIs, Rust, Flutter, React Native, and native embedding.
- Users wanted clearer guidance on when PGlite beats SQLite or DuckDB for embedded workloads.

### LLM perspective

- View: PGlite’s strongest moat is PostgreSQL compatibility at embedded-tool convenience, not merely browser novelty.
- Impact: Development tools can emulate server databases locally with fewer setup and semantic mismatches.
- Watch next: Track native bindings, protocol support, persistence benchmarks, extension coverage, and multi-runtime adoption.
