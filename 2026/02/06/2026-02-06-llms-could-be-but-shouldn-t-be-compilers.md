# LLMs could be, but shouldn't be compilers

- Score: 108 | [HN](https://news.ycombinator.com/item?id=46912781) | Link: https://alperenkeles.com/posts/llms-could-be-but-shouldnt-be-compilers/

### TL;DR
The essay argues that even if LLMs stopped hallucinating, they still shouldn’t replace compilers in the sense of “write only English, get correct programs.” Traditional compilers rest on precise formal languages and semantics, so we know what “correct” means and can test it. Natural language is inherently underspecified, so LLMs must guess data models, edge cases, and tradeoffs, quietly turning vague requests into concrete systems. That encourages “specification laziness”; the real bottleneck becomes writing tight specs and verification, not code.

---

### Comment pulse
- Determinism isn’t the key distinction → compilers can be nondeterministic but semantically closed; LLMs are semantically open, so correctness isn’t internally decidable — counterpoint: even deterministic LLM “guesses” are unsafe.

- LLMs resemble fallible humans more than compilers → need oversight, review, and accuracy metrics, like other probabilistic ML systems, rather than assuming compiler-like guarantees.

- Treat LLMs as anything‑to‑anything pipelines → better to go description → spec → plan → implementation than straight to code, keeping humans in charge of specification and review.

- Some see hallucinations as secondary → they already test generated code like any other; critics reply that debugging and performance tuning at the wrong abstraction level is costly.

---

### LLM perspective
- View: Use LLMs as optimizing assistants over well-specified artifacts (tests, specs, schemas), not as primary interpreters of fuzzy intent.

- Impact: Strong specification skills, property-based testing, and contracts become central developer competencies; prompt-writing alone isn’t enough.

- Watch next: IDEs that co-design specs and tests with LLMs, plus benchmarks comparing spec-driven vs. prompt-only development workflows on reliability and maintainability.
