# Mistral Medium 3.5

- Score: 409 | [HN](https://news.ycombinator.com/item?id=47949642) | Link: https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5

### TL;DR
Mistral Medium 3.5 is a new 128B dense “merged” model (instructions, coding, reasoning, vision) with 256k context and open weights under a modified MIT license. It’s tuned for long-horizon, tool-using “agentic” work and now powers two features: Vibe remote coding agents (cloud sandboxes that run async, integrate with GitHub/Jira/Sentry, and open PRs) and Le Chat’s new Work mode, which orchestrates multi-step, cross-tool tasks. Positioned as ~frontier-minus-20% capability but far cheaper and self-hostable.

---

### Comment pulse
- Local-first crowd: 70GB Q4 is impressive vs 400–600GB peers, but token speeds on Macs/consumer hardware may be too slow for interactive use.  
- Benchmark skeptics: many open-weight launches “beat Sonnet” on paper; real-world responsiveness, context length, and quantization quality rarely match cloud Sonnet/Opus performance.  
- Competitive landscape: DeepSeek v4 Flash at 2-bit with high speed challenges the value of a 128B dense model; some question why Mistral moved away from MoE.

---

### LLM perspective
- View: This is less a pure model release and more an “agent platform” push: long-running, tool-rich workflows as the main product.  
- Impact: Stronger open-weight option for enterprises wanting EU vendor diversity, on-prem deployment, and GitHub/Jira/SaaS-integrated coding agents.  
- Watch next: Independent evals of agent performance vs DeepSeek/Qwen/Sonnet, practical local quantization benchmarks, and whether future 3.6/3.7 return to MoE.
