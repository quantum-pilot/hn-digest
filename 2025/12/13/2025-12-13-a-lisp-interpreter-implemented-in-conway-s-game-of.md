# A Lisp Interpreter Implemented in Conway's Game of Life (2021)

- Score: 85 | [HN](https://news.ycombinator.com/item?id=46251620) | Link: https://woodrush.github.io/blog/posts/2022-01-12-lisp-in-life.html

### TL;DR

Hikaru Ikuta built a Lisp interpreter that runs inside Conway’s Game of Life, demonstrating the cellular automaton’s universality through a high-level language rather than assembly alone. Lisp source enters as ASCII-encoded cells; output appears in simulated RAM. A C interpreter supporting lexical closures and macros is compiled through ELVM to a modified Quest for Tetris CPU, first represented in VarLife and then converted with 2,048-by-2,048 metapixels. Extensive optimizations make a tiny multiplication program finish in VarLife in about one minute, but native Life still needs roughly six hours.

### Comment pulse

- Readers situated ELVM as a C front end and intermediate representation targeting deliberately strange machines, including QFTASM and lambda calculus.
- Related references showed the same theme through register machines, Diophantine equations, and earlier discussions of this project.

### LLM perspective

- View: The project is valuable as an end-to-end proof, not as a practical execution environment.
- Impact: It exposes how compilers, architecture, representation, and simulation costs compound across abstraction layers.
- Watch next: Smaller patterns, faster Hashlife runs, broader C compatibility, and independent verification of claimed novelty.
