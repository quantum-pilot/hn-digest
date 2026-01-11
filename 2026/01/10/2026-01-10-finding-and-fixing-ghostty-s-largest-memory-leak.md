# Finding and fixing Ghostty's largest memory leak

- Score: 162 | [HN](https://news.ycombinator.com/item?id=46568794) | Link: https://mitchellh.com/writing/ghostty-memory-leak-fix

### TL;DR
Ghostty, a GPU-accelerated terminal, had a long-standing memory leak where certain large text “pages” allocated via `mmap` were never `munmap`’d. A scrollback optimization reused old pages by changing metadata but not the underlying allocation size, causing large pages to be misclassified as pool pages and leaked on free. Workloads with lots of complex Unicode (like Claude Code and some TUIs) finally exposed it at scale. The fix: never reuse oversized pages and add macOS VM tagging plus regression tests.

---

### Comment pulse
- Some users hit the leak without Claude Code → suggests non-standard pages can appear in more workflows than assumed—counterpoint: benchmarks still show standard pages dominate.
- Concern about shipping fix only in a future feature release → expectation that severe memory bugs receive a faster, targeted bugfix release.
- Developers report OOMs in Unicode-heavy TUIs → reinforces that multi-codepoint glyphs and resizing can stress terminal memory systems in non-obvious ways.

---

### LLM perspective
- View: Mixing pooling with special-case allocations is brittle; metadata and allocation size must stay tightly coupled or be assert-checked.
- Impact: Terminal, editor, and game engine authors should re-audit pooling + “hot path” optimizations under pathological but realistic workloads.
- Watch next: Telemetry on non-standard page frequency, allocator tagging on more OSes, and possibly dynamic strategies for when to keep oversized pages.
