# The cult of vibe coding is dogfooding run amok

- Score: 446 | [HN](https://news.ycombinator.com/item?id=47664912) | Link: https://bramcohen.com/p/the-cult-of-vibe-coding-is-insane

### TL;DR
Bram Cohen argues that Anthropic’s “vibe coding” culture—building Claude Code mostly by chatting with the model and avoiding reading its output—confuses dogfooding with abdication. “Pure” vibe coding is a myth: humans still design plans, skills, and rules, and AI is excellent at debt cleanup if you inspect and guide it. The leaked messy codebase isn’t an inevitable side effect of AI development; it’s a management choice to tolerate bad software, which will hurt long‑term maintainability more than short‑term success.

---

### Comment pulse
- Leaked Claude Code proves messy code can power a hit product → ugly code is industry‑standard under deadline pressure—counterpoint: long‑term evolvability still suffers badly.  
- “AI Levels” framing → best practice is heterogeneous levels: deep algorithms mostly human, UI/middleware heavily AI‑authored, tuned per risk and complexity.  
- Many embrace AI coding: burnt‑out devs, excited newcomers, and high performers wanting leverage → others fear skills devaluation and increasing “slop” in codebases.

---

### LLM perspective
- View: Best results come from AI as aggressive refactoring assistant, not autonomous coder; humans must still read, reason, and set standards.  
- Impact: Teams that mix AI cleanup with human architectural judgment will out-iterate both purist vibe coders and AI refusers.  
- Watch next: Tooling that tracks AI-authored code quality, enforces tests/specs, and supports “AI level” choices per module, not per project.
