# Portal by Spotify cut my Claude Code token usage by 90%

- Score: 257 | [HN](https://news.ycombinator.com/item?id=49571465) | Link: https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90

### TL;DR

Spotify’s article claims Portal reduced Claude Code token usage by 90% by delegating file reading and patterned writing to declarative “modes” running cheaper models, reserving the frontier model for harder reasoning. The shown bulk-reader mode uses Gemini 2.5 Flash in an ephemeral runtime with configured instructions and tools. The packet does not provide a measured correctness rate, task-success comparison, or total-cost calculation. Commenters questioned whether input-token savings survive output prices, errors, verification, and retries, while some compared the pattern to scouting subagents already used elsewhere.

### Comment pulse

- Skeptics said routing by task size ignores complexity and could replace visible token cost with subtle correctness failures.
- Supporters viewed cheaper scouts as useful filters when expensive agents over-read—counterpoint: the parent must still verify their findings.
- Many criticized the page’s writing and custom scrolling, distracting from its technical proposal.

### LLM perspective

- View: Token reduction is an incomplete optimization target without task success, correction effort, latency, and monetary cost.
- Impact: Teams can lower frontier-model context load, but delegation introduces another model boundary where errors may hide.
- Watch next: Publish controlled comparisons covering accuracy, retries, output tokens, human review, latency, and cost per accepted task.
