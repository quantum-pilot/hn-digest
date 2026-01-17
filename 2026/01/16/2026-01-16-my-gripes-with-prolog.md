# My Gripes with Prolog

- Score: 148 | [HN](https://news.ycombinator.com/item?id=46641348) | Link: https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/

- TL;DR  
Wayne, updating his Logic for Programmers book, vents about ISO Prolog’s ergonomics: no standard strings, no functions, few collection types, no booleans, confusing cut/negation semantics, awkward result collection with bagof/`^`, term-operator quirks, and a set-like sort that drops duplicates. He still values bidirectional logic programming but often prefers Picat or ASP. HN commenters largely agree the warts are real, but argue they stem from Prolog’s distinct logic paradigm and highlight meta‑interpretation and good pedagogical resources that make Prolog shine.

- Comment pulse  
  - Prolog has ugly ISO-era corners, but you can write elegant code once you learn idioms; meta‑interpreters showcase Prolog’s unique power.  
  - Many gripes reflect imperative/FP expectations; to use Prolog well you must internalize unification, backtracking, and the interpreter’s search. — counterpoint: cuts/negation remain treacherous even then.  
  - Syntax choices (no trailing commas, operators as terms) come from precedence-based parsing and enable embedded DSLs like CLP(FD), not arbitrary weirdness.

- LLM perspective  
  - View: This tension shows how pure logic languages struggle to serve as general-purpose tools without modernized, standardized libraries and pedagogy.  
  - Impact: Learners may gravitate to Picat, ASP, or Datalog embeddings that keep logic benefits while smoothing Prolog’s sharp edges.  
  - Watch next: Efforts to standardize strings/collections, better negation/cut abstractions, and host-language integrations that hide low-level Prolog quirks.
