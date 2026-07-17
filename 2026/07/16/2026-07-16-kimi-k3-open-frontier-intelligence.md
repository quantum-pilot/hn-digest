# Kimi K3: Open Frontier Intelligence

- Score: 1057 | [HN](https://news.ycombinator.com/item?id=48935342) | Link: https://www.kimi.com/blog/kimi-k3

### TL;DR
Kimi K3 is a 2.8T-parameter, open-weights MoE model with native vision and a 1M-token context window, targeted at long-horizon coding, “agentic” knowledge work, and multimodal reasoning. Architecturally it introduces Kimi Delta Attention, Attention Residuals, and a 16-of-896 Stable LatentMoE setup plus quantization-aware training, claiming ~2.5× better scaling efficiency than K2. Benchmarks put it just behind Claude Fable 5 and GPT‑5.6 Sol but ahead of other frontier models, prompting excitement, skepticism about benchmark inflation, and concerns about data usage and Chinese AI strategy.

---

### Comment pulse
- Providers train on API traffic → Moonshot’s terms allow using customer content for model improvement; serious secrecy needs enterprise deals or self-hosted models.  
- Benchmarks look stellar → commenters suspect overfitting/benchmark leakage and marketing spin (“second only to two others”)—counterpoint: still impressive that open weights approach frontier labs.  
- Chinese labs “commoditizing intelligence” → cheap/open models may undercut US AI moats; others argue it’s just rational GTM and reputation-building, not a unified state plot.

---

### LLM perspective
- View: Open near-frontier models with huge context push serious work—codebases, research, video—into commodity tooling.  
- Impact: Strong incentive for enterprises to reassess “closed-only” stacks; infra vendors and open-source inference stacks gain leverage.  
- Watch next: Independent evals on real workflows, robustness/safety audits, and how usable full 2.8T weights are outside hyperscale clusters.
