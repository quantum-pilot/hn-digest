# MAI-Code-1-Flash

- Score: 362 | [HN](https://news.ycombinator.com/item?id=48374466) | Link: https://microsoft.ai/news/introducingmai-code-1-flash/

### TL;DR
Microsoft’s Superintelligence team released MAI-Code-1-Flash, a proprietary coding model now rolling out inside GitHub Copilot for VS Code. It’s trained directly in Copilot’s production harness, emphasizing “agentic” behavior with tools and adaptive response length, and is benchmarked primarily against Anthropic’s Claude Haiku 4.5, where it wins on accuracy and uses up to 60% fewer tokens. Hacker News reception is mixed: people question benchmarking only against Haiku, note the model’s large size versus modest gains, debate the value of small cloud models, and criticize the Anthropic-like site design.

---

### Comment pulse
- Model positioning → 137B parameters but only slightly ahead of Qwen 3.6-35B; beating Haiku 4.5 is seen as an easy, outdated target.  
- Small models in workflows → Many say Haiku-class models waste time vs Opus/DeepSeek; others report big savings using them as execution workers under a large “planner” model.  
- Ecosystem & UX → Copilot’s new per-token pricing and Microsoft’s Anthropic-style, accessibility-poor site push some developers toward self-hosted Qwen/DeepSeek instead.

---

### LLM perspective
- View: This is mainly a Copilot-embedded, Haiku-class workhorse, not a direct Opus/GPT-5.5 competitor.  
- Impact: Most relevant for developers locked into Copilot who want cheaper, faster routine edits and refactors.  
- Watch next: Real user latency/quality reports, comparisons vs Qwen/DeepSeek, and whether Microsoft ships a larger “Sonnet/Opus-class” in Copilot.
