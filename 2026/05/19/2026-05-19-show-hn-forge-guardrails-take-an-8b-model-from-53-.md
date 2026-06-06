# Show HN: Forge – Guardrails take an 8B model from 53% to 99% on agentic tasks

- Score: 275 | [HN](https://news.ycombinator.com/item?id=48192383) | Link: https://github.com/antoinezambelli/forge

### TL;DR
Forge is a Python framework that wraps self-hosted LLMs with guardrails—response validation, retries, tool-step enforcement, and context compaction—to dramatically improve multi-step tool-calling reliability. It can be used as a workflow runner, pluggable middleware, or an OpenAI-compatible proxy that “makes small models act smarter” without changing clients. Benchmarks on a 26-scenario suite show big jumps in success rates, and HN discussion centers on harness design, small-model viability, and limits on very long-horizon tasks.

---

### Comment pulse
- Rich harnesses can decompose plans, validate each tool argument, and rewind conversations → cleaner histories and fewer tool-call failures — counterpoint: adds many extra round-trips.
- With retries and guardrails, small local models can perform “surprisingly well” → reasoning is often good enough; the main job is preventing uncorrected mistakes.
- Guardrails fix tool-call ambiguities (e.g., grep exit code 1) → improves medium-horizon reliability, but frontier models still win on very long contexts.

---

### LLM perspective
- View: Reliability layers will become standard for agents; tooling around validation, retries, and orchestration matters as much as model choice.
- Impact: Makes 7–14B local models viable for serious automation, reducing dependence on costly frontier APIs and large GPUs.
- Watch next: Head-to-head harness benchmarks, standardized agent-task suites, and stronger context/trace compaction to push small models on 100+ step workflows.
