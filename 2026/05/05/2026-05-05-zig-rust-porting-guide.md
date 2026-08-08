# Zig → Rust porting guide

- Score: 698 | [HN](https://news.ycombinator.com/item?id=48016880) | Link: https://github.com/oven-sh/bun/commit/46d3bc29f270fa881dd5730ef1549e88407701a5

### TL;DR

Bun’s experimental guide instructs agents to translate Zig files into noncompiling Rust drafts first, then make crates compile in a later phase. It prescribes exact layouts, naming, ownership, allocators, byte-oriented strings, JSC rooting, FFI safety, and performance markers while preserving Bun’s callback-driven runtime and avoiding mainstream async/I/O libraries. A Bun maintainer stressed that no rewrite is committed and the branch may be discarded; the goal is a side-by-side comparison. HN split between optimism about test-guided translation and concern that a 774,000-line generated diff is effectively unreviewable.

### Comment pulse

- Existing architecture and tests make rewrites unusually verifiable → one commenter reported an AI Postgres port passing over 95% of tests.
- Mass translation overwhelms human review → 773,950 additions cannot receive the line-by-line scrutiny nondeterministic output still requires.
- The experiment is exploratory, not a migration decision → counterpoint: unresolved production bugs make a huge speculative branch look like misplaced effort.

### LLM perspective

- **View:** The guide is less a language tutorial than a machine-readable specification of Bun’s hidden invariants.
- **Impact:** Success would shift porting effort from initial transcription toward validation, integration, and idiomatic redesign.
- **Watch next:** Test-suite parity, benchmark deltas, unsafe-code audits, review throughput, and whether maintainers retain any generated code.
