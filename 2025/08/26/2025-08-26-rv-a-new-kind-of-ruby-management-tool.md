# Rv, a new kind of Ruby management tool

- Score: 333 | [HN](https://news.ycombinator.com/item?id=45023730) | Link: https://andre.arko.net/2025/08/25/rv-a-new-kind-of-ruby-management-tool/

- TL;DR
    - rv is a Rust-based “language manager” for Ruby from Bundler’s André Arko, unifying version management and gem deps. It installs precompiled Ruby 3.4 on macOS/Ubuntu in ~1s, auto-switches versions, and adds uv-inspired rvx: run/install isolated CLI tools and single-file scripts with embedded requirements. Team includes RubyGems’ Samuel Giddins and rbenv’s Sam Stephenson. HN split: Bundler already suffices vs. speed/one-tool appeal; polyglots prefer asdf/mise/Nix and ask for .tool-versions support; some fear Python-style env sprawl.

- Comment pulse
    - Bundler already isolates gems and supports inline scripts; Ruby installs aren’t painful; speed gains may be marginal — counterpoint: one tool simplifies onboarding.
    - Polyglot workflows use asdf/mise/Nix/direnv; prefer a standard like .tool-versions and rv as a backend; unclear if mise truly offers precompiled Ruby.
    - Worry: Ruby could drift toward Python-style env chaos; optimism: rv arrives later, copying uv’s clearer model and could reduce fragmentation.

- LLM perspective
    - View: If rv ships instant precompiled Rubies + isolated tool runs, it meaningfully reduces CI/dev friction beyond Bundler alone.
    - Impact: Newcomers, CI pipelines, teams standardizing fewer tools; mise/asdf could delegate Ruby to rv.
    - Watch next: Benchmarks for no-op installs, Windows/ARM/musl support, supply-chain verification of binaries, .ruby-version/.tool-versions compatibility.
