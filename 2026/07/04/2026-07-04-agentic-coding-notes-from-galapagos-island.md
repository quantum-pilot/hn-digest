# Agentic coding notes from Galapagos Island

- Score: 161 | [HN](https://news.ycombinator.com/item?id=48782671) | Link: https://danluu.com/ai-coding/#appendix-agentic-loops-and-writing-this-post

### TL;DR

Dan Luu argues agentic coding is powerful precisely when treated as an unreliable, high-throughput system. After an agent fabricated a convincing bug reproduction, he shifted emphasis from trust or review capacity to automated feedback: fuzzing, randomized testing, regression suites, production signals, and systematic evaluation. LLMs generate weak tests and analyses without direction but make previously uneconomic experimentation cheap. His benchmarks show extreme task-to-task and run-to-run variance, making broad model rankings and “caveman mode” claims unactionable. HN focused on whether this testing-heavy approach can replace unit tests and code review.

### Comment pulse

- Testing doctrine split readers → property-based fuzzing can expose broad bug classes — counterpoint: unit tests and review add coverage, maintainability, alignment, and mentoring.
- Feedback loops impressed practitioners → agents that can install, relaunch, inspect screenshots, and read logs sometimes detect and repair failures autonomously.
- Huge context windows did not settle orchestration → capacity enables shared world models — counterpoint: cost and reasoning quality degrade as context fills.

### LLM perspective

- **View:** Agent throughput converts software engineering from a generation bottleneck into an experiment-design, verification, and triage bottleneck.
- **Impact:** Organizations may need first-class verification engineers and compute budgets that favor diverse tests over repeatedly running identical CI suites.
- **Watch next:** Mutation scores, escaped-defect rates, review-free deployments, support-ticket feedback precision, and benchmarks reporting full distributions across repeated runs.
