# F*: A general-purpose proof-oriented programming language

- Score: 146 | [HN](https://news.ycombinator.com/item?id=49143925) | Link: https://fstar-lang.org/

### TL;DR

F* combines dependent types, SMT-backed proof automation, effects, and embedded verification languages for high-assurance programming. Low* compiles verified low-level code to C; Vale targets assembly; Steel and Pulse support concurrent separation logic. Its research lineage has produced verified cryptography, TLS and QUIC components, secure parsers, sandboxes, allocators, protocol models, and Rust verification workflows, with emerging AI-assisted proof synthesis. HN saw real industrial value, especially incremental migration around C, but criticized the site for burying syntax, tutorials, and a concise explanation of when developers should choose the language.

### Comment pulse

- New-language visitors wanted syntax and purpose immediately; others preferred memory model, type system, targets, and use cases before surface notation.
- F*’s industry case rests on deployed verified cryptography and Windows parsing hardening, not merely academic theorem-proving demonstrations.
- Incremental calls into existing C make adoption practical, though commenters wanted clearer explanation of assumptions around unported external functions.

### LLM perspective

- View: F* is best understood as a verification platform with multiple domain-specific layers, not simply a functional language with proofs.
- Impact: Security-critical teams can move assurance closer to executable implementations while extracting efficient C, assembly, WebAssembly, OCaml, or Rust paths.
- Watch next: Track tutorial discoverability, proof-maintenance cost, extraction performance, trusted computing base size, and adoption beyond cryptography and systems research.
