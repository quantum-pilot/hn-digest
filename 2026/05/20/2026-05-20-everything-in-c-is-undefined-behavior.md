# Everything in C is undefined behavior

- Score: 468 | [HN](https://news.ycombinator.com/item?id=48203698) | Link: https://blog.habets.se/2026/05/Everything-in-C-is-undefined-behavior.html

### TL;DR
- The post argues that essentially all nontrivial C/C++ code contains undefined behavior (UB), and that no human can realistically avoid it, even experts.  
- UB isn’t “the optimizer being mean”; it’s the language saying certain situations have no defined meaning, so compilers can assume they never occur and generate code that silently misbehaves if they do.  
- Examples span alignment, casting, varargs, float–int conversions, null pointers, and integer promotions.  
- The author uses LLMs to systematically find UB (including in OpenBSD), and suggests that in 2026 serious C/C++ work without automated UB checking is increasingly irresponsible.

---

### Comment pulse
- UB is deeper and weirder than the article shows → volatile, sequencing, and packed/unaligned access make even simple expressions technically UB—counterpoint: this is largely a spec-design failure.  
- UB is about the C abstract machine, not hardware faults → once UB happens, the compiler can erase or reorder code arbitrarily, so “it works on my CPU” is meaningless.  
- Some call the post FUD, noting UB often depends on inputs → others respond that input‑triggered UB is exactly what attackers exploit, making such “edge” cases critical.

---

### LLM perspective
- View: LLMs are now practical UB auditors; pairing static analyzers, sanitizers, and LLM review is a realistic safety baseline for C/C++.  
- Impact: Systems, embedded, and security‑sensitive projects gain; lone experts offload tedious spec‑lawyering and focus on design.  
- Watch next: Benchmarks comparing LLM‑assisted UB finding vs. UBSan/compilers on large codebases; organizational rules that require automated UB audits for critical C/C++ code.
