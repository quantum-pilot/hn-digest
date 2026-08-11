# Show HN: I ported Tree-sitter to Go

- Score: 169 | [HN](https://news.ycombinator.com/item?id=47155597) | Link: https://github.com/odvcencio/gotreesitter

### TL;DR

`gotreesitter` is a pure-Go Tree-sitter runtime designed to use existing grammar parse tables without CGo, a C toolchain, or grammar recompilation. The project supports incremental parsing, queries, highlighting, symbol tagging, WebAssembly, and 204 of 205 tested grammars fully, with Norg partial because of its external scanner. Its own Go-source benchmarks report faster full parses and dramatically faster incremental and no-op cases than the standard CGo binding, although full parses allocate substantially more memory. The repository remains pre-1.0 and lists further C-parity and query-edge validation.

### Comment pulse

- No-CGo support appeals to Bazel tooling and Go-based forges where cross-compilation and deployment simplicity matter.
- Readers stressed this is a parser runtime, not an LSP replacement with diagnostics, navigation, refactoring, and semantic project awareness.
- Naming may change because Got already identifies another project; benchmark and compatibility claims also need independent validation across workloads.

### LLM perspective

- **View:** Removing CGo is a concrete integration win, separate from language-server functionality.
- **Impact:** Go-native parsing could simplify portable editors, analyzers, build systems, and WebAssembly tools.
- **Watch next:** External parity tests, allocation reductions, scanner coverage, and stable API design.
