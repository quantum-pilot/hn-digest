# GPT-5.5 Price Increase: What It Costs

- Score: 193 | [HN](https://news.ycombinator.com/item?id=48057209) | Link: https://openrouter.ai/announcements/gpt55-cost-analysis

### TL;DR

GPT-5.5 doubled list prices versus 5.4 to $5 per million input tokens and $30 per million output tokens. OpenRouter’s before-and-after switcher cohort found actual normalized costs rose 49–92%, partly offset because prompts above 10,000 tokens yielded 19–34% shorter completions; shorter prompts saw no savings and sometimes longer answers. HN argued request-level token economics miss the decisive metric: total cost to complete a verified task, including turns. Reports varied by workload—some found 5.5 substantially stronger, while lower reasoning tiers often lost on cost-performance.

### Comment pulse

- Task-level benchmarks place 5.5 around 1.5–2× costlier → only xhigh reasoning reached a favorable frontier for one spec-driven TypeScript workflow.
- Stronger models may need fewer follow-ups → OpenRouter cannot group requests into goals, making per-request normalization incomplete.
- Users disagreed on qualitative progress → coding harnesses benefited, while some noncoding systems saw more failures and costly prompt rewrites.

### LLM perspective

- **View:** Token prices describe billing mechanics; verified outcome cost describes economic value.
- **Impact:** Teams need domain-specific evaluations before migrating defaults, especially at lower reasoning levels.
- **Watch next:** Transparent sample counts, task grouping, turn distributions, retry costs, and reasoning-setting comparisons.
