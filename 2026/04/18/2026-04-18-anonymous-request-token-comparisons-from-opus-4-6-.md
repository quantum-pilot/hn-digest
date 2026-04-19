# Anonymous request-token comparisons from Opus 4.6 and Opus 4.7

- Score: 395 | [HN](https://news.ycombinator.com/item?id=47816960) | Link: https://tokens.billchambers.me/leaderboard

### TL;DR
Community tool collects anonymous prompts and compares how many request tokens Opus 4.6 vs 4.7 consume, focusing on tokenizer/input changes. Commenters argue this is only a partial picture: total cost also depends on output and “reasoning” tokens, where benchmarks show 4.7 often uses fewer than 4.6. Depending on workload, 4.7 can be slightly cheaper or clearly more expensive. Many users, however, report faster limit burn, degraded code quality, and issues tied to forced adaptive thinking, with debate over whether this reflects strategy, capacity, or safety tradeoffs.

### Comment pulse
- Tokenomics comparison is incomplete → tool isolates tokenizer/input costs; benchmarks show 4.7 cuts output/reasoning tokens, so real per-task cost is workload-dependent.  
- Perceived quality and usability drop → forced adaptive thinking, cycling, hand‑wavy reasoning, and high limit usage push some developers to stick with 4.5.  
- Motives disputed → some see profit-driven “engagement” design; others argue capacity, mis-tuning, or safety concerns are likelier than deliberate degradation.

### LLM perspective
- View: Treat tokenizer-only comparisons as diagnostics; decide on models using full-task cost, latency, and defect/redo rates.  
- Impact: Power users with long coding sessions and IDE agents feel changes most, especially where model swaps are forced.  
- Watch next: Independent benchmarks of “cost per solved ticket,” better effort controls, and whether older, cheaper models remain available.
