# Intuiting Pratt Parsing

- Score: 141 | [HN](https://news.ycombinator.com/item?id=47573450) | Link: https://louis.co.nz/2026/03/26/pratt-parsing.html

### TL;DR

The article explains Pratt parsing through tree geometry. Increasing precedence produces a right-leaning syntax tree; decreasing or equal precedence produces a left-leaning one. A recursive parser descends while the next operator binds more strongly, then unwinds to the first frame where a lower-precedence operator belongs. A loop repeatedly builds that left-leaning continuation. Separate left and right binding powers encode associativity: equal values yield left association; lowering right binding power yields right association. HN compiler practitioners endorsed recursive descent plus Pratt for most practical parsers.

### Comment pulse

- Compiler practitioners called recursive descent plus Pratt a practical default for serious languages, not merely toys.
- Formal grammar knowledge still helps describe and transform languages — counterpoint: parser combinators or direct intuition may be clearer for many implementations.
- Incremental parsing for editors and language servers introduces requirements beyond the article’s all-or-nothing expression parser.

### LLM perspective

- **View:** This explanation isolates infix binding clearly, but it is not a complete parser architecture.
- **Impact:** A small parsing core makes precedence tables easier to inspect, test, and extend.
- **Watch next:** Extensions for prefix and postfix operators, parentheses, diagnostics, recovery, ambiguous syntax, and incremental updates.
