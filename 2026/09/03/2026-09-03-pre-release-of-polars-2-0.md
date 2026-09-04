# Pre-Release of Polars 2.0

- Score: 394 | [HN](https://news.ycombinator.com/item?id=49546753) | Link: https://pola.rs/posts/announcing-polars-2/

### TL;DR

Polars 2.0 RC1 is positioned as a compatibility cleanup rather than a feature-heavy release. LazyFrame collection now defaults to the streaming engine, which the project expects to deliver roughly fivefold aggregate speed and major memory savings, but some operations no longer preserve row order unless requested. The release also rejects lossy `is_in` coercion, errors on unequal horizontal concatenation without explicit extension, replaces ambiguous casts with dedicated methods, and improves migration errors. Further engine, I/O, SQL, and planner work is planned for later 2.x releases.

### Comment pulse

- Commenters welcomed strictness and semantic-version discipline, though some described frequent minor-version deprecations as costly.
- Row-order changes split opinion between scientific reproducibility concerns and the view that ordering should always be explicit.
- Supporters saw the release’s deliberately limited scope as evidence of a mature project.

### LLM perspective

- View: Predictable failure is preferable to silent coercion, but changed ordering deserves prominent migration treatment.
- Impact: Streaming-by-default may cut memory and runtime while exposing pipelines that accidentally relied on implicit order.
- Watch next: Release-candidate feedback on regressions, deterministic workflows, and whether projected streaming gains hold broadly.
