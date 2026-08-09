# The simple geometry behind any road

- Score: 120 | [HN](https://news.ycombinator.com/item?id=47788207) | Link: https://sandboxspirit.com/blog/simple-geometry-of-roads/

### TL;DR

For procedural game roads, the author represents road cross-sections as profiles and connects matching endpoints with straight segments plus circular arcs. A two-line fillet supplies tangent continuity when profile continuation lines intersect; lateral shifts use a midpoint profile sampled from a cubic Hermite spline, splitting an S-curve into two solvable pieces. Special orientations receive simpler constructions, while impossible placements are prevented by editor constraints. This keeps parallel road edges exact and computation constant-time. Commenters warn that real roads use clothoids to vary curvature smoothly, avoiding instantaneous lateral-force changes.

### Comment pulse

- Clothoid advocates prioritize continuous curvature and jerk limits for believable vehicle dynamics, especially railways and racing.
- The author notes offset clothoids are not clothoids and proposes approximating them with sequences of shrinking-radius arcs.
- Arc-and-line geometry suits visual generation — counterpoint: elevation, banking, acceleration, and physical comfort require a richer 3D model.

### LLM perspective

- Separate render geometry from vehicle dynamics so visual simplicity does not dictate force simulation.
- Validate tangent, curvature, width, and self-intersection invariants across randomized profile pairs.
- Intersections add the next complexity: multiple profile strips must be trimmed and stitched consistently.
