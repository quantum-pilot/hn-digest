# Two things LLM coding agents are still bad at

- Score: 305 | [HN](https://news.ycombinator.com/item?id=45523537) | Link: https://kix.dev/two-things-llm-coding-agents-are-still-bad-at/

### TL;DR

The author identifies two recurring coding-agent failures: agents regenerate moved code instead of performing exact copy-and-paste operations, and they make assumptions rather than asking clarifying questions. Regeneration can silently alter comments, links, or logic during nominal refactors; brute-force action can compound a mistaken premise. Commenters supplied examples of hallucinated URLs, unrelated edits, incomplete architectural replacements, and missed repository conventions. They argued that review practices must adapt because apparently mechanical moves may now contain semantic changes invisible at a glance.

### Comment pulse

- Readers advocated disclosing AI use in pull requests so reviewers can target unfamiliar failure modes.
- Others emphasized curated context, tests, constrained tools, and explicit repository instructions over unsupervised autonomy.

### LLM perspective

- View: Treating generative edits as mechanical transformations is the core category error behind these failures.
- Impact: Review cost rises because unchanged-looking regions can no longer be presumed textually preserved.
- Watch next: Agents need deterministic move tools, provenance-aware diffs, and reliable escalation when assumptions matter.
