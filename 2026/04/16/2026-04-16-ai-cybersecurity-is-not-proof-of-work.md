# AI cybersecurity is not proof of work

- Score: 193 | [HN](https://news.ycombinator.com/item?id=47791236) | Link: https://antirez.com/news/163

### TL;DR

The author rejects proof-of-work as a model for AI vulnerability research. Hash search guarantees progress with more computation; bug discovery eventually saturates meaningful paths and becomes capped by model intelligence. The OpenBSD SACK flaw required combining validation, overflow, and impossible-state reasoning that weaker models could mention separately without understanding or exploiting. Hacker News challenged the claim because restricted Mythos prevents comparison and “better” could mean training, context, scaffold, prompt, or budget. Commenters said breadth, capability, and expert humans all matter; defenders must also patch widely, while attackers need one exploit.

### Comment pulse

- Restricted Mythos makes replication impossible; observers cannot separate model scale from security training, context, prompting, or agent scaffolding.
- More tokens expand search breadth — counterpoint: no amount of sampling guarantees a model will synthesize a vulnerability beyond its reasoning threshold.
- On-demand token spending industrializes expert labor, but unequal budgets may leave small maintainers and low-margin IoT fleets chronically exposed.

### LLM perspective

- **View:** Security search has both compute and capability frontiers; calling either sufficient obscures the empirical curve between them.
- **Impact:** Frontier-model access becomes strategic infrastructure, while patch economics and deployment speed may dominate discovery gains.
- **Watch next:** Reproducible model comparisons, token-capability scaling curves, exploit validation rates, defender lead time, patch adoption, and construction-based vulnerability elimination.
