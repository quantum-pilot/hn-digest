# Expert: LSP for Elixir

- Score: 241 | [HN](https://news.ycombinator.com/item?id=45057322) | Link: https://github.com/elixir-lang/expert

- TL;DR
  - Expert is Elixir’s new, official Language Server, born from last year’s cross-project collaboration (ElixirLS, Lexical, next‑ls). Its architecture isolates the server from project namespaces and supports multiple Elixir/OTP versions to reduce clashes and performance regressions. Binaries and nightlies are available; source builds use Zig. HN welcomes the consolidation and long‑term tooling plan, expects smoother performance than ElixirLS, debates the “Expert” name, and notes this is the first truly official LSP.

- Comment pulse
  - Unified, community-led tool → ElixirLS/Lexical/next‑ls maintainers converged on a vendor‑neutral server; day‑to‑day isn’t core‑team/Dashbit‑run.
  - Isolation and compatibility → Namespacing and multi‑version support aim to prevent module collisions and work across varied Elixir/OTP matrices.
  - Performance hopes → Users expect fewer slowdowns than ElixirLS — counterpoint: earlier LSPs weren’t official; this is the first.

- LLM perspective
  - View: Official standardization reduces fragmentation; architecture choices suggest fewer edge-case crashes and better editor parity.
  - Impact: Most Elixir devs → simpler setup, consistent features; plugin authors consolidate around one protocol surface.
  - Watch next: Independent benchmarks vs ElixirLS/Lexical, VS Code/Neovim integration updates, migration guides and OTP version-matrix support.
