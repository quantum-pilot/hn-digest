# What is a manifold?

- Score: 346 | [HN](https://news.ycombinator.com/item?id=45809193) | Link: https://www.quantamagazine.org/what-is-a-manifold-20251103/

TL;DR
Quanta’s explainer traces manifolds from Riemann’s 1854 vision to today’s toolkit: spaces that look Euclidean locally, stitched by charts/atlases to do calculus intrinsically. Examples (circle vs figure eight; sphere vs double cone; double pendulum’s torus) illustrate “locally flat, globally curved.” Manifolds unify geometry, dynamics and physics, underpinning general relativity’s spacetime and modern data/robotics modeling. HN readers swap textbook paths (Lee/Tu), ask for deeper atlas treatment, debate the ML “manifold hypothesis” and ReLU smoothness, and note spacetime is pseudo‑Riemannian/Minkowski, not Riemannian.

Comment pulse
- Best intros: John M. Lee or Loring Tu → Lee is comprehensive; Tu gentler; some prefer Jeffrey M. Lee for rigor.
- Good history; thin on atlases and examples → Readers wanted chart transitions; double-pendulum torus vs [0,2π)^2; spacetime is pseudo-Riemannian, not Riemannian — counterpoint: accessible audience.
- Data lie on manifolds? → Often assumed; atlases rarely used; ReLU breaks smoothness; manifold+noise common — counterpoint: smooth activations, information geometry show promise.

LLM perspective
- View: Focus on intrinsic definitions and transition maps; practice with spheres, tori, and the double pendulum’s torus configuration space.
- Impact: Data workflows: estimate intrinsic dimension and curvature before applying manifold learning; choose smooth activations if continuity matters.
- Watch next: Benchmarks of ReLU vs swish on manifold recovery; diffusion maps/Isomap releases; updated Lee/Tu editions clarifying atlases and pseudo-Riemannian geometry.
