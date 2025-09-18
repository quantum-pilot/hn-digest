# Uncertain<T>

- Score: 448 | [HN](https://news.ycombinator.com/item?id=45054703) | Link: https://nshipster.com/uncertainty/

- TL;DR
  - NSHipster ports Microsoft Research’s Uncertain<T> to Swift, making uncertainty a first-class type. Comparisons return probabilistic booleans; computations form graphs evaluated via Monte Carlo sampling and SPRT, supporting many distributions and statistics. Examples include GPS distance and physics, with migration and performance guidance. HN praises the approach, notes circular GPS error is simplistic, links to particle filters and probabilistic programming/monads, asks about covariance (handled via shared sampling), and cites hardware (Signaloid) and Haskell/Python libraries as related work.

- Comment pulse
  - Circular GPS error is simplistic → multipath/sensor fusion dominate; real systems use particle filters. — counterpoint: fine under open-sky, long fixes.
  - Sampling-based types compose → shared leaf sampling yields covariance “for free”; echoes probability monads/probabilistic programming; autodiff/compute graphs generalize.
  - Hardware and tools are emerging → Signaloid propagates sample sets in silicon; Haskell monad-bayes and Python gvar show language-level precedents.

- LLM perspective
  - View: First-class uncertainty types with lazy sampling improve correctness and UX, but require careful modeling and reproducibility controls.
  - Impact: Mobile/location apps, robotics, and simulation benefit; QA adopts probabilistic assertions; perf and energy budgets must include sampling costs.
  - Watch next: Benchmarks vs EKF/particle filters; explicit covariance APIs; deterministic seeding; Swift Numerics integration; profiling guidance for iOS.
