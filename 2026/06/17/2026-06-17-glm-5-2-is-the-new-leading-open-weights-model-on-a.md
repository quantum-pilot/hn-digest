# GLM-5.2 is the new leading open weights model on Artificial Analysis

- Score: 760 | [HN](https://news.ycombinator.com/item?id=48567759) | Link: https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index

### TL;DR

Z.ai’s MIT-licensed GLM-5.2 has 744B total parameters, 40B active, and a 1-million-token context. It scores 51 on Artificial Analysis’s Intelligence Index—11 points above GLM-5.1 and seven above its nearest open-weight peers. It also reaches 1524 on GDPval-AA v2, roughly level with GPT-5.5 xhigh, at about $0.46 per indexed task. The tradeoff is 43,000 output tokens per task, including 37,000 reasoning tokens. HN praised frontier-adjacent quality and low API prices but disputed coding benchmarks, provider fidelity, usability, and real-world efficiency.

### Comment pulse

- Maximum effort can stall delivery → one Nim task consumed 45,000 reasoning tokens before creating a file; lower effort reportedly cuts usage 2–2.5×.
- Leaderboard rank is harness-sensitive → Artificial Analysis’s coding score uses two benchmarks, and commenters observed major model shifts between Cursor and Codex.
- Cheap hosting may conceal quality loss → third parties can quantize or misconfigure models — counterpoint: open weights enable private, interchangeable providers at subscription prices.

### LLM perspective

- **View:** GLM-5.2 closes capability gaps faster than latency gaps; lower token prices do not eliminate waiting time or orchestration overhead.
- **Impact:** Teams gain a permissively licensed frontier alternative, but text-only input requires separate vision models for screenshot-driven workflows.
- **Watch next:** Compare High versus Max on task success, latency, token use, variance, and coding suites with identical harnesses.
