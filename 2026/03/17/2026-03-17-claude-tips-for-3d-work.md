# Claude Tips for 3D Work

- Score: 195 | [HN](https://news.ycombinator.com/item?id=47365299) | Link: https://www.davesnider.com/posts/claude-3d

## TL;DR
Author describes using Claude Code as a main coding partner for complex 3D web apps, but notes that LLMs still fail at pure spatial reasoning. His fix is to build a tooling “language”: scripts that regenerate geometry, capture multi-angle screenshots, move the camera, and drop visible markers. Claude then runs a loop of edit → render → visually self-check without human prompting. HN commenters echo this tooling-first mindset, highlight cost concerns, and share mixed experiences using LLMs to script CAD and parametric models.

---

## Comment pulse
- Automated screenshot-driven refinement boosts 3D reliability but can 3–4× token and compute costs, so some teams keep it disabled until prices fall.  
- Developers increasingly front-load work into tiny CLI tools and geometry scripts so models operate within clear verbs and views instead of free-form descriptions.  
- People disagree on what to hand-code: some outsource ubiquitous CSS/UI to LLMs, others safeguard favorite layers—counterpoint: everyone wants control over architecture patterns.

---

## LLM perspective
- View: Treat the model as a visually impaired agent that needs instruments—cameras, markers, scripts—rather than as an all-seeing designer.  
- Impact: 3D, CAD, robotics, and game tools can embed such loops to offload tedious geometry iteration while humans handle taste.  
- Watch next: benchmark such toolchains on cost, speed, and failure modes to learn when automated visual feedback beats manual tweaking.
