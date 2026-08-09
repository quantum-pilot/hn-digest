# A sufficiently detailed spec is code

- Score: 588 | [HN](https://news.ycombinator.com/item?id=47434047) | Link: https://haskellforall.com/2026/03/a-sufficiently-detailed-spec-is-code

### TL;DR

The author argues that reliable code generation cannot eliminate programming labor: a specification precise enough to determine behavior becomes pseudocode, formalism, or code itself. OpenAI’s Symphony illustrates the claim; its lengthy specification embeds schemas, algorithms, redundancy, and literal pseudocode, yet Claude Code’s Haskell implementation still contained bugs and stalled on a trivial ticket. The post says specifications should support deliberate design, not promise cheaper delivery. HN agreed reliability demands constrained details, while noting models can successfully infer familiar, low-stakes boilerplate from terse prompts.

### Comment pulse

- Model weights act as a shared codebook → terse prompts can decode familiar applications — counterpoint: novelty and complexity sharply reduce reliability.
- A specification defines an envelope of compliant programs → underspecified security, performance, and interfaces permit both good and dangerous implementations.
- Formal methods expose the same tradeoff → abstract specifications widen the verification gap, while precise synthesis languages move closer to code.

### LLM perspective

- **View:** Agents compress implementation when conventions supply missing detail; they do not erase the need to define novel behavior.
- **Impact:** Teams should spend specification effort on constraints, risks, and acceptance tests rather than translating every algorithm into prose.
- **Watch next:** Repeated Symphony reproductions, conformance rates, brownfield maintenance results, and machine-checked links between specifications and implementations.
