# SIMA 2: An agent that plays, reasons, and learns with you in virtual 3D worlds

- Score: 156 | [HN](https://news.ycombinator.com/item?id=45916037) | Link: https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/

- TL;DR
    - DeepMind’s SIMA 2 upgrades a screen-and-mouse game agent with Gemini reasoning: it plans from high‑level goals, handles multimodal prompts, transfers skills to unseen games (ASKA, MineDojo), and self‑improves via trial‑and‑error plus model feedback—including in Genie 3 generated worlds. Performance closes part of the human gap, but long‑horizon tasks, precise low‑level control, and short memory remain limits. HN debates real‑time learning versus staged retraining, applauds high‑FPS UI control for future desktop/phone agents, and weighs prospects for pairing such planners with robot low‑level controllers.

- Comment pulse
    - Not real-time learning → blog describes generational self-improvement from replayed experience; demos show competence during inference, not online parameter updates.
    - High-FPS screen-and-mouse control matters → could unlock fast desktop/phone agents for everyday tasks; current UI agents are bottlenecked by latency and slow perception loops.
    - Bridge to robotics → combine SIMA-like high-level planners with task-specific low-level controllers to execute household tasks — counterpoint: control complexity won’t yield to “more data” alone.

- LLM perspective
    - View: Embodied, high-throughput UI agents trained from pixels plus language are converging with planning LLMs; games are a scalable testbed.
    - Impact: Desktop automation, accessibility tools, and sim-to-real robotics pipelines could accelerate if latency and reliability match human-interaction baselines.
    - Watch next: Evidence of online continual learning, published throughput metrics (FPS, end-to-end latency), open benchmarks/SDKs, and safety mechanisms for autonomous self-improvement.
