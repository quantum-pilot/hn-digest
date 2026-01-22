# Anthropic's original take home assignment open sourced

- Score: 597 | [HN](https://news.ycombinator.com/item?id=46700594) | Link: https://github.com/anthropics/original_performance_takehome

### TL;DR
Anthropic open‑sourced its original performance engineering take‑home: a tiny virtual‑machine program you must hand‑optimize for fewer simulated clock cycles. The README lists progressively better solutions from Claude Opus/Sonnet models, down to 1,363 cycles in internal harnesses, with top human results even lower and unpublished. Anyone beating 1,487 cycles can email code as a recruiting signal. HN readers debate feelings of inadequacy vs specialization, fairness of long take‑homes, and early benchmarks of various LLM agents on the task.

### Comment pulse
- Humbling but specialized problem → low-level performance tuning is niche; struggling reflects unfamiliarity, not lack of intelligence or long-term learning ability.  
- Recruiting via open challenge → nicer than LeetCode, but week-long unpaid projects feel unrealistic and non-transferable — counterpoint: it's optional, just one strong-signal path.  
- Community benchmarking LLMs → naive runs show GPT‑5 beating some Claude baselines, others looping or stalling; humans still best with ~1112‑cycle hand-tuned solutions.  

### LLM perspective
- View: Public, game-like micro-optimization tasks expose concrete LLM weaknesses in reasoning about unfamiliar instruction sets and global program structure.  
- Impact: Encourages performance-minded engineers to systematically probe models, while giving Anthropic an unusual but precise hiring filter.  
- Watch next: Open-source harnesses comparing many models, hybrid human+agent workflows, and whether sub‑1000‑cycle strategies become widely known or retained.
