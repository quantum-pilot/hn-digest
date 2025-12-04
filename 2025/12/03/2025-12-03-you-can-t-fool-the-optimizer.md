# You can't fool the optimizer

- Score: 224 | [HN](https://news.ycombinator.com/item?id=46133622) | Link: https://xania.org/202512/03-more-adding-integers

### TL;DR
Godbolt shows several bizarre implementations of `x + y` on ARM—including a recursive version—that all compile to the same single `add` instruction. Compilers translate source into an intermediate representation and aggressively canonicalize equivalent patterns, allowing them to see through obfuscation and replace loops and recursion with simple arithmetic. This supports the advice: write clear, intention-revealing code and let the optimizer handle micro-optimizations. Hacker News debates where compilers excel, where they fail, and how much to “trust the optimizer.”

---

### Comment pulse
- Optimizers can be impressively smart → LLVM’s Scalar Evolution folds many loops (even Brainfuck-like) into closed-form arithmetic; Julia and SCEV examples show non-trivial loop-to-formula rewrites.  
- Optimizers still miss “obvious” math → e.g., `%2 && %3` vs `%6`, `strlen("hello")`, division vs shift; flags, language semantics, and link-time visibility all constrain transformations — counterpoint: higher optimization levels or LTO often fix these.
- Trust compilers for low-level tweaks → focus on algorithms and data layout, which compilers rarely change; DFA and peephole rules help, but formal equivalence has hard theoretical limits.

---

### LLM perspective
- View: Treat compilers as algebra engines that normalize code; write for clarity, then check generated assembly when performance is critical.  
- Impact: Systems and HPC developers gain confidence to avoid hand-rolled micro-tricks, investing effort in data structures and asymptotic improvements.  
- Watch next: Better interprocedural and whole-program reasoning (LTO, devirtualization) and tools exposing optimization decisions to guide source-level refactors.
