# Formalizing Fermat's Last Theorem

- Score: 625 | [HN](https://news.ycombinator.com/item?id=49568506) | Link: https://www.anthropic.com/research/formalizing-fermats-last-theorem

### TL;DR

Anthropic says Claude agents produced the first complete computer-checked formalization of Fermat’s Last Theorem in Lean, largely autonomously over 11 days. Using Prove2Me and a multi-agent harness, the effort generated 13 million lines, used 29,500 intermediate theorems, and consumed roughly six billion output tokens. Lean checked the proof against standard axioms, and a comparator matched its theorem statement to Mathlib’s. The work formalizes existing mathematics rather than discovering a new proof, and still depends on trusted tooling and correct specification.

### Comment pulse

- Commenters stressed that proof length does not itself weaken verification; confidence concentrates in Lean’s checker and the encoded statement.
- Mathematicians noted formal checking cannot replace exposition or assess a paper’s significance and contextual meaning.
- Discussion celebrated the speed while questioning undisclosed compute cost and effects on long-running human formalization projects.

### LLM perspective

- View: The breakthrough is scalable translation into checkable form, not a replacement for mathematical understanding.
- Impact: Referees may offload correctness checks while spending more effort on meaning, novelty, and exposition.
- Watch next: Independent recompilation, proof simplification, exact compute costs, checker audits, and reuse in Mathlib.
