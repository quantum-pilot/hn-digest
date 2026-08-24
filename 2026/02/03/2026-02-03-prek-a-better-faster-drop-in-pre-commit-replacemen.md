# Prek: A better, faster, drop-in pre-commit replacement, engineered in Rust

- Score: 176 | [HN](https://news.ycombinator.com/item?id=46873138) | Link: https://github.com/j178/prek

### TL;DR

Prek is an MIT-licensed Rust reimplementation of the Python-based pre-commit framework, designed as a mostly drop-in replacement for existing configurations and hooks. It ships as a standalone binary, shares toolchains between hooks, installs independent repositories concurrently, supports parallel execution, uses uv for Python environments and includes Rust-native common hooks. The project claims multiple-times faster execution and half the disk use, while adding monorepo support and targeted run options. Some languages lack full parity, and commenters debate whether commit-time hooks are the right workflow at all.

### Comment pulse

- Supporters value compatibility with pre-commit’s ecosystem and the ability to reuse identical checks locally and in CI.
- Critics prefer background or push-time checks, arguing commits should remain instantaneous and installation should be separate from lint execution.
- Competing designs emphasize WASI sandboxing or simpler hook runners, exposing tradeoffs beyond raw Rust speed.

### LLM perspective

- View: Compatibility lowers migration cost, but also inherits pre-commit’s architectural constraints and supply-chain surface.
- Impact: Existing users gain speed and easier setup without rewriting configurations; greenfield teams face a broader workflow choice.
- Watch next: Independent benchmarks, remaining language parity and reliability across large polyglot repositories and CI systems.
