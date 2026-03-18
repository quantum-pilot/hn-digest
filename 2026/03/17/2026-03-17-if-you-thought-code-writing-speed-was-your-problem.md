# If you thought code writing speed was your problem you have bigger problems

- Score: 294 | [HN](https://news.ycombinator.com/item?id=47415919) | Link: https://andrewmurphy.io/blog/if-you-thought-the-speed-of-writing-code-was-your-problem-you-have-bigger-problems

## TL;DR
- The essay argues that AI coding tools “speeding up developers by 40%” usually optimize the wrong part of the system. Using Theory of Constraints, it says the true bottlenecks are deciding what to build, review and deployment queues, coordination and calendar waits, and learning whether features actually solve user problems. Turning up code throughput just inflates WIP, increases risk, and reduces understanding of the system. Real gains come from mapping the value stream, measuring cycle time, and killing wait states and bad incentives. HN comments add nuance on AI’s tactical usefulness, human fatigue, and long‑term maintainability.

## Comment pulse
- AI agents shine on refactors, boilerplate, and edge cases, yet “work while it codes” workflows cause heavy context switching, exhaustion, and a less satisfying craft.  
- Some argue faster coding aids problem discovery via cheap prototypes; others reply real bottleneck is scarce customer feedback, like talking faster doesn’t improve understanding.  
- Viewing source as disposable IR, written by agents, meets pushback: compiler output is deterministic and formal; LLM code is non‑deterministic, semantic‑lossy, and accumulates debt.

## LLM perspective
- View: AI coding helps most in orgs that already fixed flow—then faster implementation actually moves the end‑to‑end needle.  
- Impact: Shift metrics from output counts to cycle time, incident rates, and outcome validation, or AI-boosted throughput quietly worsens systems.  
- Watch next: Empirical studies comparing AI and non‑AI teams’ lead time, failure rates, and on‑call load, not just PRs merged.
