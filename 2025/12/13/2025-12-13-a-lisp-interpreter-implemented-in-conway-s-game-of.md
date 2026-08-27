# A Lisp Interpreter Implemented in Conway's Game of Life (2021)

- Score: 85 | [HN](https://news.ycombinator.com/item?id=46251620) | Link: https://woodrush.github.io/blog/posts/2022-01-12-lisp-in-life.html

### TL;DR

This project runs a Lisp interpreter directly inside Conway’s Game of Life: source text is encoded as cells in simulated RAM, then read, parsed, evaluated, and written back as binary ASCII. The author compiled a C implementation through an extended ELVM toolchain to a modified QFT architecture, represented first in VarLife and then in enormous OTCA metapixels. It supports closures, macros, control flow, lists, evaluation, and arithmetic, but even printing 3×14 requires trillions of Life generations and substantial compute resources.

### Comment pulse

- Discussion mainly connected the work to earlier cellular-automata computers and the broader ELVM compilation stack.

### LLM perspective

- View: The achievement is conceptual completeness, not practical speed: interpretation itself emerges from Life’s simple rule.
- Impact: It makes universality tangible by connecting high-level language semantics to explicit cellular evolution.
- Watch next: Further architectural or Hashlife optimizations that reduce the immense simulation cost without weakening the demonstration.
