# Your code is fast – if you're lucky

- Score: 124 | [HN](https://news.ycombinator.com/item?id=48870799) | Link: https://tiki.li/blog/lucky_code.html

### TL;DR

An optimized C Quicksort changed from two statements—store through a pointer, then increment it—to the compact `*ptr++ = value` idiom. On an M1 with Clang `-O3`, the reported time for sorting 50 million doubles fell from 4.39 seconds to 0.70, beating a cited 1.33-second `std::sort` run. Clang’s altered intermediate ordering let SimplifyCFG merge branch stores into a select, producing ARM `csel` or x86 `cmov`; GCC retained branches. HN analysis traced the brittleness to pass pattern-matching, questioned benchmark rigor and readability, and noted branchless code can itself be slower.

### Comment pulse

- The IR shape explains the outcome → compact syntax leaves stores at branch ends, enabling SimplifyCFG to hoist them behind a select.
- Semantic equivalence does not ensure optimizer equivalence → conservative, ordered passes recognize local patterns and may never normalize both ASTs identically.
- Branchless is workload-dependent → one commenter measured a 30% win after replacing conditional moves with branches — counterpoint: the explanation remained uncertain.

### LLM perspective

- **View:** This demonstrates compiler sensitivity, not a general rule that terse C is faster or conditional moves are superior.
- **Impact:** Performance-critical code needs assembly inspection and repeatable benchmarks across compilers, architectures, datasets, and realistic branch predictability.
- **Watch next:** Report repeated trials, identical inputs, correctness checks, more compilers, and whether a reduced reproducer triggers LLVM remediation.
