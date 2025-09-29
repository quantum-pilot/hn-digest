# The AI coding trap

- Score: 424 | [HN](https://news.ycombinator.com/item?id=45405177) | Link: https://chrisloy.dev/post/2025/09/28/the-ai-coding-trap

- TL;DR
    - Chris Loy argues AI codegen speeds typing, not delivery: complex systems still need human understanding, integration, testing, and design. Treat LLMs like lightning‑fast juniors: unchecked they produce brittle “vibe code”; with guardrails—specs, modularity, TDD, standards, and monitoring—they can amplify sustainable output. HN discussion splits: some say plan‑first workflows with “don’t write code yet” prompts improve architecture and documentation; others warn of lost mental models, debugging overhead, marginal time gains, and prefer manual coding when depth or learning matter.

- Comment pulse
    - Plan-first LLM use improves architecture and docs → “Do not write code yet” prompts enforce design and decisions — counterpoint: mental-model drift yields unstable foundations.
    - Efficiency calculus: prompts save time only when first pass is right → re-prompting/debugging often erase gains; manual coding is safer and faster for many tasks.
    - Workstyle split: thinkers relish AI shifting effort to design/testing; doers/learners prefer manual coding for skill and deep models — counterpoint: user skill with tools compounds.

- LLM perspective
    - View: Use LLMs as scoped executors, not authors—require design briefs, tests, and module boundaries before allowing code changes.
    - Impact: Gains show up in cycle time, defect rates, and onboarding speed, not lines-of-code or “10x” anecdotes.
    - Watch next: IDE agents with verified edits, persistent memory, and coverage-gated merges; org policies on code provenance and automated review.
