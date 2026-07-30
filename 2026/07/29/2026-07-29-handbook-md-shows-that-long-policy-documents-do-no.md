# Handbook.md shows that long policy documents do not reliably govern agents

- Score: 275 | [HN](https://news.ycombinator.com/item?id=49096969) | Link: https://arxiv.org/abs/2607.25398

### TL;DR
The paper introduces HANDBOOK.md, a benchmark where agents must follow 20–124 page “company handbooks” while doing realistic multi-step work (finance, HR, billing, etc.) via tools like email, calendars, and issue trackers. Success requires both doing required actions and avoiding prohibited ones, graded by 824 deterministic checks. Even the best evaluated configurations pass only 36% of tasks; many are below 25%. HN discussion stresses that giant context windows and static policy files don’t reliably control agents and that real reliability likely needs training, structure, and better harnesses, not just longer prompts.

### Comment pulse
- Long context is fragile → effective usable window is far below “1M tokens”; quantization, attention limits, and RoPE cause recall and adherence to degrade.  
- Humans also fail at 100‑page policies → true reliability usually comes from training, feedback, and procedural scripts, not dumping the whole handbook in front of a worker.  
- Practical takeaway → keep static instructions short, structure workflows as graphs of focused one-shot prompts, fine-tune or script agents before trusting handbook-in-context governance.

### LLM perspective
- View: Benchmarks like this expose that “just stuff policies in context” is fundamentally inadequate for safety- or compliance-critical agents.  
- Impact: Enterprise AI teams must rethink designs: more tooling, retrieval, and training; less blind faith in long system prompts.  
- Watch next: Results on upcoming frontier models, RAG+policy tooling benchmarks, and methods that distill large handbooks into train-time or tool-level constraints.
