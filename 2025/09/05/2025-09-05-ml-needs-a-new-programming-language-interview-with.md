# ML needs a new programming language – Interview with Chris Lattner

- Score: 311 | [HN](https://news.ycombinator.com/item?id=45137373) | Link: https://signalsandthreads.com/why-ml-needs-a-new-programming-language/

### TL;DR

Chris Lattner argues that fragmented GPU and accelerator stacks need a portable, performance-first programming layer. Modular's Mojo uses Python-like syntax, strong types, and compile-time metaprogramming so domain experts can explicitly specialize kernels across hardware without relying on a “sufficiently smart” compiler. Today, he positions it for fast CPU/GPU code and Python extensions; broader Rust- or Python-like ambitions remain future work. The interview reflects its co-founder's vision, while commenters question ecosystem adoption, missing classes, corporate control, and accelerator licensing.

### Comment pulse

- Supporters value an explicit, typed alternative to CUDA and Python/C++ glue; skeptics stress Python's enormous application ecosystem.
- Licensing and single-company governance are recurring adoption concerns, especially for non-Nvidia accelerators.

### LLM perspective

- View: Mojo's strongest thesis is programmable specialization across hardware, not the much broader prospect of replacing Python.
- Impact: Success could reduce vendor-specific kernel duplication while preserving the expert control that peak accelerator performance requires.
- Watch next: Mojo 1.0 stability, cross-version linking, independent benchmarks, AMD support terms, Python integration, and production users.
