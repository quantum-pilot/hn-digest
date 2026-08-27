# Kimi K2 Thinking, a SOTA open-source trillion-parameter reasoning model

- Score: 533 | [HN](https://news.ycombinator.com/item?id=45836070) | Link: https://moonshotai.github.io/Kimi-K2/thinking.html

### TL;DR

Moonshot introduced Kimi K2 Thinking, a trillion-parameter reasoning model built for long tool-using workflows and native INT4 inference. The company reports 44.9% on HLE with tools, 60.2% on BrowseComp, 71.3% on SWE-bench Verified, and coherent runs of 200–300 tool calls; its consumer chat mode uses fewer tools and may not reproduce those results. Evaluations use large step and token budgets, custom harnesses, and some retested baselines. Commenters welcomed competition but disputed “open source,” local practicality, benchmark representativeness, and economics.

### Comment pulse

- Commenters noted that mixture-of-experts activation may reduce per-token compute, yet the full trillion-parameter footprint still complicates local deployment.
- Several wanted independent tests under matched budgets rather than comparisons assembled from differing harnesses and providers.

### LLM perspective

- View: The headline performance claim is inseparable from its agent scaffold, generous budgets, and evaluation methodology.
- Impact: Hosted providers and researchers benefit first; local users face substantial memory and infrastructure constraints.
- Watch next: Independent replication, licensing clarity, real task costs, latency, and release of the fuller agentic mode.
