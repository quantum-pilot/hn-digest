# Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model

- Score: 629 | [HN](https://news.ycombinator.com/item?id=47863217) | Link: https://qwen.ai/blog?id=qwen3.6-27b

### TL;DR
Qwen3.6-27B is a new 27B-parameter *dense*, open-weight, multimodal model that targets “flagship-level” coding. Despite its size, it beats Qwen’s own 397B MoE predecessor on every major coding benchmark (SWE-bench Verified/Pro, Terminal-Bench 2.0, SkillsBench), and is competitive on reasoning and vision tasks. It exposes OpenAI- and Anthropic-compatible APIs, supports “thinking” traces, and integrates with tools like OpenClaw and Claude Code. HN discussion focuses on local performance, hardware requirements, and how close it really is to Claude/Opus in day‑to‑day coding.

---

### Comment pulse

- Local use is viable → 16–20GB quantized variants run on high-end consumer Macs/GPUs with ~20–30 tok/s; Simon Willison’s “pelican” test output is unusually strong — counterpoint: may indicate training-set leakage/overfitting.

- Dense vs MoE tradeoff → 27B dense gives higher quality but is much slower than 35B-A3B MoE on Macs; expect ≥24GB VRAM for comfortable GPU serving.

- Open vs closed frontier → Open models narrow the gap and slash costs, but many still find Opus/Claude clearly superior for serious coding and trust US hosts more than Chinese cloud providers.

---

### LLM perspective

- View: 27B dense multimodal models look like the new practical “high-end local/enterprise” tier for coding agents.

- Impact: Lowers cost for strong in-house copilots; increases pressure on proprietary providers to differentiate on quality, reliability, and governance.

- Watch next: Independent end-to-end coding evals, quantization-quality curves on real workloads, and whether API providers react to “vampire attack” training by deliberate output poisoning.
