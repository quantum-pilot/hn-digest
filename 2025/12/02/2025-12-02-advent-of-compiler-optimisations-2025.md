# Advent of Compiler Optimisations 2025

- Score: 328 | [HN](https://news.ycombinator.com/item?id=46119500) | Link: https://xania.org/202511/advent-of-compiler-optimisation

### TL;DR

Matt Godbolt’s December series promises 25 daily articles and videos explaining how C and C++ compilers optimize code. Each installment will identify an optimization, show when and why it applies, connect source changes to generated assembly, and examine cases where it does not trigger. The material ranges from architecture-specific details to higher-level transformations, using mostly x86-64 plus 64-bit and 32-bit Arm. The opening announcement frames the project as a practical path toward reading compiler output and reasoning about performance.

### Comment pulse

- Starting simple won approval → readers said expert instruction works best when it builds from first principles.
- Unity builds prompted nuance → link-time optimization largely supersedes them for optimization, though they may shorten some compiles.

### LLM perspective

- View: Daily, example-led explanations can make opaque optimizer behavior approachable without flattening its caveats.
- Impact: Developers may diagnose performance and missed optimizations with better mental models of generated code.
- Watch next: Whether later installments connect architecture-specific mechanics to portable source-level decisions.
