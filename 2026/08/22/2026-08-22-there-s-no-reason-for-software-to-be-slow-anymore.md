# There's no reason for software to be slow anymore

- Score: 626 | [HN](https://news.ycombinator.com/item?id=49395628) | Link: https://danluu.com/perf-opt/

### TL;DR

The author argues coding agents collapse the human cost of performance work, making formerly specialized optimizations and workload-specific software economical. Experiments include an agent-built regex engine whose native path improved eligible representative searches about 7%, a personalized variant gaining roughly 2%, and optimized game AI where repeated rewrites became cheap. The claim is not that agents supply judgment: models overfit benchmarks, mishandle experimental design, and can introduce incorrect optimizations, so humans must define holdouts, tests, and objectives. Discussion split over how broadly this approach generalizes beyond bounded, measurable tasks.

### Comment pulse

- Optimization loops thrive when profilers, acceptance tests, and executable benchmarks provide feedback; SafeRE and a Python-to-Rust port supplied positive examples.
- Skeptics called the method familiar superoptimization and warned that noisy benchmarks, unseen workloads, allocations, and cache behavior can invalidate apparent gains.
- Network waits drew blame for perceived slowness—counterpoint: teams often add avoidable server and client delay atop unavoidable round trips.

### LLM perspective

- View: Agents change optimization economics more convincingly than optimization science; cheap iteration amplifies whatever measurement system humans provide.
- Impact: Teams can test marginal or bespoke improvements, but weak benchmarks may industrialize overfitting and maintenance burden.
- Watch next: Independent holdouts, end-to-end latency, correctness regressions, maintenance costs, diverse hardware, and comparisons against expert-optimized baselines.
