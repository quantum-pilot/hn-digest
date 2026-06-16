# Openrouter Fusion API

- Score: 196 | [HN](https://news.ycombinator.com/item?id=48537641) | Link: https://openrouter.ai/openrouter/fusion

### TL;DR
OpenRouter’s Fusion API turns each request into a mini-ensemble: several “analysis” models answer in parallel (with web tools), then a judge model synthesizes consensus, contradictions, and blind spots into one response. Benchmarks on deep research tasks show this can match or beat a single frontier model, especially by increasing test-time compute, but at higher cost and latency. HN commenters note that, in practice, judging and panels only help in specific, verifiable tasks and are often worse than just using one stronger model.

---

### Comment pulse
- Judge models rarely improve fuzzy tasks → they mostly reward answers similar to their own, adding latency and cost—counterpoint: structured issue-finding on verifiable tasks (e.g. resumes) works well.  
- Gains often come from more samples, not model diversity → multiple runs or self-fusion plus an LLM judge approximate majority voting; mixing models can even degrade ensemble quality.  
- Heavy multi-agent workflows exist in the wild → elaborate panel/rebuttal schemes can surface more issues, but are complex, slow, expensive, and may not beat a single frontier run.

---

### LLM perspective
- View: Fusion productizes LLM ensembling, combining panel outputs and an LLM judge into a single OpenAI-compatible endpoint.  
- Impact: Most useful for high-stakes research, evaluation, or safety checks where extra compute is cheaper than being wrong.  
- Watch next: Systematic benchmarks on cheap-model fusions, and whether fused outputs can train smaller distilled models with similar reliability.
