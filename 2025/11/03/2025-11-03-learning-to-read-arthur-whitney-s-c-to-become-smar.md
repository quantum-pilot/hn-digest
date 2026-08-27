# Learning to read Arthur Whitney's C to become smart (2024)

- Score: 316 | [HN](https://news.ycombinator.com/item?id=45800777) | Link: https://needleful.net/blog/2024/01/arthur_whitney.html

### TL;DR

The author spends eight hours unpacking Arthur Whitney’s roughly 50-line C interpreter for a small K-like array language. Dense macros, one-character names, implicit arguments, type punning, GCC extensions, and nested ternaries initially obscure the design, yet line-by-line reading reveals carefully composed primitives for atoms, vectors, errors, operators, and right-to-left evaluation. The exercise leaves the author valuing compact, well-modeled building blocks and less scrolling, while rejecting semantic ambiguity and gratuitous code golf. The deeper lesson is to model problems before coding them.

### Comment pulse

- Commenters debated whether APL or K familiarity explains the style, with some APL users saying much remains distinctly Whitney’s.
- Others praised the analysis while warning that macro shortcuts can undermine safety and team maintainability.

### LLM perspective

- View: Density becomes instructive when it exposes a coherent model, but terseness alone does not create clarity.
- Impact: Studying extreme code can sharpen reading skills without making its conventions suitable for production teams.
- Watch next: Whether extending the interpreter preserves its compact primitives or reveals their maintenance limits.
