# How to make a fast dynamic language interpreter

- Score: 241 | [HN](https://news.ycombinator.com/item?id=47843194) | Link: https://zef-lang.dev/implementation

## TL;DR

Author takes a deliberately naive, AST‑walking interpreter for a dynamic language (Zef) and, via 21 incremental changes, speeds it up 16.6× under Fil‑C++ and ~67× under Yolo‑C++. Key wins: good tagged value representation, replacing strings with interned symbols, redesigning the object model, adding inline caches and watchpoints for property/method access, and aggressively reducing allocations around arguments and common operations. The final interpreter becomes competitive with CPython, Lua, and QuickJS on classic language benchmarks, without using a JIT or bytecode.

## Comment pulse

- Language design matters → Wren/Lua trade away dynamic shapes and extreme dynamism, enabling simpler, faster method lookup than Python’s heavily dynamic model.  
- Inline caches on ASTs → Zef uses placement-new to specialize AST nodes; great for single-threaded interpreters, but conflicts with immutable-AST sharing and background JIT compilation.  
- Parallel experiences → Rust and Scheme implementers report similar gains from argument-arity specialization, closure/object model work; reinforces that dispatch and allocation dominate, not exotic tricks.

## LLM perspective

- View: This is a stepwise recipe for taking a “toy” interpreter into production-speed territory using mostly classic VM ideas.  
- Impact: Especially valuable for language hobbyists and educators: it demystifies inline caches, object layouts, and allocation tuning without diving into full JITs.  
- Watch next: Add bytecode tier, real GC in the Yolo-C++ build, and cross-VM benchmarks with more real‑world, allocation-heavy workloads.
