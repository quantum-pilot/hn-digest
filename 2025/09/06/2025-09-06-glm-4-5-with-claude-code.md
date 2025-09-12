# GLM 4.5 with Claude Code

- Score: 210 | [HN](https://news.ycombinator.com/item?id=45145457) | Link: https://docs.z.ai/guides/llm/glm-4.5

- TL;DR
  - Z.AI’s GLM‑4.5 (355B MoE; 32B active) and 4.5‑Air (106B/12B) target agentic coding: 15T‑token pretrain, RL tuning, 128k context, tool/browse support, and switchable “thinking” mode. They publish a 52‑task Claude Code benchmark showing near‑Sonnet performance, with ultra‑low pricing ($0.20/M in, $1.10/M out) and >100 tok/s variants. HN debates real-world value: OpenRouter provider quality and quantization, bargain positioning versus Sonnet/Opus, hardware needs for local speed, and broad data‑use rights in Z.ai’s privacy policy.

- Comment pulse
  - Claude Code integration is easy → point ANTHROPIC_BASE_URL to Z.ai or use routers; Claude‑tuned prompts hinder others — counterpoint: GLM claims CC‑tuned performance.
  - OpenRouter outputs vary → provider quantization (FP8/FP4) and batching affect quality; denylist bad providers or request precision; local smaller models sometimes beat hosted.
  - Privacy is a concern → Z.ai policy grants broad, perpetual rights over prompts/code; free or cheap tiers trade privacy for cost.

- LLM perspective
  - View: A credible low-cost coding agent contender; open trajectories and CC-bench increase trust and make third-party replication feasible.
  - Impact: Downward pressure on code-assistant pricing; more experimentation with model routing and denylisting in developer workflows.
  - Watch next: Third-party audits of quantization effects, reproducible CC-bench reruns, and client-side privacy controls or self-hosted SKUs.
