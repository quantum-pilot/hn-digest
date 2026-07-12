# Your code is fast – if you're lucky

- Score: 124 | [HN](https://news.ycombinator.com/item?id=48870799) | Link: https://tiki.li/blog/lucky_code.html

### TL;DR
A quicksort partition loop written with a “beginner-friendly” style  
```c
*lwr = x; lwr++;
*rwr = x; rwr--;
```  
compiled much slower than the compact idiom  
```c
*lwr++ = x;
*rwr-- = x;
```  
even though they are semantically equivalent. In Clang/LLVM, the latter triggers a pattern that becomes branchless `cmov`-style code; the former leaves an actual branch. HN discussion digs into AST/IR differences, fragile optimization passes, and how tiny syntactic shifts can unpredictably change performance.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Minor syntax change → different LLVM IR → SimplifyCFG only recognizes the single-statement pattern, hoists the store, and emits branchless code; two-statement form blocks this.
- Distinct AST shapes (`*p++ = x` vs `*p = x; p++`) mean extra passes are needed to unify them; optimizers stay conservative to avoid miscompiles.
- Some worry about quicksort’s O(n²) worst-case; others note both versions sort identical data, so variation is from code generation, not algorithmic complexity.

---

### LLM perspective
- View: Treat compiler output as another artifact to test; small refactors can silently change performance characteristics.
- Impact: Low-level C/C++ code, hot loops, and performance-critical libraries are most exposed to such optimizer brittleness.
- Watch next: Better IR canonicalization, less pattern-fragile passes, and tooling that flags large codegen changes from tiny source edits.
