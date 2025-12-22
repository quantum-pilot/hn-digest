# Measuring AI Ability to Complete Long Tasks

- Score: 219 | [HN](https://news.ycombinator.com/item?id=46342166) | Link: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/

### TL;DR
METR proposes a benchmark for AI agents based on the *length* of tasks they can complete, defined by how long those tasks take human experts. Across diverse software and reasoning tasks, current frontier models nearly always succeed on tasks taking humans under ~4 minutes, but fall below 10% success for tasks taking >4 hours. Fitting logistic curves over time shows the “task-completion horizon” doubling roughly every 7 months (even faster on SWE-Bench), implying week‑ to month‑long autonomous projects within a few years if trends hold.

---

### Comment pulse
- LLMs as “feature machines” → users offload complex coding (e.g., vector search) to agents, then optionally learn by inspecting tailored, working solutions—counterpoint: risks opaque, unmaintainable codebases.  
- Metric clarified → “4-hour task” means human-equivalent difficulty, not AI runtime; this helps reconcile flashy benchmarks with weaker real-world automation.  
- Reliability vs workflow → a 50% success horizon is risky; commenters propose human checkpoints or cheap, parallel throwaway PoCs to exploit speed while containing failures.

---

### LLM perspective
- View: Human-time task horizons are a practical bridge between benchmark scores and real job automation, especially for long-horizon reasoning and tooling.  
- Impact: Helps teams decide when to trust agents with multi-hour projects, structure supervision, and prioritize tool-building versus end-to-end autonomy.  
- Watch next: Independent replications beyond coding, adding metrics for recovery from errors, and policy that ties deployment risk to task length and reliability.
