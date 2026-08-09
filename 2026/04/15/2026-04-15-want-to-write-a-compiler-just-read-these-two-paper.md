# Want to write a compiler? Just read these two papers (2008)

- Score: 455 | [HN](https://news.ycombinator.com/item?id=47776796) | Link: https://prog21.dadgum.com/30.html

### TL;DR

James Hague argues compiler construction feels harder than it is because textbooks front-load broad theory. He recommends Jack Crenshaw’s “Let’s Build a Compiler!” for a minimal single-pass compiler with parsing and code generation interleaved, then “A Nanopass Framework for Compiler Education” for the missing abstraction: represent programs internally and implement compilation as dozens of tiny, separate transformations. Build working systems first; consult comprehensive references afterward when their concepts answer concrete needs.

### Comment pulse

- Alternatives included Dragon Book chapter 2, Wirth’s 99-page Compiler Construction, Ghuloum’s incremental approach, and Crafting Interpreters.
- Modern backends require SSA, data-flow analysis, optimization, linking, and object formats beyond these beginner paths.
- Thick books work as random-access references — counterpoint: novices cannot retrieve concepts they do not know exist.

### LLM perspective

- A sequence of executable milestones provides fast feedback and keeps theory attached to observable behavior.
- Nanopasses improve inspectability and testing, though production pass counts add orchestration and performance costs.
- Start with a tiny language, explicit IR, golden tests, and one real target before optimizing.
