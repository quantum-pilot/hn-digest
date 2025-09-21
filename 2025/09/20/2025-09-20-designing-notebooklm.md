# Designing NotebookLM

- Score: 140 | [HN](https://news.ycombinator.com/item?id=45315312) | Link: https://jasonspielman.com/notebooklm

- TL;DR
  - Google Labs’ NotebookLM design lead outlines how the product evolved from prototypes to a three-panel, AI-first workspace built around Inputs → Chat → Outputs, aiming to end “tab overwhelm” and support reading, writing, and creation in one place. He highlights responsive layouts, Audio Overviews, and a brand system, emphasizing fast, user‑informed iteration. HN readers praise the ambition but call the UX overdesigned with low information density, scaling issues on small screens, and unstable controls, preferring simpler “chat with documents” tools like Claude; the author engages and commits to improving.

- Comment pulse
  - Overdesigned UX → Low information density and crowded controls obscure the “chat with my files” core task; portfolio page mirrors this with scrolljacking and carousels.
  - Feature sprawl hurts usability → Tall artifacts panel, narrow notes sidebar, unstable follow-ups; small-screen users resort to Tampermonkey fixes — counterpoint: team promises adjustments.
  - Value question vs alternatives → Some prefer Claude Projects/CLI for simple document chat; others find NotebookLM’s integrated, source-grounded approach compelling for learning.

- LLM perspective
  - View: 3-panel anchored by chat is sensible for AI-native creation, but must not bury primary intents under options.
  - Impact: Success depends on small-screen ergonomics, progressive disclosure, and stability; otherwise users defect to simpler project/file chat workflows.
  - Watch next: Consolidation of artifacts/actions, flexible note sizing, benchmarks vs Claude Projects; public bug tracker and UX telemetry guiding de-bloat.
