# The Cost of a Closure in C

- Score: 182 | [HN](https://news.ycombinator.com/item?id=46228597) | Link: https://thephd.dev/the-cost-of-a-closure-in-c-c2y

### TL;DR
The post measures how expensive it is to emulate closures in C compared with native mechanisms in C++ and other systems. C++ lambdas effectively act as compile-time closures: the compiler creates a small struct of captured state and optimizes access, so they benchmark very well. GNU C’s nested functions rely on trampolines that require executable memory, hurting both performance and security. The discussion argues C really lacks a “fat” function pointer (code + context), while `std::function` shows how ownership-heavy abstraction can explode costs in recursive scenarios.  
*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- GCC trampolines need executable stacks → distros disable those for security; `-ftrampoline-impl=heap` moves trampolines to mmap’d heap pages to avoid executable stacks.  
- Article’s “static variable” wording criticized → defenders note it matches ISO C “static storage duration”; debate reveals subtle confusion about storage vs linkage.  
- Benchmarks: lambdas and `function_ref` are lean closures → `std::function` copies state recursively, causing massive overhead; some still oppose adding closures to C at all.

---

### LLM perspective
- View: C would benefit from a standardized bound-method/fat-pointer primitive instead of full-blown lambda syntax.  
- Impact: Systems code, callbacks, and event frameworks in C could gain safety and speed without C++-level complexity.  
- Watch next: WG14 proposals on closures, GCC’s heap-trampoline evolution, and real-world benchmarks beyond micro-tests like Man-or-Boy.
