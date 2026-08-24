# Thoughts on Generating C

- Score: 187 | [HN](https://news.ycombinator.com/item?id=46945235) | Link: https://wingolog.org/archives/2026/02/09/six-thoughts-on-generating-c

### TL;DR

Compiler author presents C as a pragmatic target: GCC and Clang supply mature optimization, instruction selection, register allocation, and runtime linkage. His patterns use always-inline helpers for zero-cost abstractions, explicit conversion functions with -Wconversion, single-member structs to preserve source-language types, memcpy for unaligned accesses, and manual argument/result placement for large signatures and tail calls. Costs include weak stack control, unavailable side tables, and difficult source debugging. Commenters added that inlining can alter floating-point semantics or optimization, while #line directives and shadow stacks partially address debugging and precise GC.

### Comment pulse

- One commenter warned always-inline boundaries can inhibit optimization, change floating-point contraction, and erase pointer aliasing information; the author resisted turning edge cases into folklore.
- Several recommended #line directives, generated names, and existing generator output as practical debugging aids when emitting full DWARF is infeasible.
- Precise moving GC remains awkward; shadow stacks enable scanning but add writes, aliasing challenges, and poorer debugger visibility.

### LLM perspective

- View: C is attractive when generated code can encode invariants explicitly and accept toolchain-specific compromises.
- Impact: Projects inherit optimized native code without a custom backend, but sacrifice stack, exception, debugging, and portability control.
- Watch next: Cross-compiler musttail behavior, inline regressions, aliasing, #line usability, DWARF options, shadow-stack performance, and precise-GC ergonomics.
