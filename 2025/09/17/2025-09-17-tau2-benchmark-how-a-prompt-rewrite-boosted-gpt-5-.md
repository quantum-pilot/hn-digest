# Tau² benchmark: How a prompt rewrite boosted GPT-5-mini by 22%

- Score: 179 | [HN](https://news.ycombinator.com/item?id=45275354) | Link: https://quesma.com/blog/tau2-benchmark-improving-results-smaller-models/

- TL;DR
    - Using Tau²’s telecom agent benchmark, the authors boosted GPT-5-mini’s pass@1 from 0.55 to 0.675 by rewriting agent policies into concise, stepwise prompts (decision trees, explicit tool calls, binary checks, verification). Pass@2 rose 0.4→0.5 and “unsolvable” tasks halved. GPT-5-mini remains faster/cheaper and, with the rewrite, beat o3 while narrowing the gap to GPT-5. HN debate centered on eval design (Telecom grades outcomes, not references), reproducibility and prompt length effects, and the emergence of prompt-as-programming; the author later shared before/after prompts.

- Comment pulse
    - Prompting ≈ programming → Structured, imperative instructions reduce ambiguity and improve tool use — counterpoint: magic-words feel brittle and may shift with each model.
    - Telecom is the better eval → Outcome-state scoring avoids penalizing valid alternate solutions; Retail/Airline plateau from brittle reference grading.
    - Publish prompts/diffs → Transparency enables replication and ablations; may reveal length, not content, drove gains.

- LLM perspective
    - View: Use stronger models to refactor policies for smaller ones; codify into checklists and decision trees.
    - Impact: Near-flagship tool-use on routine tasks with lower latency and cost; raises baseline reliability.
    - Watch next: Prompt DSLs, ablation on structure vs brevity, cross-domain Tau² runs beyond Telecom.
