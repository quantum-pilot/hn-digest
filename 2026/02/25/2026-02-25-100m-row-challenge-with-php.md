# 100M-Row Challenge with PHP

- Score: 164 | [HN](https://news.ycombinator.com/item?id=47149752) | Link: https://github.com/tempestphp/100-million-row-challenge

### TL;DR

The PHP community’s two-week challenge asks entrants to parse 100 million CSV page visits into pretty-printed JSON, grouped by URL and date, before March 15. Submissions run on the same 2-vCPU, 1.5-GB server; FFI and JIT are disabled, results are manually validated, and the three fastest win prizes. HN discussion treated it as both language benchmark and systems exercise: sorting a 7-GB input dominated one shell attempt, while commenters proposed in-memory aggregation or SQLite and debated whether using other tools misses the point.

### Comment pulse

- Aggregation strategy dominates → one shell pipeline spent roughly 20 minutes sorting, while the small key space favors counting in memory.
- A uniform machine and secret dataset improve comparability → manual runs and originality checks still limit leaderboard speed and reproducibility.
- The language constraint drives learning → counterpoint: production engineers might choose SQLite, shell tools, Go, or Rust instead.

### LLM perspective

- **View:** The benchmark rewards data layout and I/O choices more than clever syntax.
- **Impact:** Participants get a concrete profiler-driven lesson in PHP’s performance envelope.
- **Watch next:** Final runtimes, memory ceilings, validation disputes, and whether multicore designs dominate.
