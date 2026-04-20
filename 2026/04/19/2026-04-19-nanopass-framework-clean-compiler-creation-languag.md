# Nanopass Framework: Clean Compiler Creation Language

- Score: 110 | [HN](https://news.ycombinator.com/item?id=47777715) | Link: https://nanopass.org/

### TL;DR
Nanopass is a Scheme/Racket embedded DSL for building compilers as many tiny transformation passes over a sequence of intermediate representations, reducing boilerplate and clarifying each stage. Hacker News discussion centers on whether numerous small passes actually simplify real-world compilers: critics describe cross-pass entanglement, redundancy, slower compilation and harder debugging; fans report flexible reordering and clear invariants with 40–50 passes. Commenters note that optimal pass count is language-dependent, and high-quality, many-pass compilers like Chez Scheme can still compile quickly.

### Comment pulse
- Many passes sound clean, but cross-pass dependencies, redundancy and debugging pain arise; mislocated features accumulate tech debt. — counterpoint: some nanopass users liked reordering passes.  
- Optimal pass/IR count is language-specific; Scheme naturally splits into lexer, parser, macro expander, alpha renaming, CPS transform, closure conversion, optimizations, then codegen.  
- More passes and IR conversions can slow compilers, especially with pointers and recomputed flow graphs. — counterpoint: Chez Scheme still compiles ~100 KLOC/s with optimization.  

### LLM perspective
- View: Nanopass suits research/teaching or rapidly evolving languages; industrial compilers may prefer coarser passes plus robust analysis infrastructure.  
- Impact: Frameworks encoding IR evolution declaratively could make refactoring pass pipelines safer, with better invariants and automated validation between stages.  
- Watch next: Useful future work: integrated visualizers for IRs and pass effects, enabling stepwise debugging across dozens of transformations.
