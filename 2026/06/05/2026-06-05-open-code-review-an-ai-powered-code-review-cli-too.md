# Open Code Review – An AI-powered code review CLI tool

- Score: 258 | [HN](https://news.ycombinator.com/item?id=48406358) | Link: https://github.com/alibaba/open-code-review

### TL;DR

Alibaba open-sourced a CLI that reviews workspaces, commits, or branch diffs through a configurable LLM, returning line-level findings or CI-ready JSON. Its hybrid design uses deterministic file selection, related-file bundles, rule matching, positioning, and reflection to constrain an agent that retrieves broader code context. Alibaba says its internal predecessor served tens of thousands of developers and found millions of defects. HN valued repeatable enforcement and reviewer-model diversity, but early benchmark results suggested severe false-positive noise; commenters also warned about token cost and review theater without independent human judgment.

### Comment pulse

- Coverage was promising but noisy → a 10-PR sample found 74% recall yet 12% precision, making human triage the dominant cost.
- A separate reviewer may expose different blind spots → another model plus CI enforcement avoids correlated self-review and forgotten local checks.
- Automation can become review theater → PR comments preserve rationale — counterpoint: merely relaying agent output provides no independent judgment.

### LLM perspective

- **View:** Deterministic orchestration is the product; the underlying model remains interchangeable and still determines much of review quality.
- **Impact:** Teams gain enforceable pre-merge coverage but may exchange escaped bugs for triage load and API spend.
- **Watch next:** Run the full 50-PR benchmark by model; report precision, recall, cost, latency, and developer acceptance.
