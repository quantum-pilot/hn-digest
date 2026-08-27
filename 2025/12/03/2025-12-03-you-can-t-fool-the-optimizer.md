# You can't fool the optimizer

- Score: 224 | [HN](https://news.ycombinator.com/item?id=46133622) | Link: https://xania.org/202512/03-more-adding-integers

### TL;DR

Several deliberately convoluted unsigned-addition functions, including loops and recursion, compile to the same single ARM add instruction. The compiler first translates source into an intermediate representation, simplifies behavior, and canonicalizes equivalent forms before code generation; it does not need a catalog of every strange addition pattern. This lets developers favor readable, intention-revealing code while relying on mature optimizers for local transformations. Commenters stress the boundary: compilers rarely replace algorithms or reorganize data layouts, where programmers can achieve much larger gains.

### Comment pulse

- Compiler explorers expose surprising transformations → LLVM can reduce arithmetic loops and some recursive patterns to direct instructions.
- Optimizers remain constrained by semantics and available knowledge → signed rounding, dynamic linkage, and aliasing can block obvious-looking rewrites.
- Readability usually beats manual micro-optimization → developers still own algorithms, data locality, and communicating useful invariants.

### LLM perspective

- View: Trust compilers with canonical local rewrites, but do not outsource algorithm and memory-layout decisions.
- Impact: Clear code improves human optimization opportunities while preserving the compiler’s ability to simplify implementation details.
- Watch next: Inspect generated code when performance matters, then change abstractions only after measurements expose a real limitation.
