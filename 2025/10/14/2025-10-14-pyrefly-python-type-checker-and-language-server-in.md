# Pyrefly: Python type checker and language server in Rust

- Score: 180 | [HN](https://news.ycombinator.com/item?id=45579275) | Link: https://pyrefly.org/?featured_on=talkpython

- TL;DR
  - Meta’s Pyrefly is a Rust-based Python type checker and language server claiming 1.85M LOC/s and fast IDE features, plus a VSCode extension. HN testers report uneven startup speed and missing niceties versus BasedPyright, with developers acknowledging alpha status and opening issues. Comparisons with Astral’s Ty and Zuban note raw speed but limited features; combining LSPs is suggested. Some see inaccurate diagnostics with untyped or typeshed-backed libraries. Consensus: adoption hinges on effortless integration, low noise, and parity on everyday editor workflows.

- Comment pulse
  - Ergonomics over raw speed → Tools must be fast, low-friction, low-noise (ruff/uv standard); BasedPyright wins by “disappearing” UX — counterpoint: Pyrefly devs are shipping fixes, request repros.
  - Feature/diagnostics gaps → Unreachable-code checks missing, module autocomplete flaky, go-to-declaration absent; diagnostics noisy with untyped packages and typeshed mismatches (e.g., asyncio); __slots__ confusions.
  - Positioning → Ty is a type-checker-only LSP; editors can combine servers. Some plan to wait; others want faster pyright replacements now.

- LLM perspective
  - View: Rust type-checkers are converging; UX and correctness will trump raw throughput.
  - Impact: Large repos and AI-assisted editors benefit most; typeshed maintainers face more scrutiny.
  - Watch next: Startup latency, false-positive rate, go-to-declaration/unreachable checks, multi-LSP workflows, real-world conformance benchmarks.
