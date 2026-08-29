# Hilariously fast volume computation with the divergence theorem (2018)

- Score: 256 | [HN](https://news.ycombinator.com/item?id=49476143) | Link: https://alyssarosenzweig.ca/blog/hilariously-fast-volume-computation-with-the-divergence-theorem.html

### TL;DR

For a simple, closed, consistently oriented triangular mesh, the divergence theorem converts volume from a triple integral over the solid into a sum over its surface triangles. Choosing the vector field `(x,0,0)` reduces each face’s contribution to its x-directed area term multiplied by the triangle’s average x-coordinate. The resulting algorithm is linear in triangle count and requires about 11 floating-point operations per face. Commenters identify it as a known three-dimensional analogue of signed-area and shoelace formulas, not a novel result.

### Comment pulse

- Geometric explanations recast the formula as summing signed projected prisms or origin-based tetrahedra, with cancellation removing excess volume.
- Earlier work computed volume, centroid, moments, and inertia similarly; generalized Stokes reasoning extends the technique beyond scalar volume.
- Readers stressed validating closure and orientation before trusting output, while questioning whether disjoint components or holes violate simplicity.

### LLM perspective

- View: The derivation’s value is pedagogical: sophisticated calculus collapses into a tiny, auditable per-triangle computation.
- Impact: Geometry software can compute exact mesh volume faster and more accurately than voxel sampling under valid preconditions.
- Watch next: Benchmark numerical stability, degenerate faces, large coordinates, inconsistent winding, holes, and parallel implementations.
