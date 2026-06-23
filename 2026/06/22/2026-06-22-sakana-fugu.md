# Sakana Fugu

- Score: 212 | [HN](https://news.ycombinator.com/item?id=48624782) | Link: https://sakana.ai/fugu/

## TL;DR

Sakana Fugu is a “multi-agent system as a model”: instead of one LLM, it’s a learned coordinator that routes work among many expert models. Built on the TRINITY and Conductor research, it uses roles, natural‑language coordination, and reinforcement learning to discover efficient collaboration patterns. Offered as Fugu (latency/quality balanced) and Fugu Ultra (max quality), it runs behind an OpenAI‑compatible API, claims frontier‑level results on coding/reasoning benchmarks and bespoke tasks, and provides flexible pricing plus limited control over which underlying agents are used.

---

## LLM perspective

- View: A generic orchestration layer over third‑party LLMs commoditizes base models and shifts value to coordination, evaluation, and tooling.

- Impact: Engineering teams can swap vendors and gain multi-model performance via one endpoint, but lose transparency into per-query routing decisions.

- Watch next: Independent, reproducible benchmarks of Fugu vs top single models, plus real-world latency/reliability data under production workloads.
