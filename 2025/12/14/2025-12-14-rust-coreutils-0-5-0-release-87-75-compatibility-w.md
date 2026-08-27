# Rust Coreutils 0.5.0 Release: 87.75% compatibility with GNU Coreutils

- Score: 90 | [HN](https://news.ycombinator.com/item?id=46264329) | Link: https://github.com/uutils/coreutils/releases/tag/0.5.0

### TL;DR

uutils coreutils 0.5.0 passes 566 of 645 tests against GNU Coreutils 9.9, reporting 87.75% compatibility, up 1.95 percentage points from 0.4.0. The release improves Unicode-aware `fold`, checksum consolidation, `install` mode handling, large-integer `seq`, and CI support for OpenBSD, Redox, and Cygwin. However, 55 tests still fail, one errors, and 23 are skipped. Commenters dispute whether suite percentage predicts real compatibility and whether replacing mature GPL tools with incomplete MIT-licensed Rust implementations benefits users.

### Comment pulse

- Supporters say shared tests have uncovered GNU bugs and Rust limits memory faults; critics question meaningful privilege-escalation risk in these utilities.
- Ubuntu adoption draws concern as premature, while others expect remaining incompatibilities to shrink over several years.

### LLM perspective

- View: The test trend is meaningful engineering progress, not proof of drop-in equivalence across undocumented behavior.
- Impact: Distributions adopting uutils inherit portability and memory-safety gains alongside script-compatibility and licensing tradeoffs.
- Watch next: Track production regressions, failing-test severity, GNU differential testing, and distribution rollback paths.
