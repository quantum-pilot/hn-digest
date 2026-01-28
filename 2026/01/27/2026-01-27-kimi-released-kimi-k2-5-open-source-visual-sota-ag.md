# Kimi Released Kimi K2.5, Open-Source Visual SOTA-Agentic Model

- Score: 453 | [HN](https://news.ycombinator.com/item?id=46775961) | Link: https://www.kimi.com/blog/kimi-k2-5.html

### TL;DR
Kimi K2.5 is a 1T-parameter, open-source, native multimodal MoE model (32B active) focused on coding with vision and large-scale “agentic” workflows. It’s pretrained on ~15T text+vision tokens and can reconstruct UIs from images/video, do autonomous visual debugging, and handle real-world software engineering via tools and Kimi Code. Its key novelty is a self-directed agent swarm: up to 100 sub-agents and 1,500 tool calls, trained with parallel-agent RL and a latency-oriented “critical steps” metric to cut wall-clock time by up to 4.5× on complex, tool-heavy tasks.

---

### Comment pulse
- License quirk → MIT-like, but products over 100M MAU or $20M/month revenue must prominently show “Kimi K2.5” in the UI—counterpoint: feels like a branding fee instead of cash.
- Open mega-model economics → Awe at a 1T-parameter release plus skepticism: few can run it locally, unclear business model, and concerns about hype vs actual adoption (e.g., DeepSeek parallels).
- Safety and agents → Some worry that strong open models plus agent swarms will materially help cyber and future bio attacks, especially given they’re coming from competitive, not humanitarian, actors.
- Agent-swarm practicality → RL-trained orchestration for 100 sub-agents is seen as a big step, but 1,500 tool calls per task raises serious unit-economics and infrastructure concerns.

---

### LLM perspective
- View: The real innovation is RL-trained orchestration and parallelism, not just another big vision-coding model.
- Impact: Most benefits will accrue via hosted APIs and IDE integrations; home deployment is largely symbolic at this scale.
- Watch next: Independent swarm benchmarks, cost-per-task analyses, and safety evaluations for autonomous multi-agent systems using open weights.
