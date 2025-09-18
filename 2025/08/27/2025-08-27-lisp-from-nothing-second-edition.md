# Lisp from Nothing, Second Edition

- Score: 372 | [HN](https://news.ycombinator.com/item?id=45037419) | Link: http://t3x.org/lfn/index.html

- TL;DR
  - “Lisp from Nothing” (2nd ed.) is a hands-on tour from a metacircular evaluator to a ~400‑line self‑hosting Lisp compiler that emits a single C program, with free code. New: a Lambda Calculus chapter, quasiquotation for macros, and prose/errata fixes, plus reflections on early Lisp hacking. HN readers celebrate the author’s minimalist, practice-driven philosophy; others deep-dive Church encodings and nil tests; several recommend his website and “Scheme 9 from Empty Space.” The author emphasizes beauty and simple knowledge transfer.

- Comment pulse
  - Author’s ethos → Create something beautiful and teach simply; readers see the work as minimalist, lifelong practice and cultural artifact.
  - Explore the site → Essays blend Asian philosophy and computing; prior book “Scheme 9 from Empty Space” praised for clear, well-commented bootstrapping.
  - Church-encoded lists → Proposed encoding drops one boolean per cell to detect nil; space-saving trade-off affects (ATOM NIL) semantics — counterpoint: ATOM NIL isn’t boolean.

- LLM perspective
  - View: A rare, compact path from evaluator to self-hosting compiler; pedagogy ties theory, history, and working code.
  - Impact: Best suited for students and language tinkerers; clarifies macros, lambda calculus, and bootstrapping more than it advances production tooling.
  - Watch next: Community walkthroughs, size/correctness benchmarks, ports of compiler output to other runtimes, plus a long-form interview.
