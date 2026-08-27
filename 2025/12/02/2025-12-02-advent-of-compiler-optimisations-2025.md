# Advent of Compiler Optimisations 2025

- Score: 328 | [HN](https://news.ycombinator.com/item?id=46119500) | Link: https://xania.org/202511/advent-of-compiler-optimisation

### TL;DR

Matt Godbolt introduces a 25-day series of short posts and videos explaining compiler optimizations in C and C++. Each installment aims to show what optimization applies, how it appears in assembly, and when it cannot be used. Examples will mostly target x86-64, with some 32-bit ARM and AArch64, spanning low-level instruction choices and higher-level transformations. Commenters welcomed the gradual progression and the practice of understanding one layer below; discussion also noted that link-time optimization has largely displaced unity builds.

### Comment pulse

- Progressive examples earned praise → small compiler transformations make assembly literacy approachable.
- Unity-build curiosity → broader visibility once enabled optimizations, but commenters argue LTO now addresses much of that role.

### LLM perspective

- View: Explaining optimization boundaries is more educational than presenting clever assembly alone.
- Impact: C and C++ developers can better predict performance and recognize misleading microbenchmarks.
- Watch next: Track which transformations generalize across architectures and which depend on target-specific cost models.
