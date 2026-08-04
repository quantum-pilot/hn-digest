# Sakana Fugu

- Score: 212 | [HN](https://news.ycombinator.com/item?id=48624782) | Link: https://sakana.ai/fugu/

### TL;DR

Sakana Fugu exposes a learned multi-model orchestrator through one OpenAI-compatible API. Drawing on TRINITY and Conductor research, it dynamically selects agents, assigns Thinker, Worker, and Verifier roles, and coordinates multi-turn work rather than using fixed workflows. Fugu favors latency and allows provider opt-outs; Fugu Ultra uses a fixed, deeper pool for quality. Sakana reports frontier-level benchmark results and charges Ultra $5 input and $30 output per million tokens. HN reactions were polarized: supporters praised independent orchestration research, while users questioned speed, quotas, pricing, and real-world quality.

### Comment pulse

- Hands-on value lagged benchmarks → one developer reported under three weekly hours, slow responses, and weak workhorse quality; another paid roughly $60 for mixed research.

- Orchestration may have a short moat → frontier labs can add meta-reasoning harnesses or converge in capability, reducing benefits from model routing.

- Sakana’s approach deserves credit → supporters cited distinctive evolutionary research and strong published scores — counterpoint: product execution remains separate from research pedigree.

### LLM perspective

- **View:** Fugu productizes ensemble diversity, but opaque routing makes attribution, debugging, compliance verification, and reproducibility harder for customers.

- **Impact:** Teams gain vendor diversification behind one endpoint, trading direct model control for potentially higher quality and operational simplicity.

- **Watch next:** Measure task-level latency, total token consumption, independent benchmark replication, provider-failure behavior, routing transparency, and quality after model-pool updates.
