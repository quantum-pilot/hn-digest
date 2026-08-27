# Auto-grading decade-old Hacker News discussions with hindsight

- Score: 255 | [HN](https://news.ycombinator.com/item?id=46220540) | Link: https://karpathy.bearblog.dev/auto-grade-hn/

### TL;DR

Andrej Karpathy built an HN “time capsule” that gathers December 2015 front pages, articles, and full comment threads, then asks GPT-5.1 Thinking to summarize outcomes, award prescience grades, and score retrospective interest. Opus 4.5 helped produce the pipeline in roughly three hours; 930 analysis calls reportedly cost $58 and ran for about an hour. The resulting archive and leaderboard are entertaining, but commenters question whether free-form historical claims can be objectively resolved and whether predictable, low-information opinions deserve high grades.

### Comment pulse

- “Boring” predictions often age well → critics argue accuracy should be weighted by how surprising a claim was initially.
- Reputation scoring sounds useful → ambiguity, grader randomness, private upvotes, and underspecified predictions make durable rankings difficult.

### LLM perspective

- View: Hindsight synthesis is compelling archival browsing, but a model-generated leaderboard should not be mistaken for calibrated forecasting skill.
- Impact: Cheap batch analysis can make old discussions searchable while also attaching questionable reputational judgments to users.
- Watch next: Multiple graders, explicit resolution criteria, confidence calibration, and reproducibility tests would expose ranking instability.
