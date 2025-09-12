# Adaptive LLM routing under budget constraints

- Score: 206 | [HN](https://news.ycombinator.com/item?id=45094421) | Link: https://arxiv.org/abs/2508.21141

- TL;DR
  - The paper frames LLM routing as a contextual bandit: PILOT (a LinUCB variant) learns a shared query–model embedding from human preferences, adapts online via bandit feedback, and adds a knapsack-based budget policy to pick models under cost constraints. Aim: near-frontier quality at lower spend. HN debates whether routing’s economics hold in practice and how to measure “performance” (user satisfaction, tokens-per-interaction) versus benchmarks, whether LLMs can self-label task complexity (justifying human priors), and if enterprises actually care about LLM API costs yet.

- Comment pulse
  - Routing economics → Large price gaps (e.g., 100x) make savings robust even with errors; evaluate via satisfaction and TPI×PPT, not raw benchmarks.
  - Human preference data is needed → LLMs misjudge task complexity; 'pattern matchers' can't infer intent; feedback prevents routing blind spots.
  - Enterprise cost sensitivity is low → LLM spend often <10% of cloud; STT/image dominate; teams favor velocity — counterpoint: aggregators/resellers may optimize aggressively.

- LLM perspective
  - View: Bandit routing cuts evaluation cost by avoiding full cross-model inference; preference-initialized embeddings mitigate cold start.
  - Impact: Beneficial for API gateways, cost-capped apps, and hybrid on-device/cloud stacks.
  - Watch next: Standardized cost–quality–latency leaderboards; ablation vs supervised routers; safety/guardrail-aware routing policies.
