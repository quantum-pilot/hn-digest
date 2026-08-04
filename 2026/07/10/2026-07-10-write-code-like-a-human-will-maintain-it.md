# Write code like a human will maintain it

- Score: 322 | [HN](https://news.ycombinator.com/item?id=48859701) | Link: https://unstack.io/write-code-like-a-human-will-maintain-it

### TL;DR

The author let an LLM duplicate access-control logic across entry points because each version worked. The hidden cost is feedback: generated code reads the repository, so every merged shortcut models local style, encouraging more duplication and making cleanup less reliable. HN agreed agents compound code smells but disputed why; models often ignore good abstractions even when shown them, implying an independent reimplementation bias. Responses ranged from review checklists and refactoring passes to writing critical code manually, while skeptics warned long instructions dilute compliance and machine-made abstractions can be worse.

### Comment pulse

- Repository quality is context quality → copied logic and stale comments become examples future generations imitate, creating a compounding maintenance loop.
- Review prompts provide backpressure → persistent checklists can catch recurring mistakes — counterpoint: hundreds of generic rules dilute attention and create false assurance.
- Models may duplicate despite clean examples → training priors favor familiar reimplementation and can ignore project abstractions, so human architectural judgment remains necessary.

### LLM perspective

- **View:** AI-assisted codebases are self-conditioning systems: every merge changes both the software and the examples steering subsequent generation.
- **Impact:** Outsourcing typing without retaining a human mental model converts short-term speed into delayed refactoring, review, and incident costs.
- **Watch next:** Duplication metrics, abstraction adherence, instruction-compliance tests, comment staleness, reviewer recall, periodic architecture audits, and maintainability after team handoff.
