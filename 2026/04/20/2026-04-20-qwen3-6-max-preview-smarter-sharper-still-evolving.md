# Qwen3.6-Max-Preview: Smarter, Sharper, Still Evolving

- Score: 509 | [HN](https://news.ycombinator.com/item?id=47834565) | Link: https://qwen.ai/blog?id=qwen3.6-max-preview

### TL;DR
Alibaba’s Qwen3.6-Max-Preview is a new proprietary, cloud-only flagship model focused on “agentic coding,” world knowledge, and instruction-following. It shows sizable gains over Qwen3.6-Plus on coding (SWE-Bench Pro, Terminal-Bench 2.0, SkillsBench, SciCode), knowledge (SuperGPQA, QwenChineseBench), and tool-call formatting. The API is OpenAI/Anthropic-compatible and supports streaming reasoning traces via `enable_thinking` and `preserve_thinking`, targeting complex multi-step agents. HN discussion centers on real-world coding performance, cost vs Kimi K2.6, and the strategic role of open-weight Qwen models.

---

### Comment pulse
- Benchmarks vs reality → Users report GLM/Qwen sometimes outperform Claude/GPT on specific coding tasks; SWE-bench is Python-heavy, so scores don’t fully capture model strengths.  
- Cloud vs local → Self-hosting large Qwen/Gemma on consumer GPUs is slow and memory-constrained, yet open-weight 32B/72B Qwen is already “good enough” for many local workloads.  
- Open vs proprietary → Concern about “free, then closed” patterns; Chinese labs often move in reverse, opening larger models as a strategic and marketing play — counterpoint: rising prices erode this advantage.

---

### LLM perspective
- View: Max-Preview targets high-value agent workflows, not hobbyist local use; open-weight Qwen is the real story for community adoption.  
- Impact: Enterprise coding assistants and tool-heavy agents gain options beyond US vendors, especially where Chinese clouds are cheaper or politically preferred.  
- Watch next: Side-by-side coding benchmarks vs Kimi, Claude, GPT; latency/price comparisons; and whether next Qwen open weights inherit Max-Preview’s agentic skills.
