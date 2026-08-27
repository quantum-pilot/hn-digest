# Why don't you use dependent types?

- Score: 171 | [HN](https://news.ycombinator.com/item?id=45790827) | Link: https://lawrencecpaulson.github.io//2025/11/02/Why-not-dependent.html

### TL;DR

Isabelle creator Lawrence Paulson explains that he spent years with AUTOMATH and Martin-Löf type theory before favoring generic Isabelle and higher-order logic. He argues LCF-style kernels do not need stored proof objects and says ALEXANDRIA formalized advanced mathematics, including Grothendieck schemes, without hitting a dependent-type barrier. He remains wary of intensional equality, performance complaints, and knowing when not to use dependent types, while admiring Lean's community. Commenters largely reframed the issue from necessity to tradeoffs among expressiveness, debugging, proof ergonomics, logical strength, and libraries.

### Comment pulse

- Practitioners value types indexed by values, but warn that equality and type-checking failures can become difficult to diagnose.
- Readers disputed whether “unnecessary” matters; productivity depends on formalism, tooling, task, and user preference.
- HOL's strength and category-theory size issues remained contested, with added axioms offered as one answer.

### LLM perspective

- View: Mature proof assistants demonstrate that foundations matter less alone than automation, libraries, interfaces, and community practice.
- Impact: Teams can choose simpler logics without forfeiting advanced verification, but may sacrifice convenient encodings.
- Watch next: Comparative proof size, checker performance, equality friction, library growth, and reproducible case studies across systems.
