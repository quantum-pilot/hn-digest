# Claude Token Counter, now with model comparisons

- Score: 206 | [HN](https://news.ycombinator.com/item?id=47829178) | Link: https://simonwillison.net/2026/Apr/20/claude-token-counts/

### TL;DR

Simon Willison’s Claude Token Counter can now compare the same text, image, or PDF across model IDs. Opus 4.7 appears to be Claude’s first tokenizer change: Anthropic warned identical input may expand 1.0–1.35×, while its own system prompt measured 1.46× versus 4.6. Because per-token prices stayed at $5 input and $25 output per million, that implies higher effective cost. A large image counted 3.01× more only because 4.7 accepted higher resolution; small-image counts were nearly identical, and a text-heavy PDF rose 1.08×.

### Comment pulse

- Users said tokenizer differences make headline per-token prices misleading, especially across languages.
- Some hypothesized semantic or morphological benefits — counterpoint: commenters noted little evidence such tokenizers improve performance and no design details are published.
- Subscription users reported faster quota depletion and requested transparent technical explanations before interpreting inflation as a pricing maneuver.

### LLM perspective

- Compare task-level cost and quality, not nominal token rates, because tokenization changes both billing and context consumption.
- Content type matters: raw text, PDFs, and images showed materially different multipliers.
- Reverse-engineered tokenizer behavior or official benchmarks would clarify whether extra tokens buy measurable capability.
