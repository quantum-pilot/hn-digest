# Folks, we have the best π

- Score: 325 | [HN](https://news.ycombinator.com/item?id=45246953) | Link: https://lcamtuf.substack.com/p/folks-we-have-the-best

- TL;DR
  - The post explores Lp metrics, defining πp as circumference/diameter measured with the same metric. Taxicab (p=1) and Chebyshev (p=∞) give π=4; Euclidean (p=2) gives ≈3.14159, and πp grows as p moves away from 2. Adler–Tanton prove πp is minimized uniquely at p=2. The author sketches numerical polygon approximations; for p<1 the “distance” ceases to be a metric and unit “circles” become concave, with πp blowing up as p→0. HN ties this to inner-product symmetry and algorithmic consequences.

- Comment pulse
  - Euclidean norm is uniquely tied to inner products → rotation/reflection invariance and the parallelogram law; underpins SVD, K‑means, Gaussian likelihoods.
  - Computing πp → arc-length integral of the Lp quarter circle; numeric polygon approximation works; calculus shows global minimum at p=2 — counterpoint: heavy derivation omitted.
  - p→0 behavior → |x|^p→1 for x≠0; distances collapse to {0,1,∞}; triangle inequality fails; circles concave; πp diverges.

- LLM perspective
  - View: Reframing π via Lp arc length spotlights L2 as uniquely efficient for perimeter under fixed diameter in normed planes.
  - Impact: Norm choice shapes algorithm behavior and constants: clustering, regularization, robustness, and geometry-aware path planning may prefer L2 for minimal perimeters.
  - Watch next: Generalize to higher dimensions: Lp surface-area/volume ratios, isoperimetric constants, geodesics; publish reference implementations and benchmarks for πp estimation.
