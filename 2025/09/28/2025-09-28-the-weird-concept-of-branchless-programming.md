# The Weird Concept of Branchless Programming

- Score: 108 | [HN](https://news.ycombinator.com/item?id=45405750) | Link: https://sanixdk.xyz/blogs/the-weird-concept-of-branchless-programming

### TL;DR

The tutorial introduces branchless programming as replacing data-dependent control flow with arithmetic, bit masks, conditional moves, or similar instructions to avoid branch-misprediction costs. C examples cover absolute value, clamping, and array partitioning; the author reports no gain for the first two and a roughly 1.2-times partition speedup, recommending the technique only for hot unpredictable loops, cryptography, or SIMD. Commenters challenged both code and measurements, noting optimizing compilers already remove many branches and that longer reruns sometimes made the proposed branchless versions slower.

### Comment pulse

- Commenters urged checking generated assembly before assuming source-level conditionals become machine branches.
- The article’s millisecond-resolution benchmarks were criticized as too coarse to support its performance conclusion.

### LLM perspective

- View: “Branchless” is an assembly property, not a source-code aesthetic, so compiler output and workloads decide its value.
- Impact: Hand-written bit tricks can reduce readability while losing to compiler-generated conditional moves or optimized branches.
- Watch next: Reproducible benchmarks across compilers, optimization levels, architectures, input distributions, and constant-time requirements.
