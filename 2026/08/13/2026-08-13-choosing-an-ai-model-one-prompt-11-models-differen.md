# Choosing an AI model: one prompt, 11 models, different results

- Score: 175 | [HN](https://news.ycombinator.com/item?id=49285327) | Link: https://www.netlify.com/blog/one-prompt-11-models-very-different-results/

### TL;DR

Netlify ran one sparse coffee-shop-site prompt three times across 11 models, comparing design, copy, and Agent Runner credit use rather than production-grade coding. Average cost ranged from 2.4 credits for DeepSeek V4 Flash to 519 for Claude Opus 5; Opus produced richer work but one run consumed 1,055 credits, while GPT-5.6 Terra delivered worthwhile variety around 39 credits with occasional glitches. Netlify frames the choice as turnkey ideation versus cheaper guided iteration. Commenters found the unconstrained task narrow, clichéd, and highly sensitive to run variance.

### Comment pulse

- Critics said generic prompts reward median visual tropes and reveal little about constrained, serious development or correctness.
- Others found model “taste” useful for solo ideation—counterpoint: three runs expose variance but remain thin evidence for broad rankings.

### LLM perspective

- View: Model choice is a task-and-harness decision; price, autonomy, visual taste, and correctness occupy different frontiers.
- Impact: Teams can reserve expensive models for exploration or judging, then route constrained implementation to cheaper candidates.
- Watch next: Netlify’s database, upload, AI-gateway, security, and self-validation tests should reveal whether visual rankings survive functional work.
