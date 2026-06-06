# An AI coding agent, used to write code, needs to reduce your maintenance costs

- Score: 347 | [HN](https://news.ycombinator.com/item?id=48089289) | Link: https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs

### TL;DR
The article models engineering productivity as dominated by long‑term maintenance, not initial feature throughput: every extra month of code creation incurs years of support, bug fixes, upgrades, and rework. Applying this to AI coding agents, a tool that only speeds up code generation—without *reducing per‑unit maintenance cost by at least the same factor*—actually makes you worse off long term, even if you later stop using it. HN commenters report mixed realities: AI can greatly ease legacy work, but also encourages low‑understanding code sprawl and subtle, hard‑to-review bugs.

---

### Comment pulse
- AI can significantly ease legacy maintenance → faster upgrades, deletions, diagnostics, tests across many services. — counterpoint: indiscriminate AI use also correlates with more outages and unread, poorly understood code.  
- Maintainability isn’t “non‑functional” → it preserves future feature capacity; renaming it as quality/operational characteristics helps prevent it being deprioritized.  
- AI shifts maintenance work → less manual coding, more complex review/debug of fluent but subtly wrong AI code; net benefit depends on team rigor.

---

### LLM perspective
- View: Track maintenance explicitly (bug rate, MTTR, time-on-refactors) before and after AI; otherwise “productivity” numbers are misleading.  
- Impact: Engineering leads and vendors should design agents that prioritize refactoring, deletion, and simplification over raw LOC output.  
- Watch next: Longitudinal studies of AI-heavy codebases and tools focused on safe code removal, dependency reduction, and automated regression testing.
