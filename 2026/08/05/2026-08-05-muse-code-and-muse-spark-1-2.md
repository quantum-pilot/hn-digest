# Muse Code and Muse Spark 1.2

- Score: 323 | [HN](https://news.ycombinator.com/item?id=49187575) | Link: https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2

### TL;DR

Meta has released Muse Code in beta, a terminal coding agent powered by Muse Spark 1.2. The harness pairs a main loop with persistent asynchronous subagents, records calls, tools, approvals, and edits in a replayable event log, and includes planning, plan-review, and goal-oriented skills. Spark 1.2 was co-trained for that environment using long-horizon repository work, harness trajectories, compaction, and self-generated tasks. Meta highlights complex debugging and a 24-hour GPU-kernel optimization case study; the model is available through Muse Code and Meta’s API.

### Comment pulse

- Contributor pricing is dramatically cheaper when users permit training on their data; commenters valued the transparency but flagged free-credit terms.
- Benchmark choices drew criticism because stronger frontier models often remained ahead.
- Some welcomed another competitor, while others urged Meta to resume publishing open weights.

### LLM perspective

- View: Persistent subagents and replayable state target reliability on long-running coding work.
- Impact: Harness-model co-training may matter as much as raw benchmark strength for practical agent performance.
- Watch next: Independent task results, data-retention defaults, open-weight availability, and recovery behavior in real repositories.
