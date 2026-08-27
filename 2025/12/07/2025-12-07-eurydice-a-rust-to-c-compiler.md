# Eurydice: a Rust to C compiler

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46178442) | Link: https://jonathan.protzenko.fr/2025/10/28/eurydice.html

### TL;DR

Eurydice translates a supported subset of Rust into readable C or C++ for legacy and proprietary toolchains, enabling one Rust source base to target environments lacking Rust support. It lowers MIR through Charon and KaRaMeL, with passes for monomorphization, pattern matching, iterators, arrays, and evaluation order. The project is already being integrated into cryptographic-library work, but important constraints remain: manual configuration, uncertain layout equivalence, strict-aliasing violations, platform-specific post-configuration MIR, and an assumption that input code is panic-free.

### Comment pulse

- Readers distinguished readable C distribution from LLVM’s lower-level C backend output.
- Cryptographic users raised side-channel and semantic-preservation concerns around translated code.

### LLM perspective

- View: Eurydice is a compatibility bridge, not a general replacement Rust compiler.
- Impact: It could extend verified Rust implementations into otherwise unreachable legacy environments.
- Watch next: Evidence on layout fidelity, side channels, and configuration at larger project scale.
