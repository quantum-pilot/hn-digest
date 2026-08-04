# Kimi K3 Is Competitive with Fable; Kimi K3 and Fable Is SoTA

- Score: 167 | [HN](https://news.ycombinator.com/item?id=48999291) | Link: https://fireworks.ai/blog/kimik3-fable

### TL;DR

Fireworks benchmarked Kimi K3 and Fable 5 on roughly 1,000 agentic coding, terminal, algorithmic, multilingual, and legal tasks. Overall quality was close—92.4% versus 92.6% on software work—but their strengths differed by domain. An oracle that ran both and retrospectively chose the cheapest correct answer reached 93% accuracy, selected K3 for 72–96% of tasks, and projected savings up to 50× on long loops. HN liked K3’s cost and openness but stressed that this is a theoretical ceiling, not a demonstrated predictive router.

### Comment pulse

- Oracle savings are not deployable routing → the study knows correctness after running both models; a live system must predict before paying.
- Cost depends on platform economics → prompt-cache hits, token pricing, and variable agent turns drove the gap; K3 could be cheaper yet slower.
- Open-model enthusiasm extended beyond price → users valued fewer safety refusals and self-hostable gateways — counterpoint: the release may provide weights without full training openness.

### LLM perspective

- **View:** Model complementarity is real; the unproven asset is forecasting which specialist will solve each unseen task most economically.
- **Impact:** Teams could reserve premium models for rare tasks, but routing errors may erase savings or silently reduce quality.
- **Watch next:** Evaluate trained routers prospectively on private workloads, including overhead, latency, abstentions, drift, and end-to-end cost per correct result.
