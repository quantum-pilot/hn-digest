# Show HN: I made a heatmap diff viewer for code reviews

- Score: 160 | [HN](https://news.ycombinator.com/item?id=45760321) | Link: https://0github.com

- TL;DR
  - WebFetch’s Heatmap overlays GitHub diffs with LLM-scored “attention” colors, highlighting secrets, risky crypto modes, and gnarly logic. To use, swap github.com with 0github.com; the open-source service clones the repo, runs a model per diff, and renders a JSON-driven heatmap. HN likes the idea for triaging large or AI-generated PRs, but flags overbroad GitHub auth prompts, model cost/latency, and missing project context. Requests: configurable gradients, click-to-filter labels, CLI/IDE pre-PR runs, and learning reviewer style from past comments.

- Comment pulse
  - Overbroad GitHub auth → asks to 'act on your behalf'; public PRs shouldn’t need login — counterpoint: maintainer says anon PRs work; login prompt appears.
  - Expensive per-PR LLM scoring → unclear project context; propose change-frequency or bug-correlation heatmaps. Replies: free Gemini tiers, distillation, diff-entropy, but limited beyond-diff issues.
  - UX asks → configurable colors/labels, click-to-filter, mobile tooltips, CLI/IDE pre-PR runs; personalization via prior reviews (DSPy) desired.

- LLM perspective
  - View: Use as triage aid, not a correctness oracle; pair LLM scores with lightweight repo heuristics and past defect signals.
  - Impact: Cuts reviewer time on high-volume teams; concentrates attention on suspect tokens, not just changed lines.
  - Watch next: Add personal API keys, cache models, and offline heuristics; benchmark vs bug-introducing changes; integrate IDE/CLI and permission-scope hardening.
