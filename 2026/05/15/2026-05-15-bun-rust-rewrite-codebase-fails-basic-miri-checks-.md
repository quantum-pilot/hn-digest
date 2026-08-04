# Bun Rust rewrite: "codebase fails basic miri checks, allows for UB in safe rust"

- Score: 352 | [HN](https://news.ycombinator.com/item?id=48150900) | Link: https://github.com/oven-sh/bun/issues/30719

### TL;DR

A Bun issue demonstrated that safe `PathString::init` erased an input slice’s lifetime, letting callers create a dangling `&[u8]`; Miri also flagged lost pointer provenance. Maintainers reproduced it, marked that API and a parallel iterator hole unsafe, documented outlives contracts across roughly 70 call sites, and added a signature regression test. The episode intensified criticism of Bun’s AI-assisted Zig-to-Rust port as unreviewed unsafe translation. HN split between treating this as a trust-breaking process failure and viewing undefined behavior as expected, repairable debt in an unpublished first-pass port.

### Comment pulse

- Deterministic translation is no panacea → c2rust-style ports preserve unsafe pointer semantics, generate unwieldy code, and can reproduce the source crash unchanged.
- Porting strategy divides reviewers → critics demand safety-first human review — counterpoint: others favor landing mechanical Rust, then using Miri and types for cleanup.
- Public scrutiny became self-defeating → signal-boosting exposed serious flaws, but low-information pile-ons overwhelmed the issue and encouraged maintainer defensiveness.

### LLM perspective

- **View:** Rust’s guarantees apply only when unsafe boundaries encode true invariants; language choice cannot substitute for proof and review.
- **Impact:** Users judge governance alongside defects; generated intermediate states can consume project trust faster than repairs restore it.
- **Watch next:** Track Miri coverage, unsafe-call reductions, audited invariants, fuzzing results, and recurrence of safe APIs permitting undefined behavior.
