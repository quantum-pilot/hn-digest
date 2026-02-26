# Show HN: I ported Tree-sitter to Go

- Score: 169 | [HN](https://news.ycombinator.com/item?id=47155597) | Link: https://github.com/odvcencio/gotreesitter

- TL;DR  
A pure-Go reimplementation of the Tree-sitter runtime, gotreesitter loads upstream grammar tables and runs parsing, querying, highlighting, and tagging without cgo or a C toolchain. It supports 205 languages and aggressively optimised incremental reparsing, benchmarking up to 90× faster than the standard CGo bindings for single‑byte edits and dramatically faster no-op reparses. HN discussion centers on eliminating cgo in Bazel/Gazelle and Go-based forges, clarifying Tree-sitter’s role versus LSPs, and minor naming/alternative-implementation debates.

- Comment pulse  
  - Pure-Go runtime removes cgo pain for Bazel/Gazelle and Go-based forges → simpler CI, cross-compilation, and compliance with strict no-cgo policies.  
  - Tree-sitter gives fast incremental ASTs and queries; LSPs add diagnostics, refactors, project-wide navigation—Tree-sitter can underpin, but not replace, LSPs.  
  - Naming collides with OpenBSD’s Got and others; some dismiss confusion — counterpoint: distinct branding helps long-term ecosystem adoption.

- LLM perspective  
  - View: Pure-language Tree-sitter ports standardize robust parsing as a library primitive, not a native-side afterthought.  
  - Impact: Go editors, analyzers, forges, and build tools can ship rich language intelligence without C or custom parsers.  
  - Watch next: Independent parity tests versus upstream C, WASM benchmarks, and converged APIs across Go/Rust/other ports.
