# Hypothesis: Property-Based Testing for Python

- Score: 223 | [HN](https://news.ycombinator.com/item?id=45818562) | Link: https://hypothesis.readthedocs.io/en/latest/

- TL;DR
    - Hypothesis is a Python library for property-based testing: you state invariants, and it generates diverse (often nasty) inputs to try to break them. The discussion praises how PBT exposes rare edge cases, shares pragmatic patterns (roundtrips, idempotency, model-vs-optimized checks), and notes adoption hurdles around “non-deterministic tests.” Performance concerns are manageable by scoping runs and promoting found counterexamples to deterministic regression tests. Tools like Schemathesis (APIs) and Approval Tests help apply PBT to legacy or spec-driven contexts.

- Comment pulse
    - PBT finds “unknown unknowns” → random inputs exposed 25th-item and negative-sqrt bugs; overnight runs built confidence via millions of trials.
    - Nondeterminism/perf are tractable → run subsets locally, long runs in CI; teammates resist randomness — counterpoint: codify counterexamples as deterministic regression tests.
    - No oracle required → assert properties (sortedness, multiplicity, idempotency, roundtrips) or compare to a slow model; Schemathesis/Approval Tests extend to APIs/legacy.

- LLM perspective
    - View: Start with simple properties on existing unit tests; expand strategies as understanding matures.
    - Impact: More robust boundaries and clearer input contracts; faster discovery of third‑party and legacy defects.
    - Watch next: CI seeds and failure replay, API schema fuzzing coverage, property libraries for common domains.
