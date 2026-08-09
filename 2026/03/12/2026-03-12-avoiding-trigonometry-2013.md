# Avoiding Trigonometry (2013)

- Score: 202 | [HN](https://news.ycombinator.com/item?id=47348192) | Link: https://iquilezles.org/articles/noacos/

### TL;DR

In 3D graphics, the author argues that algorithms accepting and returning vectors should usually stay in vector space. An example aligns one direction to another by replacing an axis-angle path—cross product, normalization, acos, then sin and cos—with a matrix derived directly from dot and cross products. The result removes inverse trigonometry, clamping, normalization, and square roots, improving performance and numerical stability. HN largely appreciated the geometry, while debating whether intuitive axis-angle APIs and maintainability outweigh optimization outside hot or fragile code.

### Comment pulse

- Dot and cross products already encode cosine and sine → converting to an angle and immediately back discards structure.
- Trig-heavy transforms can hide rare NaNs, degeneracies, and composition bugs → vector formulations often fail more visibly.
- Convenience APIs remain valuable → counterpoint: abstraction penalties become material in per-frame hot paths and precision-sensitive engines.

### LLM perspective

- **View:** Choose representations matching the domain: angles at boundaries, vectors and matrices inside geometry.
- **Impact:** Graphics and physics code can use fewer transcendentals and handle fewer degenerate regions.
- **Watch next:** Strict-versus-fast-math benchmarks, singular alignment cases, and comparisons with quaternions or Householder reflections.
