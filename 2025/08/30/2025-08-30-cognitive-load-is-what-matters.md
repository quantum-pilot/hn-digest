# Cognitive load is what matters

- Score: 1582 | [HN](https://news.ycombinator.com/item?id=45074248) | Link: https://github.com/zakirullin/cognitive-load

### TL;DR

This living software-design essay treats cognitive load as the amount a developer must hold in mind to complete a task, and urges teams to minimize complexity unrelated to the problem itself. It favors descriptive intermediate values, early returns, composition, deep modules with simple interfaces, cohesive monoliths before premature microservices, limited language cleverness, restrained DRY, framework-independent business logic, and justified abstraction layers. The author also warns that familiarity can disguise complexity and recommends using newcomers' confusion, debugging effort, and change difficulty as practical feedback.

### Comment pulse

- Commenters agreed with the goal but argued “simple” depends partly on experience, conventions, working-memory style, and project context.
- Debate centered on when abstractions reduce load versus when evolving business rules make straightforward conditional code more maintainable.

### LLM perspective

- View: Cognitive load is a strong diagnostic lens, not an objective formula that resolves every design disagreement.
- Impact: Teams can prioritize onboarding, debugging, and change cost over pattern compliance or architectural prestige.
- Watch next: Measure confusion with real maintainers and newcomers; refactor only where observed friction justifies disruption.
