# SWE-1.7 Reach Near GPT 5.5 and Opus Intelligence

- Score: 244 | [HN](https://news.ycombinator.com/item?id=48833866) | Link: https://cognition.com/blog/swe-1-7

### TL;DR

Cognition’s SWE-1.7, post-trained from Kimi K2.7, scores 42.3% on its FrontierCode benchmark, near GPT-5.5’s 43.0% and below Opus 4.8’s 46.5%, while claiming much lower rollout cost. The coding agent runs inside Devin at 1,000 tokens per second via Cerebras. Its RL advances include top-p replay to preserve entropy, cross-continent rollout clusters, hardened verifiers, and learned self-compaction for six-hour tasks. HN admired the engineering but doubted benchmark generality, citing vendor-specific eval overlap, omitted competitors, conflicting independent rankings, and Cognition’s support and pricing history.

### Comment pulse

- Vendor benchmarks may reward vendor workflows → Cognition and Cursor each rank their own Kimi-derived model highly, suggesting measurement alignment or train-eval overlap.
- Independent rankings tell a different story → Kimi trails GLM elsewhere, while prominent low-cost models were omitted from the published Pareto comparison.
- Coding specialization has limits → narrow post-training can harm generalization — counterpoint: lower-cost specialists remain valuable when routing preserves a generalist for cross-domain work.

### LLM perspective

- **View:** SWE-1.7’s contribution is as much scalable RL infrastructure as model quality: long runs, distributed rollouts, and learned state compression.
- **Impact:** Cheaper coding specialists reduce agent costs, but local optimization can increase scope creep and weaken performance beyond familiar workflows.
- **Watch next:** External evaluations, rollout cost, failure recovery, compaction fidelity, unrelated-file edits, broader-domain retention, customer support, and standalone model access.
