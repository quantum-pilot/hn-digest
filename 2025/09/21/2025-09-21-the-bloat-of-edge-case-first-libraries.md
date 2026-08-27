# The bloat of edge-case first libraries

- Score: 125 | [HN](https://news.ycombinator.com/item?id=45319399) | Link: https://43081j.com/2025/09/bloat-of-edge-case-libraries

### TL;DR

The author argues JavaScript libraries should accept intended types, validate meaningful values at application boundaries, and stop paying ecosystem-wide costs for rare cases. Packages such as is-number, is-arrayish, pascalcase, and tiny shebang helpers illustrate dependency trees built from runtime checks and atomic utilities that native features can replace. Suggested remedies include stricter contracts, dependency visualization, and e18e replacements. Commenters countered that many packages encode real historical or cross-realm behavior; misuse by modern consumers, rather than their original existence, may be the problem.

### Comment pulse

- Some blamed dynamic typing and package-manager culture; others emphasized legacy JavaScript behavior and consumers carrying outdated dependencies forward.

### LLM perspective

- View: Common-path APIs should be the default, with unusual compatibility requirements made explicit and paid for deliberately.
- Impact: Removing obsolete micro-dependencies can reduce audit surface, installation churn, and hidden behavior without abandoning genuine compatibility needs.
- Watch next: Measure bundle reductions, dependency removal, supported runtimes, and whether replacements preserve the edge cases users actually require.
