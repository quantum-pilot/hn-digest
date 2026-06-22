# When I reject AI code even if it works

- Score: 217 | [HN](https://news.ycombinator.com/item?id=48614631) | Link: https://vinibrasil.com/when-i-reject-ai-code-even-if-it-works/

### TL;DR
The author uses AI coding agents but frequently discards their output, even when tests pass, because the cost has shifted from implementation to understanding and review. They reject AI code if they can’t explain it, if the diff is larger than the problem, if it adds premature abstractions, or if it makes the system harder to reason about. HN commenters echo the risk of hidden bugs, growing tech debt, and argue for using AI as a tightly controlled “power tool,” not an autonomous coder.

---

### Comment pulse
- AI often invents complex, unnecessary abstractions; on unfamiliar or low-stakes projects that’s tolerable, but in core systems it quietly accumulates dangerous tech debt.  
- Domain work (ML, payments) exposes subtle, high-impact errors that inexperienced devs and AI alike miss—counterpoint: same standards should apply regardless of whether code is human- or AI-written.  
- Some see AI use as all-or-nothing; others thrive in the middle ground, using it for snippets, translation, and grunt work while keeping architecture and review strictly human.

---

### LLM perspective
- View: Treat AI output like a junior’s PR: valuable drafts, but no merges without full human understanding and ownership.  
- Impact: Raises the bar for tests, code review discipline, and developer domain expertise, especially where failures are costly.  
- Watch next: Better agent constraints, “simplicity-first” prompts, and org policies defining where autonomous AI edits are allowed or strictly banned.
