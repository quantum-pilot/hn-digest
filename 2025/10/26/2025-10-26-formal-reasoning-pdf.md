# Formal Reasoning [pdf]

- Score: 113 | [HN](https://news.ycombinator.com/item?id=45711062) | Link: https://cs.ru.nl/~freek/courses/fr-2025/public/fr.pdf

- TL;DR
  - The discussion frames formal reasoning as symbol manipulation under fixed rules, with proofs mechanically checkable. Commenters refine this: undecidable languages are still formal, and “mechanical” predates computers (Gödel, Turing). HN explores using formal languages as intermediates for LLMs, but reports NL→formal mapping is hard (natural language semantics is messy) and LLMs lag humans at tools like Lean. Still, hybrid pipelines—Prolog intermediates, SQL verification—show practical wins; classic logic texts (e.g., Tarski) and Montague semantics provide grounding.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - Formal means mechanical manipulation of symbols; proofs are machine-checkable; undecidable languages still formal; the notion predates computers—counterpoint: computers also misinterpret, and sometimes parse informal text.
  - NL→formal→solver→NL pipeline is appealing, but Montague-style semantics shows translation is hard: quantification, scope, anaphora, modality, pragmatics make compositional mapping brittle.
  - Practice: LLMs underperform humans at Lean 4 formalization; limited training data. Yet Prolog intermediates and SQL verification pipelines show tractable, narrow hybrid wins.

- LLM perspective
  - View: Use formal tools as validators and planners around LLMs, not full NL translators; target constrained domains and schemas.
  - Impact: Safer code/SQL generation, semi-automated proofs, and explainable reasoning steps in production pipelines.
  - Watch next: Curated NL→Lean datasets, standardized semantic benchmarks, proof-check rates, and case studies comparing Prolog/SMT integrations against baseline LLMs.
