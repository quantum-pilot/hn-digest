# Kimi K2.5 Technical Report [pdf]

- Score: 185 | [HN](https://news.ycombinator.com/item?id=46826597) | Link: https://github.com/MoonshotAI/Kimi-K2.5/blob/master/tech_report.pdf

### TL;DR

Moonshot AI presents Kimi K2.5 as an open-source, native multimodal agent model built on a 1.04-trillion-parameter mixture-of-experts backbone with 32 billion active parameters and roughly 15 trillion mixed text-vision training tokens. Early low-ratio vision fusion, text-only supervised tuning, and joint reinforcement learning reportedly strengthen both modalities. Its Agent Swarm trains an orchestrator to create frozen specialist subagents, raising BrowseComp from 60.6% to 78.4% and cutting WideSearch latency three- to 4.5-fold. Commenters praised coding quality but questioned hardware demands, harness support, and token cost.

### Comment pulse

- Early users called coding performance competitive with proprietary leaders → replies immediately asked what hardware and serving setup made that possible.
- Tool calling widened potential use → commenters saw improved structured retrieval compared with earlier open models.
- Agent Swarm generated excitement — counterpoint: users were unsure which harnesses expose it and whether its token consumption justifies the gain.

### LLM perspective

- View: The strongest contribution is learned parallel orchestration; benchmark claims remain author-reported and include some internal reevaluations.
- Impact: Open checkpoints give researchers a frontier-scale multimodal agent, but practical self-hosting remains hardware-intensive.
- Watch next: Independent benchmark replication, quantized deployments, swarm cost accounting, harness interoperability, and real-world reliability under concurrent tool use.
