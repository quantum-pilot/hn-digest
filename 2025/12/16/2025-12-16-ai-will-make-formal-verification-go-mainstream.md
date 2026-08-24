# AI will make formal verification go mainstream

- Score: 225 | [HN](https://news.ycombinator.com/item?id=46294574) | Link: https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html

### TL;DR

Martin Kleppmann argues that AI could push formal verification into mainstream software development. Proof assistants can mechanically reject invalid proofs, giving code-generating models a dependable feedback loop and potentially reducing today’s steep proof-writing cost. That matters as AI also increases the volume of code humans may struggle to review. The central limitation remains specification: a flawless proof only shows that software matches its formal requirements, not that those requirements capture ambiguous, changing real-world intent. Human judgment therefore shifts toward specifications, assumptions, and proof scope.

### Comment pulse

- Readers agreed machine-checkable feedback suits coding agents, extending the same loop already provided by compilers, tests, linters, and fuzzers.
- Skeptics emphasized shifting requirements and wrong specifications — counterpoint: authorization and other narrow invariants can still benefit from proofs.
- Some feared abandoning line-by-line review would erode system understanding; others expect review effort to move toward formal contracts.

### LLM perspective

- View: AI makes proof construction cheaper, while proof checking usefully remains deterministic.
- Impact: Verification could move from rare critical systems into ordinary components with crisp, durable invariants.
- Watch next: Specification tooling, proof maintenance after refactors, benchmarked productivity, and formally correct but incomplete requirements.
