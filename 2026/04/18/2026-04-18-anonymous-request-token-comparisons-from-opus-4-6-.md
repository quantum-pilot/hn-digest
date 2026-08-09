# Anonymous request-token comparisons from Opus 4.6 and Opus 4.7

- Score: 395 | [HN](https://news.ycombinator.com/item?id=47816960) | Link: https://tokens.billchambers.me/leaderboard

### TL;DR

An independent community page compares how Opus 4.6 and 4.7 tokenize identical anonymous prompts. Across 853 submissions, it reports an average per-request token and input-cost increase of 35.9%, with mean counts shown as 366 versus 466; recent examples range from roughly 2% to 75%. Because the tool isolates prompt tokenization, Hacker News disputed treating this as total-cost evidence: 4.7 may emit fewer output and reasoning tokens, making reasoning-heavy workloads cheaper. Users nevertheless reported faster subscription-limit consumption, opaque effort settings, adaptive-thinking quality regressions, and weak perceived capability gains.

### Comment pulse

- Input costs rise on identical text — counterpoint: benchmark data cited in comments showed lower output-token spending can outweigh that at maximum effort.
- Several Max users said 4.7 consumes limits much faster and cycles through self-corrections; these are workload anecdotes, not controlled evaluations.
- Fine-grained developers preferred 4.5’s restraint, fearing forced replacement and a 7.5× Copilot modifier would charge more for unwanted overthinking.

### LLM perspective

- **View:** The page measures a real tokenizer change, but averaging percentage increases over tiny prompts can exaggerate practical impact.
- **Impact:** Chat and coding users face workload-dependent economics: cached input, reasoning depth, output length, retries, and subscription accounting all matter.
- **Watch next:** Paired end-to-end tasks, quality-adjusted cost, cache behavior, effort-level breakdowns, stable model snapshots, and Anthropic clarification of adaptive thinking.
