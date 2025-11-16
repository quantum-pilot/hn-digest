# Designing a Language (2017)

- Score: 162 | [HN](https://news.ycombinator.com/item?id=45935342) | Link: https://cs.lmu.edu/~ray/notes/languagedesignnotes/

- TL;DR
  - Hands-on guide to language design: iterate through sketching, abstract syntax, concrete syntax, and formal grammar; know paradigms, ask sharp feature questions, and define syntax/statics/dynamics. It walks from ASTs (EsTree) to precedence/associativity, then a tiny language (Astro) specified in Ohm. Discussion pushes for coherent philosophies over feature bloat, suggests Raku for rapid grammar/DSL prototyping, debates whether new languages are worth it, and points to design-rationale resources (Python PEPs, Stroustrup’s C++, Ada) plus niche experiments like stack-based Brainfuck for evolutionary programming.

- Comment pulse
  - Have a coherent philosophy → prevents kitchen‑sink “garbage‑can” languages and keeps feasibility, sustainability, and ergonomics aligned.
  - Use Raku for prototyping → built‑in grammars, RakuAST, and “slangs” speed parsers and DSLs; powerful but “seductive and terrifying” to some.
  - Should you create a new language? → skeptics cite tech debt and duplication—counterpoint: advocates emphasize education, specialization, and progress from diversity.

- LLM perspective
  - View: Start with minimal core and target audience; evolve via prototypes; quantify trade‑offs before adding features.
  - Impact: Prefer DSLs or slangs within host languages to reduce maintenance and adoption friction.
  - Watch next: Prototype with Ohm‑JS, Raku, or ANTLR; measure parse ambiguities, error messages, and user comprehension in small studies.
