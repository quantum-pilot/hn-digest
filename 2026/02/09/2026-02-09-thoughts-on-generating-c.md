# Thoughts on Generating C

- Score: 187 | [HN](https://news.ycombinator.com/item?id=46945235) | Link: https://wingolog.org/archives/2026/02/09/six-thoughts-on-generating-c

- TL;DR  
  The author, a compiler engineer, explains practical patterns for targeting C from higher-level languages: encode abstractions via always-inlined helper functions, use explicit integer conversions, and wrap pointers/integers in single-field structs to carry source-level type information. They also rely on memcpy for unaligned memory, manually manage ABI registers and multi-value returns via globals to guarantee tail calls, and treat C as a “local optimum” backend despite poor stack control, GC integration, exceptions, and debugging. Comments add caveats, GC tricks, and backend war stories.

- Comment pulse  
  Static inline and uintptr_t wrappers impede optimization → bugs, aliasing loss, FP quirks make helpers slower than direct expressions — counterpoint: avoid overgeneralizing compilers.  
  Precise GC over C needs a shadow stack → linked pointer-frame arrays enable stack scanning but obscure variables and hurt debugging, even with #line tricks.  
  Some language implementers tire of backends → prefer targeting C, sometimes relying on specific compilers or LLVM bitcode despite portability and debugging drawbacks.

- LLM perspective  
  View: Treat C as a constrained IR: define a strict coding subset, helper libraries, and test suites across compilers and architectures.  
  Impact: For GC-heavy languages, investing in reusable shadow-stack and debug-visualization tooling may yield more benefit than chasing ideal zero-cost exceptions.  
  Watch next: Monitor standardization of musttail, stack maps, and C++ reflection; once stable, they could simplify portable tail-calls and precise GC.
