# Show HN: TikZ Editor – WYSIWYG editor for figures in LaTeX

- Score: 311 | [HN](https://news.ycombinator.com/item?id=48645437) | Link: https://tikz.dev/editor/

### TL;DR
A new open‑source WYSIWYG TikZ editor lets users draw figures visually and get LaTeX/TikZ code, targeting students and researchers who dislike hand‑coding diagrams. The author reports building it heavily with Codex/ChatGPT (≈700M tokens), illustrating how consumer subscriptions can subsidize serious dev work. Power users criticize the “naive” output: everything uses absolute coordinates instead of TikZ’s relative positioning and anchors, trading readable, idiomatic code for predictable editing behavior. Discussion compares it with specialized diagram tools and praises TikZ’s impact on academic communication.  
*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Massive LLM-assisted development → ~700M tokens via Codex/ChatGPT made a solo side project feasible, effectively converting subscription time into significant engineering capacity.  
- Code-quality concern → Editor emits absolute coordinates and ignores TikZ idioms like anchors, making output less maintainable—counterpoint: relative code complicates later interactive edits.  
- Ecosystem context → Users mention q.uiver, TikZiT, circuit2tikz, TikZ-CD, LyX, showing strong demand for domain-specific LaTeX diagram editors in math/CS workflows.

---

### LLM perspective
- View: Hybrid WYSIWYG+code is ideal: visual authoring, then optional refactoring into idiomatic TikZ for power users.  
- Impact: Students and non-expert LaTeX users gain access to TikZ quality without its steep learning curve.  
- Watch next: Features like “beautify TikZ code” and CAD-like constraint systems could bridge editable geometry with human-readable source.
