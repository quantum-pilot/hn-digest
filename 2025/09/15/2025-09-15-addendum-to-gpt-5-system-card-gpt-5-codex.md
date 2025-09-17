# Addendum to GPT-5 system card: GPT-5-Codex

- Score: 219 | [HN](https://news.ycombinator.com/item?id=45253458) | Link: https://openai.com/index/gpt-5-system-card-addendum-gpt-5-codex/

- TL;DR
  - OpenAI’s GPT‑5‑Codex is a GPT‑5 variant tuned for agentic coding: RL on real-world tasks, humanlike code/PR style, strict instruction-following, and iterative test‑until‑pass loops. It ships via Codex CLI/IDE, web, GitHub, and ChatGPT mobile. The system‑card addendum focuses on safety: training against harmful tasks/prompt injection, plus sandboxed agents and configurable network access. HN reports strong gains over Claude Code and Gemini, better long‑context handling, but flags slowness, occasional “laziness” near context limits, uptime instability, lack of custom containers, and questions on pricing sustainability.

- Comment pulse
  - Performance leap vs peers → Many switch from Claude Code/Gemini to Codex; better long-context, fewer half-done tasks. — counterpoint: Degrades near max context; pauses for confirmation.
  - Ops and pricing concerns → Frequent downtime and missing custom containers frustrate teams; pricing may be unsustainably low; JetBrains quotas burn fast.
  - Speed vs quality tradeoff → Codex “thinks too long” yet reduces reprompting; some prefer Cursor for cost-effectiveness.

- LLM perspective
  - View: Agentic coding is becoming productized: RL-tuned models plus sandboxes bridge chat and autonomous workflows inside IDEs.
  - Impact: Vendors competing on reliability and integration, not just IQ; uptime, containers, and repo context will decide daily adoption.
  - Watch next: Independent benchmarks on end-to-end tasks, context-length robustness, and cost per passing PR; roadmap for custom environments and network policy granularity.
