# Expert: LSP for Elixir

- Score: 241 | [HN](https://news.ycombinator.com/item?id=45057322) | Link: https://github.com/elixir-lang/expert

TL;DR
Expert is the new official Elixir Language Server, aiming to unify prior LSP efforts (ElixirLS, Lexical, next‑ls) after a 2024 collaboration. It ships binaries, nightly builds, and can be built from source with Zig 0.14.1. Architecture emphasizes Elixir version compatibility and isolating project namespaces to avoid conflicts, targeting fewer compiler‑induced slowdowns seen in older servers. HN discussion welcomes consolidation and long‑term tooling, debates the “Expert” name, and notes there wasn’t an official LSP before—hopes are high for performance and stability.

Comment pulse
- This is the collaborative successor to ElixirLS/Lexical/next-ls → 2024 initiative to align on one LSP reduces fragmentation — counterpoint: multiple LSPs may still coexist.
- Architecture praised → version-compatibility and project namespace isolation aim to prevent conflicts and plugin crashes.
- Performance hopes → prior servers bogged down when the compiler slowed; users expect Expert to decouple and stay responsive.

LLM perspective
- View: Official LSP reduces vendor/editor divergence; expect a single extension path across VS Code, Neovim, JetBrains.
- Impact: Elixir teams get predictable refactors, go‑to‑definition, and diagnostics across versions; tool authors target one protocol behavior.
- Watch next: Publish benchmarks versus ElixirLS/Lexical, harden version matrix, migration guides for editor plugins, and release cadence beyond nightlies.
