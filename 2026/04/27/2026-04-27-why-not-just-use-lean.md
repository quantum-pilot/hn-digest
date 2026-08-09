# “Why not just use Lean?”

- Score: 244 | [HN](https://news.ycombinator.com/item?id=47922079) | Link: https://lawrencecpaulson.github.io//2026/04/23/Why_not_Lean.html

### TL;DR

Paulson says Lean’s dominance should neither erase history nor enforce conformity. Earlier systems including AUTOMATH, ACL2, HOL, Isabelle, Rocq, and Mizar formalized deep mathematics; propositions-as-types is only one architecture. He recommends Lean when collaborators and prerequisites already use it, but favors Isabelle for Sledgehammer automation, readable structured proofs, and avoiding dependent-type complexity. Hacker News largely treated the systems as different tradeoffs and Lean’s community, library, and tooling as its advantage, while challenging Paulson’s claim that Lean wastefully retains massive proof objects and noting Isabelle’s own resource and tooling problems.

### Comment pulse

- Lean may be a jack-of-all-trades whose modern tooling, Mathlib, and community outweigh stronger individual features elsewhere.
- Isabelle and Lean target different domains; Sledgehammer offers automation, while Lean’s development experience and ecosystem feel more accessible.
- Paulson says Lean keeps useless giant terms — counterpoint: commenters say opaque theorems let the kernel ignore proofs after checking.

### LLM perspective

- **View:** Selection should follow libraries, collaborators, automation, readability, and verification domain—not prestige.
- **Impact:** AI translation may weaken library network effects and make minority systems more practical.
- **Watch next:** Cross-assistant proof ports, verified translation, memory measurements, Lean automation, CSLib growth, and human-legibility studies.
