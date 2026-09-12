# Measuring the sloppiness of code

- Score: 259 | [HN](https://news.ycombinator.com/item?id=49658311) | Link: https://earendil.com/posts/measuring-code-sloppiness/

### TL;DR

The essay argues that functional correctness does not capture AI-generated code’s duplication, needless abstraction, or accumulated architectural damage. It finds model-based judging unreliable and human review difficult to scale. As proxies, it highlights line-count growth plus SlopCodeBench’s verbosity and erosion metrics; reported agent code scored roughly twice established repositories on both averages. In iterative tasks with erased context, state-of-the-art models achieved a 0% strict pass rate. The author stresses that these metrics remain heuristic and vulnerable to optimization.

### Comment pulse

- Global structure matters most → Local duplication is repairable, while poor boundaries and layering require expensive system-wide refactoring.
- Repository results vary → One commenter’s agent-heavy Python project scored low verbosity but intermediate erosion.
- Human understanding remains consequential → Software also distributes a shared mental model across teams, not only executable behavior.

### LLM perspective

- View: Sloppiness measurement is valuable as an alarm, not a single objective that agents should optimize directly.
- Impact: Teams scaling generation without architecture controls may gain features while losing comprehension and change safety.
- Watch next: Cross-language replication, coupledness and cohesion metrics, longitudinal benchmarks, and correlations with production failures.
