# Granite 4.1: IBM's 8B Model Matching 32B MoE

- Score: 273 | [HN](https://news.ycombinator.com/item?id=47960507) | Link: https://firethering.com/granite-4-1-ibm-open-source-model-family/

### TL;DR

IBM’s Apache-2.0 Granite 4.1 family uses dense 3B, 8B, and 30B architectures trained across five phases on 15 trillion tokens. The 8B and 30B support 512K context; the 3B reaches 128K. IBM reports the 8B beating its prior 32B, 9B-active MoE on tool calling, 68.3 versus 64.7, while also posting strong math, code, and chat scores. Curated instruction filtering and four reinforcement-learning stages repaired a math regression after RLHF. However, comparisons use IBM’s evaluation harness and need independent validation.

### Comment pulse

- A local tester found the 8B fast and capable on commodity hardware, especially for autocomplete and small tasks, but preferred Qwen3.6 overall.
- The 4B vision variant attracted interest for compact table and key-value extraction if its reported benchmarks hold.
- Users seeking cloud-assistant replacements compared local chat interfaces, emphasizing persistence, tool support, usability, and hallucination costs.

### LLM perspective

- Dense models offer predictable activation cost but do not automatically beat similarly sized modern competitors.
- Long-context claims should be tested on retrieval, synthesis, latency, and memory—not advertised capacity alone.
- Enterprise adoption depends on reproducible tool calling, commercial licensing, and deployment support.
