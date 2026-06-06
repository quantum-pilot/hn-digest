# Using AI to write better code more slowly

- Score: 1135 | [HN](https://news.ycombinator.com/item?id=48272984) | Link: https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/

## TL;DR
Lawson argues against “slop cannon” AI coding and instead uses LLMs to *slow down* and raise code quality. He orchestrates several models as adversarial reviewers on each PR, ranking findings by severity, then iteratively fixes critical/high issues and often uncovers pre‑existing bugs. This doesn’t boost raw velocity and burns tokens, but improves architecture, documentation, and team understanding. HN commenters largely echo this: multi-pass, multi-model review loops are slower, sometimes no faster than hand-coding, yet yield v3-quality code on v1 features.

---

## Comment pulse
- Multi-model, multi-pass workflows → people design with one model, implement with another, then cross-review; high quality but time- and token-intensive — counterpoint: some report equal speed by just hand-coding.  
- AI as thinking partner → devs use LLMs for specs, architecture debates, repo skeletons and “grill me” skills, often preferring human-led implementation for enjoyment and control.  
- Learning and onboarding → juniors and seniors alike use back-and-forth critique to explore alternatives; AI errors become “trick questions” that deepen conceptual understanding.  

---

## LLM perspective
- View: Treat LLMs as adversarial reviewers and co-designers; reserve final authorship and judgment for humans.  
- Impact: Raises baseline review quality, formalizes team standards, and gives juniors safer exposure to gnarly edge cases.  
- Watch next: Tooling that natively coordinates multiple models/personas per PR and reports outcomes against real bug/incident metrics.
