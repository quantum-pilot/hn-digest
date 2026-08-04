# (How to Write a (Lisp) Interpreter (In Python)) (2010)

- Score: 160 | [HN](https://news.ycombinator.com/item?id=48619831) | Link: https://norvig.com/lispy.html

### TL;DR

Peter Norvig builds Lispy, a compact Scheme interpreter in Python, to explain language implementation from first principles. The tutorial separates parsing from evaluation, tokenizes parentheses into nested Python lists, maps names through environments, adds a REPL, then extends the evaluator with quotation, assignment, lambdas, closures, and lexical scope. The result is 117 nonblank, noncomment lines and 4KB, intentionally omitting tail recursion, robust errors, many data types, and much of Scheme. HN regards it as an enduring entry point, while recommending language-agnostic Make-A-Lisp and smaller full-Scheme implementations for follow-up.

### Comment pulse

- The tutorial remains evergreen → repeated HN appearances since 2010 continue attracting readers because a minimal evaluator exposes universal language concepts.
- Make-A-Lisp broadens the exercise → its host-language-neutral progression lets learners test unfamiliar languages while discovering each ecosystem’s idioms.
- Tiny need not mean toy syntax → Ribbit reportedly fits a full R4RS REPL with tail calls into 8KB JavaScript or 6.5KB x86.

### LLM perspective

- **View:** Interpreter construction is unusually high-leverage pedagogy: one small program connects syntax, scope, functions, data representation, and execution.
- **Impact:** Developers gain a concrete model for compilers, DSLs, configuration languages, templating systems, query engines, and runtime debugging.
- **Watch next:** Extend Lispy with tail calls, macros, continuations, source locations, tests, and structured errors; compare complexity added per feature.
