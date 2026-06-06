# Python 3.15: features that didn't make the headlines

- Score: 321 | [HN](https://news.ycombinator.com/item?id=48220696) | Link: https://blog.changs.co.uk/python-315-features-that-didnt-make-the-headlines.html

### TL;DR
Python 3.15 ships several under‑the‑radar but practical upgrades: `asyncio.TaskGroup.cancel()` for cleanly stopping groups of tasks; smarter `ContextDecorator` so context-manager-as-decorator now correctly wraps async functions and generators; new iterator synchronization helpers in `threading` for safe multi-threaded consumption; a completeness-focused xor operator for `collections.Counter`; and support for fully immutable JSON structures via `frozendict` plus `array_hook`. HN discussion centers on lazy imports, iterator utilities vs third‑party packages, and concerns about subtle behavioral changes and odd Counter semantics.

---

### Comment pulse
- Lazy imports spark confusion and criticism → seen as a band-aid for huge, AI-inflated codebases; some argue big users should adopt more “industrial” languages instead.  
- New iterator sync primitives → commenters welcome a stdlib solution and note overlap with existing generator+queue packages—counterpoint: may obsolete small ecosystem tools.  
- Mathematicians and maintainers worry → Counter xor on multisets feels unnatural; ContextDecorator behavior change could silently alter existing code, and the post’s Counter example is factually wrong.

---

### LLM perspective
- View: These “small” additions mostly target ergonomics and safety in async, threading, and large codebases, not just syntax sugar.  
- Impact: Library authors, framework maintainers, and infra teams gain cleaner cancellation, safer concurrency patterns, and more expressive immutable data handling.  
- Watch next: Benchmarks for lazy imports and iterator primitives; real-world breakages from ContextDecorator changes; patterns for immutable JSON in caching and config systems.
