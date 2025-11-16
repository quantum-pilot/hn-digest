# Spec-Driven Development: The Waterfall Strikes Back

- Score: 200 | [HN](https://news.ycombinator.com/item?id=45935763) | Link: https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html

- TL;DR
  - The essay argues Spec-Driven Development resurrects Waterfall: lengthy Markdown specs, duplicated review, and brittle “plans” that agents often ignore—slowing teams, especially on mature codebases. Instead, split work into tiny, testable increments and steer agents with natural-language goals, fast feedback, and plan-mode; the author built a 3D tool this way in ~10 hours. HN replies split: some praise upfront specs and acceptance criteria (per-ticket Agile), others treat specs as LLM context plus tests to “ground” outputs, while skeptics report SDD’s overhead and stochastic, “unreliable compiler” behavior.

- Comment pulse
  - Upfront planning/spec per ticket improves flow and clarifies dependencies; at this scope it’s just good Agile practice, not Waterfall.
  - Specs as LLM context plus acceptance tests ‘ground’ agents; treat LLMs like junior devs with oversight — counterpoint: still feels waterfall unless iterations are fast/cheap.
  - Critics report heavy, slow SDD; stochastic “unreliable compiler” requires double review; lack of quick end-to-end feedback derails progress on small tools.

- LLM perspective
  - View: Use SDD selectively; prefer small, iterative tasks with minimal specs, strong acceptance tests, and agent plan-mode.
  - Impact: PMs and senior devs shift to curating context and tests; fewer docs, more executable specifications and CI checks.
  - Watch next: Benchmarks of SDD vs iterative (throughput, defects, review time); visual grounding tools; agents that update specs/tests automatically.
