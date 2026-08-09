# It's OK to compare floating-points for equality

- Score: 174 | [HN](https://news.ycombinator.com/item?id=47767398) | Link: https://lisyarus.github.io/blog/posts/its-ok-to-compare-floating-points-for-equality.html

### TL;DR

The post argues that exact floating-point equality is safer than a guessed epsilon: IEEE 754 arithmetic is deterministic, while approximate equality is non-transitive, inconsistent across subsystems, and masks a modeling or algorithmic error. Examples replace tolerances with explicit state, exact zero checks, stable formulations, fixed-grid geometry, or domain-derived acceptance thresholds; epsilons remain useful for visualization and tests when justified. Hacker News broadly agreed that machine epsilon is not a universal tolerance, but objected that physical measurements and production geometry fundamentally carry uncertainty, requiring scale-aware, often accumulating tolerances rather than exactness.

### Comment pulse

- Physical quantities begin with measurement uncertainty — counterpoint: the article concerns floating-point error, not every domain’s semantic notion of equality.
- Geometry-kernel veterans described per-object tolerances and repeated expansion as production necessities when upstream meshes carry irreducible ambiguity.
- For assertions, commenters favored caller-specified error models combining relative and absolute tolerance; raw EPSILON becomes exact equality above modest magnitudes.

### LLM perspective

- **View:** Equality is a semantic choice: use exact comparison for discrete invariants and explicit tolerances for uncertain quantities.
- **Impact:** Replacing guessed epsilons can expose flawed state models and improve numerical guarantees, but demands domain-specific analysis.
- **Watch next:** Scale handling, signed zero, NaN behavior, compiler consistency, geometry robustness, and documented provenance for every tolerance.
