# Tongyi DeepResearch – open-source 30B MoE Model that rivals OpenAI DeepResearch

- Score: 230 | [HN](https://news.ycombinator.com/item?id=45789602) | Link: https://tongyi-agent.github.io/blog/introducing-tongyi-deep-research/

- TL;DR
    - Alibaba’s Tongyi DeepResearch is an open-source 30B MoE web agent claiming parity with OpenAI’s DeepResearch on HLE (32.9), BrowseComp (43.4/46.7 ZH), and xbench‑DeepSearch (75). It trains end‑to‑end on fully synthetic data: agentic continual pre‑training, SFT, and on‑policy GRPO RL in an offline Wikipedia sandbox—then runs ReAct or a test‑time‑scaled Heavy Mode (IterResearch). Real deployments include Amap trip planning and a legal research copilot. HN debates specialization vs frontier models, the real utility of “deep research,” and notes a surprisingly capable 4B distill.

- Comment pulse
    - Frontier beats niche → Big models still outpace most fine-tunes; MoE helps specialization, but keeping up is costly — counterpoint: domain models defend moats and margins.
    - Deep-research utility varies → Many find reports bland, yet value automated source discovery, market overviews, and background runs.
    - Small distills look promising → A 4B Qwen3 distillation impressed users with web search MCP, hinting at strong task transfer at tiny cost.

- LLM perspective
    - View: Open performance parity plus Heavy Mode suggests test-time compute and structured context control are now key levers for agent quality.
    - Impact: Lower-cost, credible web agents make enterprise pilots practical; expect rapid distillations to 4–8B and domain MoE experts.
    - Watch next: Live-web robustness, dataset openness/licensing, reproducible GRPO details, and whether frontier models absorb these gains quickly.
