# Sabotaging projects by overthinking, scope creep, and structural diffing

- Score: 345 | [HN](https://news.ycombinator.com/item?id=47890799) | Link: https://kevinlynagh.com/newsletter/2026_04_overthinking/

### TL;DR
The author describes how side projects die when he over-researches prior art, lets scope creep explode, or chases “perfect” designs—versus thriving when he defines small, personal success criteria and just builds. A fuzzy file-search feature and structural diff tooling send him down rabbit holes (anchors, AST algorithms, LLM-assisted overengineering) before he rediscovers YAGNI and cuts back to a minimal Emacs+Tree‑sitter prototype for reviewing LLM-generated code. Core lesson: optimize for learning-by-doing, not imagined future users or theoretical completeness.

---

### Comment pulse
- PhD research exemplifies scope creep → reading “all related work” drains momentum; better: start from a few papers, deepen survey after results.
- Perfectionism kills output → “better is good” and “don’t let perfect be the enemy of good” encourage shipping small, compounding improvements.
- Start by building, then research → practice-first projects teach constraints; deep prior-art study helps only once you’ve hit real-world walls.

---

### LLM perspective
- View: LLMs accelerate code generation but also amplify scope creep; plans and “nice-to-haves” balloon because they’re so cheap to explore.
- Impact: Solo devs and small teams must tighten success criteria and aggressively delete features to actually ship.
- Watch next: Lightweight, in-editor structural diff tools tailored for human-in-the-loop LLM workflows, with benchmarks on readability and review speed.
