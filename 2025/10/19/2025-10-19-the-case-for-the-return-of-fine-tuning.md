# The case for the return of fine-tuning

- Score: 135 | [HN](https://news.ycombinator.com/item?id=45633081) | Link: https://welovesota.com/article/the-case-for-the-return-of-fine-tuning

- TL;DR
  - Fine-tuning is resurging as models stabilize, open-weight options expand, and GPU services make LoRA cheap and fast. The piece spotlights Tinker’s research platform, actionable LoRA heuristics (apply to all linear layers, higher learning rates, small batches), and modular inference that routes to multiple adapters—while warning evaluation is still the blocker, pushing toward online RL and continuous learning. HN frames fine-tuning as a lever for control and cost/latency wins, but flags labeling shortages, skills gaps, SOTA churn, and uneven ROI.

- Comment pulse
  - Skepticism on ROI/supportability → RL tuning is nuanced; labels are scarce; platform tools hide metrics; SOTA evolves faster than enterprise delivery.
  - Concrete wins → Datadog latency cuts; Vercel custom generators; Shopify vision; small specialized models beat larger at lower cost — counterpoint: prompts often suffice.
  - Founder reality check → Lamini: fine-tuning is no easier than deep learning; elite labs outcompete; RAG/agents/memory/SLMs cover most needs; fine-tune for precision or ultra‑high‑volume.

- LLM perspective
  - View: Fine-tuning returns as a control layer: adapters, low-level APIs, and online RL enable specialization and continuous improvement.
  - Impact: Open-weight models and on-prem GPUs shift spend from API calls to owned, task-specific inference.
  - Watch next: Standardized eval suites, adapter routing benchmarks, and Tinker-like offerings for enterprises, not academia-only.
