# Date is out, Temporal is in

- Score: 290 | [HN](https://news.ycombinator.com/item?id=46589658) | Link: https://piccalil.li/blog/date-is-out-and-temporal-is-in/

### TL;DR

Mat Marquis argues JavaScript’s Date API combines inconsistent parsing, limited time-zone semantics, and mutable objects that can silently change shared date values. Temporal replaces the all-purpose constructor with specialized types and plain-language operations; methods such as add and subtract return new Temporal objects instead of altering the original. The proposal is at stage three and available experimentally in Chrome and Firefox. HN readers supplied the web-compatibility history behind broken ISO parsing, debated whether mutability is the central flaw, and noted unresolved leap-second support.

### Comment pulse

- Broken ISO parsing persists for compatibility → correcting absent-offset behavior broke sites, so browsers retained the earlier UTC interpretation.
- Mutability is not Date’s worst flaw → critics prioritized parsing and timezone semantics — counterpoint: shared mutable instances invite nonlocal bugs.
- Temporal remains incomplete for specialists → astronomical calculations still need externally maintained leap-second data because browser APIs expose POSIX-like time.

### LLM perspective

- View: Temporal improves correctness chiefly by making temporal intent explicit and transformations value-preserving.
- Impact: Developers can retire large workaround libraries and reduce bugs from ambiguous parsing, timezone conversion, and accidental mutation.
- Watch next: Track specification completion, cross-browser rollout, migration guidance, bundle savings, and decisions on leap-second access.
