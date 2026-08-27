# Hypothesis: Property-Based Testing for Python

- Score: 223 | [HN](https://news.ycombinator.com/item?id=45818562) | Link: https://hypothesis.readthedocs.io/en/latest/

### TL;DR

Hypothesis is a Python library for property-based testing: developers describe valid input ranges and invariants, then the library generates examples, including difficult edge cases. Discussion emphasized that useful properties need not require a second implementation; tests can check round trips, idempotence, ordering independence, bounds, permitted exceptions, or agreement with a simpler model. Practitioners reported finding rare structural, numeric, parser, and API bugs. Adoption barriers include strategy-design skills, legacy-code complexity, runtime concerns, and teams that mistake generated tests for unreproducible randomness.

### Comment pulse

- Starting small helps: replace arbitrary fixtures with generated values, then add invariants as domain understanding grows.
- Found counterexamples should become regression tests; convenient subset execution can prevent slower suites from alienating developers.

### LLM perspective

- View: Property testing is most valuable when correctness has compact invariants but enormous input space.
- Impact: It shifts test design from enumerating examples toward defining boundaries and behavior.
- Watch next: Shrunk counterexamples, CI runtime, flaky-test controls, and strategy reuse across teams.
