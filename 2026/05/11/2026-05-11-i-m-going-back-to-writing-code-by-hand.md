# I'm going back to writing code by hand

- Score: 911 | [HN](https://news.ycombinator.com/item?id=48090029) | Link: https://blog.k10s.dev/im-going-back-to-writing-code-by-hand/

### TL;DR
Developers report that letting LLMs “vibe-code” entire features or systems leads to bloated, tangled, fragile codebases and a loss of architectural clarity. Models are reasonably effective for local, mechanical work (simple migrations, boilerplate, tests, some math-heavy routines) but repeatedly violate invariants and can’t step back when specs or constraints fundamentally change. Many commenters are retreating to a hybrid approach: humans design architecture and core abstractions, keep a tight mental model, and use AI only as a constrained, well-reviewed coding assistant.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- LLMs mis-handle invariants and changing specs → they contort code around wrong assumptions; only humans can judge when to change architecture vs bolt-on hacks.  
- Heavy agent use creates “comprehension debt” → you ship more code than you understand, lose mental models, and later changes become risky, slow, and demoralizing.  
- Used carefully, AI boosts experts on mechanical tasks and mathy code → big speedups on known designs—counterpoint: novices over-trust output, yielding fragile, spaghetti architectures.

---

### LLM perspective
- View: Treat AI-generated code like an external library: constrained interfaces, strong tests, and explicit ownership, not as an autonomous teammate.  
- Impact: Teams that formalize “AI coding guidelines” and review standards will outperform both laissez-faire vibe coders and AI refusers.  
- Watch next: languages, IDEs, and agents co-designed for local reasoning and invariants, plus tooling that tracks and caps comprehension debt.
