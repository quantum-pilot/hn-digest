# Protobuf has LSP support

- Score: 172 | [HN](https://news.ycombinator.com/item?id=49322573) | Link: https://buf.build/blog/protobuf-lsp

### TL;DR

Buf has bundled a Protobuf language server into its CLI, offering definition navigation, completion, references, semantic highlighting, and detailed diagnostics across LSP-compatible editors. It builds on Buf’s compiler work but introduces a query-driven, incremental frontend, new AST, and intermediate representation for fault-tolerant editing and large workspaces. Planned additions include automatic imports, module integration, custom-option support, field-number suggestions, and Protovalidate/CEL highlighting. Commenters disputed “first” and “modern IDE support” claims, citing older IntelliJ and LSP implementations, while defenders said those alternatives were editor-specific or not specification-complete.

### Comment pulse

- The self-congratulatory marketing tone provoked more criticism than the feature itself, prompting Buf to add a mea culpa.
- Parser reuse split opinion: compilers demand correctness while editors need recovery; Buf’s compiler foundation may reduce semantic drift.
- Protobuf rename concerns were corrected: wire compatibility follows stable field numbers and types, although JSON or text names differ.

### LLM perspective

- View: The value is shared compiler semantics and editor portability, not being the first-ever Protobuf assistance.
- Impact: Schema authors gain faster feedback across editors, especially on large modules and new Editions features.
- Watch next: Conformance tests, memory and latency benchmarks, malformed-file recovery, custom options, and compatibility-aware refactors.
