# Caveman: Why use many token when few token do trick

- Score: 670 | [HN](https://news.ycombinator.com/item?id=47647455) | Link: https://github.com/JuliusBrussee/caveman

### TL;DR
- Caveman is a Claude Code/Codex plugin that post-processes model responses into “caveman speak”: same code/technical content, far fewer words. Benchmarks on coding-style tasks show about 65–75% fewer output tokens, promising lower costs and faster responses without touching the model’s hidden reasoning. The author stresses it’s a joke-turned-tool, not a claim of deeper intelligence gains, and that real evaluation must measure end-to-end latency, quality, and skill overhead. HN discussion debates style constraints, attention budget, and mixed real-world results.

### Comment pulse
- Author: plugin only compresses visible completion, not reasoning; claims should be modest until proper benchmarks exist → focus on end-to-end tokens, latency, task success.  
- Style constraints may steal capacity from reasoning → attention budget is limited; enforcing persona/voice can hurt accuracy — counterpoint: Anthropic’s RL-tuned coding models seem robust to mild style shifts.  
- Some users see more misunderstandings with caveman talk; others like extra “fluff” as useful redundancy → alternative idea: use “richer” technical tokens instead of primitive grunts.

### LLM perspective
- View: Post-processing for terseness is low risk; main question is usability and error rate under tighter phrasing.  
- Impact: Heavy code/chat users, API-cost-sensitive teams, and tools like IDE agents benefit most from cheaper, denser answers.  
- Watch next: Independent benchmarks on standard coding/QA suites; ablations on style constraints; richer-token prompting recipes vs caveman mode.
