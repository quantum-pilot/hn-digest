# Box3D, an open source 3D physics engine

- Score: 395 | [HN](https://news.ycombinator.com/item?id=48745445) | Link: https://box2d.org/posts/2026/06/announcing-box3d/

### TL;DR

Box3D is Erin Catto’s open-source 3D physics engine, derived from Box2D and remaining close to its C17, C API architecture. Built for The Legend of California after Unreal’s Chaos mishandled gyroscopic motion, falling trees, and large entity counts, it adds mesh, height-field, compound collisions, CCD, SIMD, multithreading, large-world doubles, determinism, and replay. Already used by several projects, it remains alpha pending testing and documentation. HN welcomed a rare new entrant among free 3D engines, while highlighting simulation complexity and asking how cross-platform determinism works.

### Comment pulse

- Open-source 3D physics remains sparse → commenters placed Box3D alongside ODE, Bullet, Newton Dynamics, and Jolt, making another maintained option welcome.
- Deterministic networking matters → replay and rejecting `-ffast-math` look promising, but commenters wanted explicit guarantees across platforms and floating-point implementations.
- Mature physics is hard → collision detection, geometry decomposition, solver tuning, robustness, accuracy, and speed create deep tradeoffs even for rigid bodies.

### LLM perspective

- **View:** Box3D’s strongest differentiator is continuity: Catto can carry proven Box2D architecture and knowledge into maintained 3D infrastructure.
- **Impact:** Engine teams gain a focused alternative when middleware behavior, scale, or integration constraints justify owning more physics code.
- **Watch next:** v0.1 benchmarks, determinism tests, character movement, ghost-collision mitigation, joint improvements, documentation, and pull-request governance.
