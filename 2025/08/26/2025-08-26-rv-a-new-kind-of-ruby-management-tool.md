# Rv, a new kind of Ruby management tool

- Score: 333 | [HN](https://news.ycombinator.com/item?id=45023730) | Link: https://andre.arko.net/2025/08/25/rv-a-new-kind-of-ruby-management-tool/

### TL;DR

Bundler veteran André Arko proposes `rv`, a Rust-based “language manager” combining Ruby installation, version selection, gem resolution, isolated CLI tools, and self-contained scripts, inspired by Python’s `uv`. The goal is to make commands automatically obtain the right precompiled Ruby and dependencies without a separate RVM/Bundler setup; `rvx` would run tools in isolated environments. The early implementation currently auto-switches installed versions and installs precompiled Ruby 3.4.x on macOS and Ubuntu. Commenters welcomed speed but questioned overlap with Bundler, mise, asdf, Nix, and existing script support.

### Comment pulse

- One command lowers Ruby onboarding friction → prebuilt runtimes and isolated tools remove several manual setup layers.
- Ruby already has coherent dependency management → critics saw fewer foundational problems than `uv` addressed in Python.
- Language-specific depth competes with polyglot convenience → universal managers cover more runtimes but may miss specialized workflows.

### LLM perspective

- View: `rv` is promising primarily as integration and distribution, not as proof Ruby’s existing tools are broken.
- Impact: Newcomers and automation may gain the most; established teams face migration and compatibility trade-offs.
- Watch next: Benchmark resolution, define lockfile compatibility, support shared version files, and deliver the planned tool isolation.
