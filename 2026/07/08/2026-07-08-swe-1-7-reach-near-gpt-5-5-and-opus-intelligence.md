# SWE-1.7 Reach Near GPT 5.5 and Opus Intelligence

- Score: 244 | [HN](https://news.ycombinator.com/item?id=48833866) | Link: https://cognition.com/blog/swe-1-7

## TL;DR
SWE-1.7 is presented as a software-engineering–optimized model claiming near-GPT‑5.5 / Claude Opus intelligence at lower cost, likely fine‑tuned from Kimi 2.7 on dev-tool logs. Hacker News commenters focus less on the tech and more on evaluation credibility: vendor-run code benchmarks appear inconsistent with third‑party leaderboards and omit strong baselines like GLM‑5.2, suggesting cherry-picking or train/eval overlap. Discussion broadens into trust in Cognition as a vendor, the difficulty of building truly coding‑specialized models, and the tradeoff between specialization and general reasoning.

*Content unavailable; summarizing from title/comments.*

## Comment pulse
- Benchmarks look self-serving → CursorBench ranks Cursor, Cognition’s bench ranks Cognition; Kimi/Kimi-derivative outperform GLM‑5.2 unlike on external sites—counterpoint: alignment to internal logs may be intentional.

- Eval philosophy → Teams optimize for their own KPIs and datasets; “benchmaxxing” and cherry-picking are common, so users should prefer independent, diverse eval suites.

- Beyond scores → Some ex-customers distrust Cognition’s pricing/support; others want cheap, coding‑focused (ideally local) models but note catastrophic forgetting and need for broad domain knowledge.

## LLM perspective
- View: Coding-specialist models are useful, but claims need cross-benchmark validation and strong baselines, including rival frontier and mid-tier models.

- Impact: Practitioners should treat vendor charts as marketing, favoring task trials, external leaderboards, and their own representative workloads.

- Watch next: Independent coding/agent benchmarks, smarter model routing between generalist and coder models, and capable local coders with transparent training/evals.
