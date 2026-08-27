# Forth: The programming language that writes itself

- Score: 307 | [HN](https://news.ycombinator.com/item?id=45639250) | Link: https://ratfactor.com/forth/the_programming_language_that_writes_itself.html

### TL;DR

The essay explains Forth as a tiny extensible system where whitespace-separated words are looked up in a dictionary and either executed or compiled. Because defining words, control structures, comments, variables, and even assembly tools can themselves be ordinary Forth words, the language can bootstrap and reshape itself with little machinery. The author’s failed all-inlining experiment reinforced why Forth’s spare design choices matter. Historical examples illustrate its fit for constrained, interactive systems, while comments note that implementation insight does not automatically produce maintainable Forth programs.

### Comment pulse

- Several commenters recalled Forth succeeding on tiny or unusual hardware where interactive control and compactness mattered.
- Others admired its language-building power but found stack-state reasoning and readable application design difficult.

### LLM perspective

- View: Forth is most revealing as a transparent model of how interpreters, compilers, and domain languages can share machinery.
- Impact: Its ideas remain useful for embedded work and language education even when Forth itself is unsuitable.
- Watch next: Compare compact implementations with real maintenance, debugging, and team-comprehension costs.
