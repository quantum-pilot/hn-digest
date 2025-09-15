# Cognitive load is what matters

- Score: 1582 | [HN](https://news.ycombinator.com/item?id=45074248) | Link: https://github.com/zakirullin/cognitive-load

- TL;DR
  - The piece argues that extraneous cognitive load—not patterns or tools—drives most software pain. Prefer deep modules with simple interfaces, composition over inheritance, early returns and named intermediates, monolith-first, self-describing errors, light dependencies, and frameworks at the edges. Beware shallow microservices, over-layered architecture, and feature bloat. HN largely agrees but notes simplicity is audience-relative; team conventions and low ego matter. Others urge delaying abstraction until patterns recur and accepting messy business logic, isolating cleanliness where it counts. Reducing cognitive load is an ongoing, skillful tradeoff.

- Comment pulse
  - Simplicity is subjective → shared conventions and low-ego teams make code feel simple — counterpoint: named intermediates/early returns can obscure control flow for some.
  - Delay DRY/abstraction → duplicate until the third time; refactor when change pain appears; measure “difficulty to change,” not line counts.
  - Business logic is muddy → abstractions decay; isolate clean, reusable infrastructure, accept conditional-rich domains; Big Ball of Mud is common.

- LLM perspective
  - View: Treat cognitive load as a metric: time-to-first-PR, onboarding confusion minutes, steps to reproduce bugs, cross-file hops per fix.
  - Impact: Favors monolith-first and deep modules; reduces dependency churn; benefits QA, new hires, and incident response.
  - Watch next: Tools that visualize cognitive load: call-graph depth, module fan-in/out, microservice hop counts; case studies comparing deep vs. shallow designs.
