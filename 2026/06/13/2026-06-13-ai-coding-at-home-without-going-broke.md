# AI coding at home without going broke

- Score: 344 | [HN](https://news.ycombinator.com/item?id=48518969) | Link: https://stephen.bochinski.dev/blog/2026/06/13/ai-coding-at-home-without-going-broke/

## TL;DR
The article compares three ways to do “AI coding at home”: (1) buying your own GPU and self‑hosting open models, (2) renting those models via API, and (3) using discounted “frontier” subscriptions (OpenAI/Anthropic). Self‑hosting only makes sense if you constantly run long, batchy workloads and accept rapid hardware churn; most people are better off with APIs. The author recommends a hybrid: frontier models for design/spec work, cheaper open models for mechanical coding, keeping total monthly spend near ~$1k for heavy solo output.

---

## Comment pulse
- Many devs never hit plan limits → structured, human‑driven workflows keep usage modest; huge bills often come from unattended agents and “vibe coding” — counterpoint: well‑tuned agents can 2×+ productivity.
- Self‑hosting economics weak → power and capex mean you mainly pay for privacy/control; some note GPU resale value, solar, and long card lifetimes soften costs.
- Local/cheap options workable → Gemma/Qwen on consumer machines, DeepSeek via API, and free tiers let people code heavily without big rigs or enterprise‑scale budgets.

---

## LLM perspective
- View: The real lever is workflow design—spec‑first, human‑in‑the‑loop cycles, and clear boundaries on when agents run autonomously.
- Impact: Solo devs and small teams can approximate “extra engineers” if they actively manage scope, context size, and agent permissions.
- Watch next: Better per‑project cost dashboards, standardized agent benchmarks, and more efficient open models will keep shifting the self‑host vs. API vs. subscription balance.
