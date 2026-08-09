# Julia Snail – An Emacs Development Environment for Julia Like Clojure's Cider

- Score: 141 | [HN](https://news.ycombinator.com/item?id=47295855) | Link: https://github.com/gcv/julia-snail

### TL;DR

Julia Snail gives Emacs a REPL-driven Julia environment modeled on SLIME and CIDER. Through vterm, Eat, or ghostel, it can evaluate lines, regions, functions, and files in the correct module; inspect a live image; complete symbols; jump to definitions; show documentation and plots; and connect to multiple, remote, or Docker REPLs. Optional extensions add history, formatting, Org Babel, and debugging. HN's sparse discussion welcomed file-plus-REPL workflows, wanted similar ergonomics for Haskell, and clarified that CIDER itself descended from SLIME.

### Comment pulse

- Runtime introspection complements static tooling → loaded Julia definitions drive module-aware completion and cross-references.
- Setup remains substantial → supported terminals, ports, Tramp, remote shell paths, and directory-local variables require coordination.
- Current gaps include local-variable completion, reference search, mature Org support, and end-to-end tests → maintainers already list them.

### LLM perspective

- **View:** This is a cohesive power-user bridge rather than an all-in-one IDE.
- **Impact:** Julia and Emacs users gain iterative workflows across local machines, clusters, and containers.
- **Watch next:** A pure-Elisp REPL, full test suite, local completion, Eldoc, and improved Windows support.
