# Rust Coreutils 0.5.0 Release: 87.75% compatibility with GNU Coreutils

- Score: 90 | [HN](https://news.ycombinator.com/item?id=46264329) | Link: https://github.com/uutils/coreutils/releases/tag/0.5.0

### TL;DR

Version 0.5.0 of the Rust implementation passes 566 of 645 GNU 9.9 tests, lifting measured compatibility from 85.80% to 87.75%; failures dropped to 55 and skips to 23 despite 11 added tests. Changes cover Unicode folding, checksums, install-mode parsing, large integers, TTY testing, and OpenBSD, Redox, and Cygwin support. HN debated whether this incomplete suite justifies distribution adoption, whether memory safety outweighs behavioral gaps, and the consequences of replacing GPL utilities with MIT-licensed ones. Shared tests have also exposed GNU bugs.

### Comment pulse

- Critics said the metric understates incompatibility and Ubuntu moved early; defenders noted many failing edge cases may rarely affect users.
- Licensing split sharply: GPL advocates feared proprietary security fixes, while permissive-license supporters treated MIT as an independent advantage.
- Memory-safety value for local tools was disputed; supporters contrasted possible C code execution with safer Rust failures.

### LLM perspective

- View: Compatibility is not one percentage; deployment risk depends on which edge cases remain and where distributions expose them.
- Impact: Adopters gain cross-platform Rust tools while accepting behavioral, licensing, and operational differences from GNU.
- Watch next: Remaining failures, workload breakage, performance, Ubuntu friction, shared-test discoveries, and convergence speed.
