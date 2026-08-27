# Pyrefly: Python type checker and language server in Rust

- Score: 180 | [HN](https://news.ycombinator.com/item?id=45579275) | Link: https://pyrefly.org/?featured_on=talkpython

### TL;DR

Pyrefly presents itself as a Rust-based Python type checker and language server with fast checking, autocomplete, immediate diagnostics, a VS Code extension, and a claimed throughput above 1.85 million lines per second on Meta infrastructure. The frozen page offers little benchmark detail, and its comparison values appear unrendered. Commenters testing Pyrefly, Ty, Zuban, and Pyright reported uneven startup speed, autocomplete, diagnostics, and package handling. A Pyrefly developer acknowledged several gaps, linked planned fixes, and described the product as alpha-stage.

### Comment pulse

- Users valued speed but said IDE completeness, low false positives, and effortless integration matter more than headline benchmarks.
- Reports varied by project, with missing unreachable-code warnings, module completion problems, and confusion around third-party annotations.

### LLM perspective

- View: Pyrefly’s compelling performance pitch remains insufficiently evidenced by this partially rendered landing page.
- Impact: Python teams gain another promising option, but migration costs rise when editor behavior trails mature tools.
- Watch next: Startup latency, diagnostic parity, autocomplete reliability, and transparent reproducible benchmarks.
