# Every layer of review makes you 10x slower

- Score: 493 | [HN](https://news.ycombinator.com/item?id=47408205) | Link: https://apenwarr.ca/log/20260316

- TL;DR
    - The author argues each extra approval layer slows work about 10x in wall‑clock time, because waiting and coordination dominate actual coding. AI accelerates writing code but not getting it approved, so more automation just feeds a clogged review pipeline or encourages skipping reviews and shipping low‑quality “slop.” He instead pushes Deming‑style systemic quality: fewer review layers, stronger automation, trust, and small modular teams that design quality in. HN discussion focuses on shifting reviews earlier, misaligned incentives, and keeping reviews lightweight but useful.

- Comment pulse
    - Shift-left advocates: replace reviews with upfront design sessions, dailies, pair programming, linters; 90% of issues disappear — counterpoint: architecture emerges during coding, management resists pairing.
    - Reviews as volunteer’s dilemma: authorship gets promotions, reviewers get little credit, so people prioritize shipping; yet reviewing teaches juniors and is core to effective leadership.
    - Optimize value/effort: keep reviews quick, focused on “does it work and not break things,” accept follow-up fixes; long nitpicky cycles just trigger the 10x slowdown.

- LLM perspective
    - View: Treat LLMs as accelerators for refactoring, testing, and boundary experiments, not excuses to bypass human judgment or process design.
    - Impact: Teams that shrink approval chains and invest in tests, linters, and ownership will benefit most from AI-generated speedups.
    - Watch next: Measure delivery time and defects as teams cut reviews, and benchmark LLM refactoring plus test-generation against human baselines.
