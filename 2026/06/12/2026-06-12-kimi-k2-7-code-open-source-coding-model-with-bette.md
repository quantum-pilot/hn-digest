# Kimi K2.7-Code: open-source coding model with better token efficiency

- Score: 453 | [HN](https://news.ycombinator.com/item?id=48502347) | Link: https://huggingface.co/moonshotai/Kimi-K2.7-Code

## TL;DR
Kimi K2.7-Code is an open Mixture-of-Experts coding model (1T parameters, 32B active) with 256K context, integrated “thinking mode,” and native INT4 quantization. It targets long-horizon, tool-using software-engineering workflows while cutting reasoning-token usage ~30% versus K2.6. Benchmarks show sizable gains over K2.6 but still behind GPT‑5.5 and Claude Opus on coding and agent tasks. Released under a Modified MIT license requiring UI attribution, it’s seen as a strong, cheaper “Claude Code–style” option, especially when paired with tools like opencode.

---

## Comment pulse
- License = MIT plus attribution clause → basically old BSD “advertising” requirement; some dislike the vague “user interface” wording.
- Many devs: once design is clear, frontier vs ~30B models feel similar for function-level coding; planning quality matters more than raw scores.
- Practitioners: Claude Code still best overall, but Kimi 2.6/2.7 via opencode is “workable” and often cheaper; one user rebased a large OpenSSL patch successfully.

---

## LLM perspective
- View: Treat Kimi K2.7-Code as a serious, open alternative for agentic coding, especially if you already drive models via your own framework.
- Impact: Lowers cost of high-quality long-context coding agents; pressures US vendors on pricing, planning quality, and explicit reasoning APIs.
- Watch next: Independent evals vs frontier models, clearer license FAQs, and tighter integrations into IDE agents and router setups.
