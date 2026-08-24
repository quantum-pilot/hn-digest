# You can't fool the optimizer

- Score: 224 | [HN](https://news.ycombinator.com/item?id=46133622) | Link: https://xania.org/202512/03-more-adding-integers

### TL;DR

Several deliberately convoluted unsigned-addition functions—including loops and recursion—compile to the same single ARM add instruction. The compiler does not catalog every odd coding pattern; it lowers programs into an intermediate representation, canonicalizes equivalent operations, and generates code after the original forms converge. Commenters demonstrate similar loop elimination through LLVM’s scalar-evolution analysis, but stress the limits: language semantics, optimization settings, external functions, algorithms, and memory layout can block transformations. Clear code helps humans, while programmers still own high-level performance decisions.

### Comment pulse

- Optimization needs facts → unsigned types, visibility into callees, and stronger optimization levels can unlock proofs unavailable from source alone.
- Compilers optimize implementation, not architecture → they rarely replace algorithms, repair N-plus-one queries, or redesign data layout.
- Readable code can improve speed indirectly → clear structure exposes larger changes that clever local tricks often obscure.

### LLM perspective

- View: Trust canonicalization for local algebra, but verify generated code when semantics or performance stakes are unusual.
- Impact: Developers can favor intention-revealing source while focusing manual effort on algorithms, locality, and interfaces.
- Watch next: Compare missed optimizations across compilers, flags, aliasing assumptions, link-time visibility, and representative benchmarks.
