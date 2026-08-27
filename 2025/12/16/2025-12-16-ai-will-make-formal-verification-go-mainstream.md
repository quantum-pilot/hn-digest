# AI will make formal verification go mainstream

- Score: 225 | [HN](https://news.ycombinator.com/item?id=46294574) | Link: https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html

### TL;DR

Martin Kleppmann predicts coding agents will make machine-checked proofs cheap enough for ordinary software, while AI-generated code increases demand for stronger guarantees. Proof assistants reject invalid scripts deterministically, making hallucination less dangerous and giving agents a tight correction loop. The bottleneck would shift from constructing proofs to writing specifications that capture what users actually need. Commenters saw immediate value in cryptography, compilers, authorization, and agent tooling, but doubted changing business requirements can be formalized economically across typical applications.

### Comment pulse

- Supporters placed proof assistants atop a ladder of executable feedback: compilers, tests, linters, fuzzers, analyzers, then formal guarantees.
- Skeptics argued verification can prove the wrong specification and becomes expensive when ambiguous requirements or stakeholder preferences change.
- Debate remained over scope: some expect broad CRUD security value; others reserve formal methods for implementations far more complex than specifications.

### LLM perspective

- View: AI lowers proof-construction cost, but cannot remove the semantic work of deciding which properties matter.
- Impact: High-assurance components may expand first, while ordinary teams gain lighter verification through types, properties, and analyzers.
- Watch next: Measure expert supervision, proof maintenance after changes, specification defects, and total cost against strong testing.
