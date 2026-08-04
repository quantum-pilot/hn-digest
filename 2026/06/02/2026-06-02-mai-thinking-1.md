# MAI-Thinking-1

- Score: 167 | [HN](https://news.ycombinator.com/item?id=48374362) | Link: https://microsoft.ai/news/introducing-mai-thinking-1/

### TL;DR

Microsoft’s new reasoning model is a sparse mixture-of-experts system with 35 billion active and roughly 1 trillion total parameters. Microsoft says it was trained from scratch on licensed, non-synthetic pretraining data without third-party distillation, scores 94.5% on AIME 2026, matches Claude Opus 4.6 on SWE-Bench Pro, and was preferred to Sonnet 4.6 in a 1,276-task blind study. It is in private Foundry preview. HN welcomed another independent model lineage but questioned licensing details, benchmark efficiency, comparison choices, and whether clean-data self-sufficiency outweighs weaker results versus smaller distilled competitors.

### Comment pulse

- Provenance → Readers wanted a concrete definition of appropriately licensed, especially for GitHub code, and contrasted the stance with Microsoft’s synthetic-data-heavy Phi work.
- Efficiency → Commenters ranked it near DeepSeek V3.2 and below smaller GLM-5.1 and Kimi K2.6 — counterpoint: those competitors allegedly rely on distillation.
- Context → Some called 256k short beside advertised million-token windows; practitioners replied that quality often degrades above 100–150k, limiting nominal capacity’s value.

### LLM perspective

- **View:** Rejecting distillation creates a slower but strategically independent learning loop; its value depends on sustained improvement, not launch-day rank.
- **Impact:** Enterprises prioritizing provenance gain an alternative; Microsoft reduces model-supplier dependence while absorbing the full cost of frontier training.
- **Watch next:** Public-preview pricing, latency, tool-use reliability, long-context retention, licensing documentation, independent SWE-Bench replication, refusal rates, and hill-climbing updates.
