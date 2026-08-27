# A Note on Fil-C

- Score: 227 | [HN](https://news.ycombinator.com/item?id=45842494) | Link: https://graydon2.dreamwidth.org/320265.html

### TL;DR

Fil-C adds dynamic spatial memory checks to Clang-compiled C and uses a concurrent garbage collector for temporal safety, aiming to protect existing code with unusually high compatibility. The author welcomes its practical path for legacy systems, citing reported CPU overhead around 1–4× while observing wider results and roughly 3–6× memory use in initial tests. Unlike Rust, Fil-C catches errors at runtime rather than statically, does not prevent data races, and can be disabled for performance. Its value depends on organizations keeping safety enabled.

### Comment pulse

- Supporters emphasized turning exploitable memory corruption into crashes without rewriting mature C applications.
- Critics questioned library interoperability and the performance-sensitive niches where C dominates; others said many applications can absorb the cost.
- Fil-C’s creator attributed current compatibility and acceptable performance to the recent InvisiCaps design, not a sudden hardware breakthrough.

### LLM perspective

- View: Fil-C trades proof and peak efficiency for deployability across code that organizations are unlikely to rewrite.
- Impact: Security-sensitive C applications gain an incremental hardening path, while libraries and low-level systems remain harder targets.
- Watch next: Distribution-scale builds, representative benchmarks, ABI interoperability, memory tuning, and production crash data.
