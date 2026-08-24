# Ty: A fast Python type checker and LSP

- Score: 209 | [HN](https://news.ycombinator.com/item?id=46294289) | Link: https://astral.sh/blog/ty

### TL;DR

Astral released the beta of ty, a Rust-based Python type checker and language server designed around incremental recomputation. The company reports uncached checking 10–60× faster than mypy and Pyright, plus millisecond-scale diagnostics after edits to large PyTorch files. Beyond speed, it offers intersection types, advanced narrowing, cross-file diagnostics, and standard editor navigation and refactoring features under MIT. Astral uses it internally and recommends motivated production adopters, while targeting stability next year after specification coverage, bug fixes, and first-class Pydantic and Django support.

### Comment pulse

- Pyright remains the quality benchmark; Astral acknowledges a conformance gap — counterpoint: specification tests poorly represent diagnostics, inference, and everyday usability.
- Early users valued responsive editor feedback and fewer annotation demands, but one reported a Cursor extension compatibility failure.
- Teams running both mypy and Pyright hope to consolidate once library support matures; differing errors show speed alone cannot decide migration.

### LLM perspective

- View: Incremental architecture matters more to interactive experience than headline full-repository benchmark speed.
- Impact: Fast, low-noise feedback could make continuous type checking tolerable across large Python codebases.
- Watch next: Stable milestone, Pyright parity, Pydantic and Django support, extension compatibility, diagnostic precision, and Astral’s long-term funding model.
