# Fast calculation of the distance to cubic Bezier curves on the GPU

- Score: 119 | [HN](https://news.ycombinator.com/item?id=45626037) | Link: https://blog.pkh.me/p/46-fast-calculation-of-the-distance-to-cubic-bezier-curves-on-the-gpu.html

- TL;DR
  - The author computes per-pixel distance to cubic Bézier curves on the GPU by minimizing squared distance; its derivative is a quintic in t∈[0,1]. They implement GLSL coefficient setup and root-finding, compare Aberth–Ehrlich (complex roots, finicky) with Cem Yuksel’s derivative-cascade + Newton-bisection (ordered roots, robust), and find the latter ~3× faster. An ITP variant underperforms here; quadratic solvers on GPUs remain numerically delicate. Future work: signed distance for curve chains. HN discusses sign-only fills, subdivision-seeded Newton, and classic Bernstein/B‑spline approaches.

- Comment pulse
  - Only need sign for path fills → implicit inside/outside test avoids distance and quintic roots; cheap for rational cubics — counterpoint: lighting needs true distance.
  - Subdivision + nearest control point seeding → gives near-optimal Newton initial t; few iterations, SIMD-friendly; but convergence guarantees on chosen subcurve remain unclear.
  - Prefer basics over heavy solvers → Bernstein/B‑spline formulations and classic root-finders may be simpler/faster; others adopt Yuksel’s method in libraries like kurbo/polycool.

- LLM perspective
  - View: Bracketing via derivative cascades plus Newton-bisection is a sweet spot for GLSL: predictable, branch-light, avoids complex arithmetic.
  - Impact: Enables fast vector SDFs and crisp zoomable text/shapes; game engines and renderers can port a degree-5, [0,1]-clipped solver.
  - Watch next: Publish cross-GPU benchmarks; stress-test quadratic numerics; compare against subdivision-seeded Newton; integrate sign-only fill paths and multi-curve signed fields.
