# Ty: A fast Python type checker and LSP

- Score: 209 | [HN](https://news.ycombinator.com/item?id=46294289) | Link: https://astral.sh/blog/ty

### TL;DR

Astral has released ty, its Rust-based Python type checker and language server, in beta and now recommends it to motivated production users. Its incremental architecture selectively recomputes affected work after edits; Astral reports large speed advantages over mypy, Pyright, and Pyrefly in selected benchmarks. The tool offers cross-file diagnostics and standard language-server features under the MIT license. Stable release work still includes specification coverage, reliability fixes, and first-class support for major libraries such as Pydantic and Django, so performance claims do not imply complete compatibility.

### Comment pulse

- Readers welcome the responsiveness but warn that specification-conformance tables alone do not measure inference, diagnostics, or practical usefulness.
- Early reports include good Emacs behavior, a Cursor extension incompatibility, and continued respect for Pyright's maturity.

### LLM perspective

- View: Ty's beta makes latency its strongest differentiator, while ecosystem compatibility remains the adoption gate.
- Impact: Near-instant diagnostics could make rigorous typing feel less intrusive across very large Python projects.
- Watch next: Track stable milestones, Pydantic and Django support, crash reports, and independent correctness comparisons.
