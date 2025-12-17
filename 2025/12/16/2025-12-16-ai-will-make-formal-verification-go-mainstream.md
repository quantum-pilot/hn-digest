# AI will make formal verification go mainstream

- Score: 225 | [HN](https://news.ycombinator.com/item?id=46294574) | Link: https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html

### TL;DR
Kleppmann argues that large language models will flip the economics of formal verification. Historically, proving software correct required rare expertise and huge effort (e.g., orders of magnitude more proof than code), so only kernels, compilers, and crypto stacks justified it. LLMs are already competent at generating proof scripts, and automated proof checking neutralizes hallucinations. As AI-generated code proliferates, he expects specs (not proofs) to become the bottleneck, with AI also assisting in writing them—pushing formal methods into the software mainstream.

---

### Comment pulse
- FV is overkill for typical apps → everyday code has shifting, ambiguous, 100‑page specs; formalizing them is costlier than tests, and most software tolerates bugs.  
  — counterpoint: spec languages like TLA+ express high‑level, non-computable properties we can’t capture in normal code.

- Many “boring” systems still have critical invariants → access control, authorization, and data consistency constraints are valuable but rarely verified because it’s too hard, not because they lack payoff.

- AI agents thrive on feedback loops → tests, linters, fuzzers, strong type systems, and FV tools act as oracles that turn semantic mistakes into tight, automatable correction cycles.

---

### LLM perspective
- View: Formal methods will likely expand first in high-value components and AI-heavy stacks, not “all software,” but that’s still a huge shift.

- Impact: Security, infra, finance, and safety-critical domains gain cheaper high assurance; junior and AI “engineers” get guardrails instead of total trust.

- Watch next: Benchmarks of LLMs in Coq/Lean/Isabelle-on-real-projects, industrial FV pilots for AI-written services, and IDEs that surface specs as first-class artifacts.
