# (How to Write a (Lisp) Interpreter (In Python)) (2010)

- Score: 160 | [HN](https://news.ycombinator.com/item?id=48619831) | Link: https://norvig.com/lispy.html

## TL;DR
- Norvig builds “Lispy,” a tiny Scheme dialect implemented in ~100 lines of Python 3, to teach how interpreters work end‑to‑end.  
- He starts with a calculator‑like subset: a tokenizer and recursive descent parser produce nested Python lists as the AST; `eval` walks these trees using a global environment of primitive functions.  
- Then he adds `quote`, `set!`, and `lambda`, introducing an `Env` class with lexical scoping and a `Procedure` closure type, plus a REPL.  
- HN discussion treats this as a perennial classic for learning language implementation, comparing it to MAL, Crafting Interpreters, and newer tiny Lisps and ports.

## Comment pulse
- This tutorial is an HN evergreen → resurfaced many times over the years as a canonical “first interpreter” reference.  
- Folks build variants → Rust port without linked lists; Ribbit offers a full R4RS, tail‑call‑optimized REPL in a few kilobytes.  
- Learning path advice → start here for intuition, then move to Crafting Interpreters or MAL for language‑agnostic, step‑by‑step practice.

## LLM perspective
- View: Implementing Lispy yourself solidifies parsing, evaluation, environments, and closures more than passively reading about them.  
- Impact: Especially valuable for engineers doing compilers, DSLs, config languages, or embedded scripting.  
- Watch next: Extend Lispy with macros, errors, and tail‑calls; compare against bytecode or WASM backends for performance and embedding.
