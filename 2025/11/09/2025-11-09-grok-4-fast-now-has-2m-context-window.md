# Grok 4 Fast now has 2M context window

- Score: 167 | [HN](https://news.ycombinator.com/item?id=45862833) | Link: https://docs.x.ai/docs/models

### TL;DR

xAI's documentation lists reasoning and non-reasoning Grok 4 Fast variants with two-million-token context windows, four-million-token-per-minute limits, and prices of $0.20 per million input tokens and $0.50 per million output tokens. The models support function calling and structured outputs; current-event access requires tools or supplied context. Commenters agreed the capacity is concrete but disputed its practical value: large prompts help whole-codebase or extraction tasks, yet attention can weaken, instructions can be forgotten, and smaller relevant contexts often produce better results.

### Comment pulse

- Speed and low cost enable high-volume routine work, while harder tasks may still require more capable models.
- Readers requested long-context retrieval benchmarks because advertised capacity does not demonstrate effective use across two million tokens.

### LLM perspective

- View: Context size is storage capacity; useful recall and prioritization determine whether it becomes working memory.
- Impact: Developers can submit larger corpora but may pay for noise that degrades focus and reliability.
- Watch next: Needle-retrieval curves, positional bias, latency, cost at full context, and codebase-scale evaluations.
