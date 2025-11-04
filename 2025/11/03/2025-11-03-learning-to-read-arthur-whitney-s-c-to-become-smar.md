# Learning to read Arthur Whitney's C to become smart (2024)

- Score: 316 | [HN](https://news.ycombinator.com/item?id=45800777) | Link: https://needleful.net/blog/2024/01/arthur_whitney.html

- TL;DR
    - A patient, line-by-line tour of Arthur Whitney’s ~50-line K-like C interpreter: macros, GCC extensions, atom/vector representation, lifted ops, and a right-to-left evaluator. The author praises compact, composable primitives and one-screen locality, but flags non-semantic typing, code-golfing, portability warnings, and heavy implicitness. Takeaway: this density suits “finished” designs; model first, then code. HN links the style to APL/K (and J), debates macro “war crimes,” and weighs best-practice tradeoffs with nods to Bourne’s Algol-flavored C.

- Comment pulse
    - Understanding needs APL/K → Style mirrors APL’s terse arrays; yet macros/ternaries/type‑punning aren’t APL, so APLers find it alien — counterpoint: J is an easier on‑ramp.
    - Macro style is hazardous → GCC-only extensions, implicit globals, and missing braces risk bugs and unreadability; one commenter called it “war crime” territory.
    - Break “best practices” selectively → Density keeps the whole program visible; tradeoffs hit maintainability, onboarding, and portability; historic parallel: Bourne’s Algol-like C.

- LLM perspective
    - View: Dense C can model array semantics; pre-modeling yields cleaner primitives than iterative refactoring.
    - Impact: Individual hackers gain speed and insight; teams risk unreadability, undefined behavior, toolchain lock-in, and brittle APIs.
    - Watch next: Prototype a typed variant, longer vectors, multi-digit numbers, and GC; compare readability, bugs, and portability to the 50-line baseline.
