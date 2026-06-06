# Vibe coding and agentic engineering are getting closer than I'd like

- Score: 346 | [HN](https://news.ycombinator.com/item?id=48037128) | Link: https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/

## TL;DR
Willison contrasts “vibe coding” (non‑ or semi‑programmers shipping unreviewed AI code, OK only for personal tools) with “agentic engineering” (experienced engineers using AI under professional constraints). He’s disturbed to find himself no longer reviewing every line of agent‑written production code, likening growing trust to normalization of deviance. As AI makes spinning up polished repos trivial, the real quality signal becomes sustained real‑world use. Output is no longer scarce; the bottlenecks shift to design, evaluation, and accountability, not typing.  

## Comment pulse
- “Claude will just do a JSON endpoint right” is disputed → API shape, edge cases, architecture and future changes still need deep human design work.  
- LLMs amplify existing discipline or its absence → bloated, ownerless codebases and pressure to skip reviews — counterpoint: best use is as “rubber duck” and for TDD.  
- More code isn’t more value → LOC helps estimate review burden; people report AI generating 10k LOC where 1.5k hand‑written suffices, and deletions often matter more.  

## LLM perspective
- View: Treat AI agents like junior vendors: demand tests, docs, and runtime evidence, but assume zero inherent trust or accountability.  
- Impact: Engineering practices must rebalance toward specification quality, review strategy, observability, and deprecation, not raw implementation speed.  
- Watch next: Longitudinal studies on AI‑heavy codebases’ maintenance cost, incident rates, and refactor difficulty compared with mostly human‑written systems.
