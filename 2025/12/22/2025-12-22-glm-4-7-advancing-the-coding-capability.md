# GLM-4.7: Advancing the Coding Capability

- Score: 200 | [HN](https://news.ycombinator.com/item?id=46357287) | Link: https://z.ai/blog/glm-4.7

### TL;DR

Z.ai presents GLM-4.7 as an open-weight upgrade focused on coding, tools, reasoning, and generated-interface quality. Vendor-reported results improve over GLM-4.6 to 73.8% on SWE-bench Verified, 66.7% on SWE-bench Multilingual, and 41% on Terminal Bench 2.0. New reasoning modes think between tool calls, retain thinking blocks across turns, or toggle thinking per turn. The model works with several coding agents and local inference frameworks. Commenters praised price and output quality but warned that full-model memory and prompt-processing costs undermine casual local deployment.

### Comment pulse

- Users reported strong writing, math, and coding impressions, while acknowledging these were informal trials rather than controlled comparisons.
- Open weights reduce provider dependence, but large quantized models may remain slow even on high-memory consumer hardware.

### LLM perspective

- View: Preserved multi-turn reasoning may matter more operationally than another incremental benchmark lead.
- Impact: Affordable access broadens agent experimentation, while hardware requirements keep capable local inference specialized.
- Watch next: Require independent benchmarks covering latency, prompt ingestion, long-horizon stability, and memory across supported quantizations.
