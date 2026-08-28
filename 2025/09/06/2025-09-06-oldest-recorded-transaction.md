# Oldest recorded transaction

- Score: 181 | [HN](https://news.ycombinator.com/item?id=45149626) | Link: https://avi.im/blag/2025/oldest-txn/

### TL;DR

A clay tablet recording malt and barley accounts around 3100 BCE inspired a database date-range experiment. MySQL dates begin at 1000 CE, so it cannot represent the tablet directly; PostgreSQL and SQLite extend to 4713 BCE. The deeper problem is that historical dates are often approximate rather than exact. Commenters suggested text, ranges, or a timestamp-plus-margin type, and noted that early writing frequently recorded goods and quantities. The tablet is best described as among the oldest known transaction records, not necessarily the first.

### Comment pulse

- Accounting may have helped drive writing because quantities and obligations are harder to preserve reliably through oral memory.
- Museum systems need sortable uncertainty, including circa dates, intervals, disputed chronologies, and records older than ordinary database types.

### LLM perspective

- View: Ancient data exposes a modeling gap: historical time is often uncertain, not merely outside modern timestamp ranges.
- Impact: Archives need representations that preserve ambiguity without sacrificing comparison, sorting, or query semantics.
- Watch next: Explicit date-range types, uncertainty metadata, BCE interchange conventions, and database behavior across calendar systems.
