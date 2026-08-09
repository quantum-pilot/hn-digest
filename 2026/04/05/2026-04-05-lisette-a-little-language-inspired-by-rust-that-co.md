# Lisette a little language inspired by Rust that compiles to Go

- Score: 252 | [HN](https://news.ycombinator.com/item?id=47646843) | Link: https://lisette.run/

### TL;DR

Lisette is an MIT-licensed language that borrows Rust-like syntax and safety while compiling to readable Go. It adds algebraic data types, exhaustive pattern matching, Hindley–Milner inference, immutable bindings, Option/Result, pipelines, lambdas, generics, and compile-time checks for nil, discarded errors, incomplete structs, visibility, and mutation. It retains Go interoperability, goroutines, channels, select, defer, panic recovery, serialization tags, and its runtime and garbage collector, with LSP support and source-mapped stack traces. HN liked the diagnostics but questioned adoption, Rust-adjacent syntax differences, two-way interop, and mismatches between Go tuples and Result semantics.

### Comment pulse

- Critics asked why not use Rust — counterpoint: Go supplies ergonomic garbage-collected concurrency, fast compilation, portability, and faster development for reference-heavy applications.
- Treating every `(T, error)` as exclusive `Result<T, error>` can misrepresent APIs such as readers returning valid bytes alongside end-of-file.
- Lisette can import Go packages, but Go cannot yet call Lisette; the author prioritizes broader package imports while targeting eventual production readiness.

### LLM perspective

- **View:** Lisette modernizes Go’s type system without abandoning its deployment model, ecosystem, or managed-memory concurrency.
- **Impact:** Go teams could adopt safer new modules incrementally only after bidirectional boundaries become reliable and unsurprising.
- **Watch next:** Package compatibility, tuple-result rules, source maps, ABI exports, dependency management, benchmarks, migration examples, and production milestones.
