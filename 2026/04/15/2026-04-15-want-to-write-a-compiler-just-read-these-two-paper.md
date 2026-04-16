# Want to write a compiler? Just read these two papers (2008)

- Score: 455 | [HN](https://news.ycombinator.com/item?id=47776796) | Link: https://prog21.dadgum.com/30.html

## TL;DR
The article argues that most compiler textbooks (e.g., the Dragon Book) are too broad and theoretical for beginners, reinforcing the myth that compilers are “hard.” Instead, it recommends Jack Crenshaw’s “Let’s Build a Compiler” to show a simple, single-pass compiler, then the “Nanopass Framework” paper to reframe compilers as many tiny, composable IR-to-IR transformations using ASTs. Hacker News comments add other approachable resources (Wirth’s book, Ghuloum, Crafting Interpreters) and debate whether heavyweight texts like Dragon are good starting points.

## Comment pulse
- Dragon Book and Wirth’s “Compilers” suffice to write a compiler → clear, end‑to‑end coverage in few chapters/pages — counterpoint: Dragon nearly scares some away entirely.  
- Incremental tutorials (Ghuloum’s Scheme compiler, Nora Sandler’s C compiler, Amin’s implementation) → many small steps from interpreter to real x86 assembly, with tests.  
- Modern suggestions (Crafting Interpreters, meta-compilers, SSA-based backends) → need intros that bridge toy compilers to optimization, SSA, linking, and contemporary toolchains.

## LLM perspective
- View: Start with a tiny, working compiler and nanopass-style transformations; treat theory texts as later reference, not entry points.  
- Impact: Lowers the barrier for self-taught developers and students; encourages more language experimentation and custom DSLs.  
- Watch next: Unified beginner track covering parsing, IR/AST, SSA, basic optimization, and linking, backed by runnable reference implementations and test suites.
