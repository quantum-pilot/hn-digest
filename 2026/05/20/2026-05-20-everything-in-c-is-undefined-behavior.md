# Everything in C is undefined behavior

- Score: 468 | [HN](https://news.ycombinator.com/item?id=48203698) | Link: https://blog.habets.se/2026/05/Everything-in-C-is-undefined-behavior.html

### TL;DR

After 30 years with C/C++, the author argues no human can reliably keep nontrivial programs free of undefined behavior. UB is not merely optimizer mischief: the language assigns no meaning to invalid cases, so intent may vanish between compiler stages even at low optimization. Examples include creating misaligned pointers, passing signed char to ctype functions, float-to-int conversion, signed overflow, null representations, varargs mismatches, and divide-by-zero. HN readers agreed the traps are deep but disputed the absolutism, portability assumptions, and proposal that LLM review become standard.

### Comment pulse

- A volatile-read example exposed sequencing subtleties; replies rejected calling single-thread UB a data race and criticized volatile as an MMIO hack.
- Some recommended compiler-defined extensions, packed structs, `-fwrapv`, and disabling strict aliasing — counterpoint: these trade language portability for a specific toolchain contract.
- Critics called conditional examples sensational; defenders stressed input-triggered UB still enables exploits and silently subjects code to compiler, architecture, and runtime changes.

### LLM perspective

- View: UB is an invisible precondition system; safety improves when contracts become machine-checkable rather than hidden in standards prose.
- Impact: Legacy C/C++ teams need automated scanning plus expert review; neither manual vigilance nor unreviewed model patches can scale safely.
- Watch next: Benchmark sanitizers, static analyzers, compiler diagnostics, and LLM reviewers against verified UB corpora and real accepted patches.
