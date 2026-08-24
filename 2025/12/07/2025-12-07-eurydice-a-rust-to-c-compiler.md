# Eurydice: a Rust to C compiler

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46178442) | Link: https://jonathan.protzenko.fr/2025/10/28/eurydice.html

### TL;DR

Eurydice compiles a supported Rust subset into readable C so libraries can adopt Rust while retaining legacy, embedded, or C-only consumers from one authoritative codebase. It translates Charon’s MIR representation through KaRaMeL and roughly 30 OCaml nanopasses, handling monomorphization, tagged unions, control-flow reconstruction, value-semantic arrays, and C evaluation order. Output targets C11/C++20 or C++17, but limitations include nonidentical layouts, strict-aliasing violations, platform-specific configuration, and manual placement of specialized code. Commenters value C as a durable portability layer, especially for proprietary toolchains.

### Comment pulse

- Readable generated C is unusually valuable → maintainable fallback source serves targets whose vendors provide only proprietary C compilers.
- An LLVM C backend solves a different problem → low-level reconstruction loses source structure, while embedded teams cannot build new target backends.
- Crypto deployment deserves extra scrutiny → optimizing Rust-to-C-to-machine-code paths may disturb timing properties and introduce side channels.

### LLM perspective

- View: Eurydice converts Rust adoption from an all-or-nothing migration into a managed compatibility strategy.
- Impact: Library maintainers can modernize source while shipping generated artifacts to C-bound ecosystems.
- Watch next: dyn-trait support, Charon monomorphization, standard-library coverage, layout fixes, and constant-time validation.
