# Will It Mythos?

- Score: 305 | [HN](https://news.ycombinator.com/item?id=48640196) | Link: https://swelljoe.com/post/will-it-mythos/

### TL;DR

A nine-bug benchmark asks whether public models can match Mythos at finding recently disclosed, real-world vulnerabilities without hints beyond a target file. Results are too sparse for firm rankings: one run per bug, uneven completion, network access, and one model’s retries. Still, several models found four of nine; inexpensive MiMo and DeepSeek competed with Opus 4.8 and GPT 5.5, while Mythos alone found four bugs no contestant detected. HN debated whether Mythos’s edge comes from weaker guardrails, larger scale, or an autonomous security-specific harness, and urged statistical caution.

### Comment pulse

- Leaderboard certainty is overstated → a commenter’s Wilson lower-bound adjustment demoted GPT 5.5 Pro’s incomplete 2/4 result and favored complete 4/9 cohorts.
- Mythos’s advantage is disputed → some attribute it to relaxed safeguards or scale — counterpoint: others credit autonomous, security-trained tooling and self-direction.
- Model impressions need receipts → commenters valued shared transcripts but warned that prose quality, remembered degradation, and complex-task anecdotes are weak substitutes for blinded metrics.

### LLM perspective

- **View:** Several models could explain each corpus bug when directed, separating recognition from blind discovery.
- **Impact:** Full-featured agents increased cost and token use without improving detections, weakening the assumption that more orchestration yields better audits.
- **Watch next:** Run repeated, network-disabled trials with identical harnesses, budgets, blinded judging, confidence intervals, and per-bug recall and false-positive reporting.
