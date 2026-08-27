# Notes by djb on using Fil-C

- Score: 286 | [HN](https://news.ycombinator.com/item?id=45788040) | Link: https://cr.yp.to/2025/fil-c.html

### TL;DR

Daniel J. Bernstein reports strong compatibility from Fil-C, a garbage-collected, memory-safe C/C++ compiler: his parallel build completed 60 of 61 bundled targets, while cryptographic microbenchmarks typically used one to four times clang's cycles. He documents substantial build memory, package-specific fixes, helper scripts, and an experiment treating Fil-C as a new Debian ABI so protected packages can replace ordinary amd64 versions. Commenters saw this as meaningful validation, while noting whole-program constraints, uncertain FFI, runtime overhead, and that the heaviest memory use likely comes from building LLVM and Clang.

### Comment pulse

- Readers interpreted the Debian rebuild effort as a strong practical endorsement of Fil-C's compatibility.
- Discussion distinguished retrofitting memory safety onto existing C/C++ from choosing a managed language for new code.

### LLM perspective

- View: The experiment tests whether memory safety can become a packaging choice instead of a source rewrite.
- Impact: Successful Debian integration could protect legacy software while preserving much of its existing build ecosystem.
- Watch next: Package coverage, FFI boundaries, performance distributions, build resource use, debugging quality, and ABI maintenance.
