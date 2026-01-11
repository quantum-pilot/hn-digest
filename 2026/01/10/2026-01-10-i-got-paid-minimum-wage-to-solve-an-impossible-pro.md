# I got paid minimum wage to solve an impossible problem

- Score: 85 | [HN](https://news.ycombinator.com/item?id=46564618) | Link: https://tiespetersen.substack.com/p/i-got-paid-minimum-wage-to-solve

## TL;DR
A supermarket employee with a CS background tried to “optimally” sweep the floor by modeling the store as a grid, then running a simulated-annealing Traveling Salesman heuristic to minimize walking distance. The algorithm delivered a technically near-optimal but physically absurd path full of sharp turns. Adding penalties for turning produced longer but actually usable routes, revealing the real lesson: optimization quality depends entirely on the cost function. HN discussion extends this to premature micro-optimization, human-centric metrics, and real-world coverage-path planning.

---

## Comment pulse
- Choosing what to optimize → Many orgs chase technically impressive optimizations nobody needs; real constraints (requests/sec, market size) often make simple solutions sufficient.  
- Cost function ≈ human satisfaction → Shortest path isn’t best; need to encode turns, visibility of “done” areas, and human perception—harder than the search itself.  
- Heuristics as education → Playing with simulated annealing and similar tools teaches complexity intuition better than formal Big-O; opens doors to tougher problems like 3D bin packing.

---

## LLM perspective
- View: The core insight is objective design beats algorithmic cleverness; mis-specified goals scale harm in automated systems.  
- Impact: Product teams, not just ML engineers, must own and revise cost functions to reflect human outcomes, not proxy metrics.  
- Watch next: Benchmarks that include human comfort, well-being, or safety; audits of engagement-optimized systems; tools to prototype and compare objective functions.
