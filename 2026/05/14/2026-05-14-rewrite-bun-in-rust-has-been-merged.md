# Rewrite Bun in Rust has been merged

- Score: 465 | [HN](https://news.ycombinator.com/item?id=48132488) | Link: https://github.com/oven-sh/bun/pull/30412

### TL;DR

Bun merged a Zig-to-Rust port spanning 6,755 commits, 2,188 files, and roughly one million added lines. Maintainer Jarred Sumner says it preserves the architecture, passes the existing cross-platform test suite, fixes leaks and flaky tests, shrinks binaries by 3–8 MB, and benchmarks from neutral to faster. It remains canary-only pending optimization and cleanup. HN questioned the advertised speed of the rewrite, preparation effort, reproducibility, and more than 10,000 unsafe blocks; defenders noted the prior codebase was similarly sized and Rust still converts many use-after-free and cleanup bugs into compiler errors.

### Comment pulse

- Skeptics suspect substantial hidden preparation behind the claimed one-week port — counterpoint: a detailed 622-line mapping guide is small beside million-line output.
- Searching found 10,428 unsafe blocks across 736 files; supporters valued Rust’s explicit audit surface despite incomplete memory-safety gains.
- Readers requested the promised methodology, customer-equivalent cost, deterministic translation details, side-by-side testing, fuzzing, and a cautious stable rollout.

### LLM perspective

- View: Passing legacy tests establishes compatibility, not semantic equivalence or maintainability after a mechanically assisted million-line port.
- Impact: Bun’s team gains compiler enforcement while inheriting a vast review burden around unsafe code and foreign-runtime boundaries.
- Watch next: Blog methodology, canary failures, performance distributions, differential tests, production shadowing, unsafe reduction, contributor velocity, and stable-release timing.
