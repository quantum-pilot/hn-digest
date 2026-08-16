# The mathematical beauty of hyperbezier curves

- Score: 187 | [HN](https://news.ycombinator.com/item?id=49237183) | Link: https://linebender.org/blog/hyperbezier/

### TL;DR

Raph Levien proposes “hyperbeziers,” an arc-length curve family whose curvature is a linear numerator over a quadratic denominator raised to 1.5. It approximates ordinary cubic Béziers at modest angles while exactly containing circles and Euler spirals, naturally modeling hyperbolas, and visually matching superellipses and elastica with smoother, often monotonic curvature. The family is closed under subdivision but permits at most one inflection. Discussion admired the curve quality yet questioned computational cost, unmoving control regions, spline integration, and whether better curvature outweighs Béziers’ direct, intuitive control.

### Comment pulse

- Hyperbeziers improve high-tension and conic-like shapes → counterpoint: control points can lose influence in extreme regions, weakening interactive predictability.
- Heavier evaluation may be acceptable → Béziers also hide costly inverse arc-length and fitting problems, while hyperbeziers subdivide cleanly.
- Curve family and spline behavior differ → local support depends on continuity choices; designers may trade G2 smoothness against G1 control.

### LLM perspective

- View: The proposal’s mathematical breadth is compelling, but an editing primitive succeeds through control ergonomics as much as curve quality.
- Impact: Font and vector-tool designers might use fewer segments for smoother forms, accepting slightly heavier evaluation.
- Watch next: Build a G2 spline, benchmark rendering and fitting, and test control mappings with working designers.
