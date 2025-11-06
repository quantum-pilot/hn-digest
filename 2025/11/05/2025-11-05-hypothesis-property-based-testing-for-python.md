# Hypothesis: Property-Based Testing for Python

- Score: 217 | [HN](https://news.ycombinator.com/item?id=45818562) | Link: https://hypothesis.readthedocs.io/en/latest/

- TL;DR
  - Hypothesis brings property-based testing to Python: you describe invariants and it generates inputs to break them, then shrinks failures to minimal counterexamples. Commenters report it surfacing rare edge cases and boosting confidence after large randomized runs. Practical guidance: test properties (sortedness, idempotence, round-trips) instead of needing an oracle; compare against a simple reference when you have one. Manage adoption friction by seeding for reproducibility, limiting per-PR runtime, running long fuzzing nightly, and promoting found counterexamples to deterministic regression tests.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - PBT finds hidden bugs → random data and shrinking expose edge cases; overnight runs build confidence — counterpoint: bound runtime with seeds, time limits, subsets.
  - Properties over oracles → check invariants (sortedness, length, multiset equality), metamorphic laws (idempotence, symmetry, triangle inequality), or round-trips; use simple reference implementations when feasible.
  - Adoption tips → start with 'doesn’t crash' and round-trips; lift failures to regression tests; tools: Schemathesis for APIs, Approval Tests for legacy snapshots.

- LLM perspective
  - View: Treat Hypothesis as fuzzing with assertions; focus on invariants and round-trips, not full input DSLs.
  - Impact: Faster defect discovery, clearer input contracts; needs seeded runs, per-PR limits, and nightly long fuzzing.
  - Watch next: Hypothesis shrinker improvements, Schemathesis CI patterns, documented team policy for stochastic tests and promoting counterexamples to deterministic cases.
