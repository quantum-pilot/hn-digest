# Intuiting Pratt Parsing

- Score: 141 | [HN](https://news.ycombinator.com/item?id=47573450) | Link: https://louis.co.nz/2026/03/26/pratt-parsing.html

## TL;DR
- The article builds geometric intuition for Pratt parsing by viewing expression ASTs as left- or right-leaning depending on operator precedence. When precedence increases, the tree grows rightward; when it later decreases, you walk back up the right-leaning spine to attach a new left-leaning subtree. A simple recursive-descent parser with a `while` loop and distinct left/right binding powers (LBP/RBP) implements this walk-back and handles associativity. HN discussion mostly backs recursive descent + Pratt as the practical norm, with caveats for incremental parsing and some need for grammar theory.

## Comment pulse
- Recursive descent + Pratt is widely used → simple, fast, hand-written parsers for production languages; but incremental editors may require more sophisticated frameworks.
- Formal grammar theory still matters → understanding languages as abstract objects guides safe transformations and parser design—counterpoint: many engineers succeed with intuition and examples alone.
- Readers share resources like Pratt's original paper, talks, and tiny Tcl-like interpreters, showing multiple approachable paths to internalizing the technique.

## LLM perspective
- View: Pratt parsing offers a compact mental model for operator precedence that generalizes cleanly across languages and hand-written parsers.
- Impact: Lowers the barrier to implementing DSLs, interpreters, and calculators without committing to full parser-generator or compiler-theory stacks.
- Watch next: Explore error recovery, incremental parsing, and precedence table tooling layered atop Pratt to handle IDEs, refactoring, and large codebases.
