# AI World Clocks

- Score: 560 | [HN](https://news.ycombinator.com/item?id=45930151) | Link: https://clocks.brianmoore.com/

- TL;DR
    - A site generates nine AI-made analog clocks every minute from the same HTML/CSS prompt, exposing tradeoffs between accuracy and creativity across models; some clocks show wrong times. Viewers highlighted pronounced personality differences among models. Skeptics questioned authenticity, later attributing mismatches to time zones and model variability. People want raw code and pairwise voting. Broken clocks inspire design ideas. Discussion broadened to image models’ difficulty with “13-hour” clocks and novel twists on familiar concepts.
- Comment pulse
    - Kimi K2 is most reliable but bland; Qwen 2.5 is funniest/most erratic; K2 sometimes shows wrong time — counterpoint: prompt may suit K2’s training.
    - Authenticity concerns: misaligned numbers and time mismatch; later traced to timezone confusion, non-deterministic outputs, and a 2000-token limit affecting layout consistency.
    - Feature requests: click to view raw HTML/CSS per clock and a Facemash-style head-to-head ranking with a leaderboard of best designs.
- LLM perspective
    - View: A playful, rolling micro-benchmark of codegen-plus-CSS animation; surfaces accuracy, responsiveness, and stylistic variance.
    - Impact: Public, model-agnostic comparisons nudge vendors on reliability; designers gain unexpected patterns; prompts become a common testbed.
    - Watch next: Release datasets of outputs and timestamps; add deterministic seeds/user controls; track time-accuracy metrics; implement pairwise voting; test cross-browser rendering.
