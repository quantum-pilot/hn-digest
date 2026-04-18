# Measuring Claude 4.7's tokenizer costs

- Score: 518 | [HN](https://news.ycombinator.com/item?id=47807006) | Link: https://www.claudecodecamp.com/p/i-measured-claude-4-7-s-new-tokenizer-here-s-what-it-costs-you

### TL;DR

The author measures Anthropic’s new Claude Opus 4.7 tokenizer and finds English/code text produces about 1.3–1.45× more tokens than 4.6, while CJK is nearly unchanged. On a small IFEval sample, 4.7 shows a modest +5 percentage-point gain in strict instruction following. For a long, cached Claude Code session, this translates into roughly 20–30% higher session cost or faster exhaustion of Max-plan limits. HN discussion debates whether this matters versus human labor costs and real per-task efficiency.

---

### Comment pulse

- Performance–cost frontier is likely logarithmic → recent Opus gains may be on a curve of steeply diminishing returns; firms must right-size models and thinking levels.

- Many report Claude yields multi‑month productivity gains for small teams → token costs are trivial versus developer salaries; price could rise substantially and still be worth it.

- Tokenizer-only analysis is incomplete → 4.7 might need fewer reasoning tokens per task, sometimes making it cheaper overall—counterpoint: others’ benchmarks sometimes find 4.7 consistently more expensive.

---

### LLM perspective

- View: Treat tokenizer changes as part of a broader “effective cost per solved task” shift, not just a raw token-multiplier story.

- Impact: Teams running long, tool-heavy coding sessions should re-benchmark workflows and possibly dial down effort/model size where quality plateaus.

- Watch next: Independent cross-model cost-per-task benchmarks, smarter routing between “cheap” and “premium” models, and better tooling to monitor cache hits and effective spend.
