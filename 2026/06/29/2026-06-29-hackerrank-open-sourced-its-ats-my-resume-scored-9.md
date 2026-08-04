# HackerRank open sourced its ATS. My resume scored 90/100. Oh wait 74. No – 88

- Score: 943 | [HN](https://news.ycombinator.com/item?id=48713832) | Link: https://danunparsed.com/p/hackerrank-open-source-ats

### TL;DR

Testing HackerRank’s open-source hiring agent 100 times on one unchanged résumé produced scores from 66 to 99; at an 85 cutoff, it failed 65% of runs. Gemini and Opus narrowed but retained variation. Checklist-like skills were stable, subjective project scores fluctuated, and an unanchored experience rubric awarded 25/25 to both an internship résumé and a senior one. HN debated nondeterminism and discrimination risk, while some hiring managers argued applicant volume makes crude filtering operationally useful—countered that random rejection adds no quality signal and rewards free-time-heavy portfolios.

### Comment pulse

- Temperature zero is not enough operationally → batching, floating-point kernels, MoE routing, and infrastructure choices can still alter outputs.
- The rubric embeds socioeconomic preference → 65% for open source and projects disadvantages caregivers, private-code workers, and people with multiple jobs.
- Random filtering can manage volume → counterpoint: without correlation to job performance, it discards qualified candidates without improving selection.

### LLM perspective

- **View:** A score is not a measurement when repeated identical inputs lack stable, calibrated meaning.
- **Impact:** Applicants face opaque luck; employers inherit bias, compliance, and false-negative risk.
- **Watch next:** Require repeated-run variance, subgroup audits, criterion validity, human review, and appeal paths before deployment.
