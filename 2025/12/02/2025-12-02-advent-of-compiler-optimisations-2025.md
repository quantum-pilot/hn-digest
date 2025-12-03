# Advent of Compiler Optimisations 2025

- Score: 328 | [HN](https://news.ycombinator.com/item?id=46119500) | Link: https://xania.org/202511/advent-of-compiler-optimisation

## TL;DR
Matt Godbolt announces an “Advent of Compiler Optimisations 2025”: 25 daily posts and videos explaining concrete C/C++ optimizations, how to read the resulting assembly, and when each transformation applies or fails, mostly on x86-64 with some ARM. HN readers are enthusiastic, praising his accessible, start-simple teaching style and broader contributions like Compiler Explorer, while discussing the value of understanding the abstraction layer beneath your work and related build techniques such as unity builds vs LTO.

## Comment pulse
- Godbolt’s work prompts the “know one layer down” rule → understanding runtimes, OS, or JVM makes debugging and performance tuning feasible, not magical.  
- People value that the series starts with simple optimizations → on-ramps for non-experts, avoiding immediately diving into esoteric x86 tricks.  
- Readers request SQLite-style amalgamation coverage → triggers unity-build vs LTO debate on speed and build times—counterpoint: amalgamation concerns build engineering, not compiler optimization.  

## LLM perspective
- View: A focused advent series creates a structured, low-friction way to build real intuition about modern optimizing compilers.  
- Impact: Systems programmers, performance engineers, and curious application developers gain vocabulary to reason about generated assembly and optimization tradeoffs.  
- Watch next: community spin-offs like exercises, live-coding, or compiler-agnostic benchmarks could turn the series into a reusable curriculum and reference.
