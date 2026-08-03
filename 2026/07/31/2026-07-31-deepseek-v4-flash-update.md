# DeepSeek-V4-Flash Update

- Score: 666 | [HN](https://news.ycombinator.com/item?id=49119559) | Link: https://api-docs.deepseek.com/updates/

### TL;DR

DeepSeek’s Flash API entered public beta with unchanged calling mechanics: select deepseek-v4-flash. The model retains the preview’s architecture and size but received additional post-training; reported agent scores include 82.7 on Terminal Bench 2.1, 70.3 on Toolathlon Verified, and 54.4 on DeepSWE. It now supports the Responses API and is adapted for Codex; Pro and app/web models remain unchanged. Commenters praise its speed, low cost, and broadly sufficient coding quality, while flagging output limits and uncertainty over whether benchmarks transfer to actual use.

### Comment pulse

- Fast, inexpensive inference changes model selection → users route most coding through Flash, reserving frontier models for planning, review, and difficult cases.
- Economics enable scale → one user reported 323 million tokens and 3,467 requests for $4.55 over 30 days.
- Benchmark enthusiasm is broad → published scores look exceptional — counterpoint: one commenter cited Flash at 54.4 versus Luna at 67 on DeepSWE.

### LLM perspective

- View: Re-post-training can materially improve agent performance without increasing model size.
- Impact: Tool and harness builders may favor fast, economical agents over maximum single-pass capability.
- Watch next: Test the forthcoming DeepSeek Harness and Pro release against Flash under matched budgets and output limits.
