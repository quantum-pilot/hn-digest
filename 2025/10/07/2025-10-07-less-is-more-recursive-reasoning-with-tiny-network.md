# Less is more: Recursive reasoning with tiny networks

- Score: 197 | [HN](https://news.ycombinator.com/item?id=45506268) | Link: https://alexiajm.github.io/2025/09/29/tiny_recursive_models.html

- TL;DR
  - A 7M‑parameter Tiny Recursion Model (TRM) tackles ARC‑AGI by iteratively refining a latent state z and answer y over K steps, achieving 45% on ARC‑AGI‑1 and 8% on ARC‑AGI‑2—rivaling far larger LLMs. It simplifies HRM‑style recursive reasoning to a minimal loop without hierarchies or fixed‑point math. HN welcomes small‑model reasoning but flags that results may depend on ARC‑AGI’s augmented/test‑time‑training protocol, questions generality beyond spatial tasks, and debates compute impact: cheaper inference could raise demand, and incumbents would adopt any gains.

- Comment pulse
  - Strong scores may reflect special ARC‑AGI protocol → HRM analysis: data aug/test‑time training lets vanilla transformers near HRM — counterpoint: TRM simplifies design, enabling ablations.
  - Not a general LLM replacement → Recurrence helps spatial reasoning; no path yet to text generation; likely needs integration with broader systems.
  - Tiny models could shift compute economics → cheaper reasoning increases demand (Jevons), and GPUs still needed for video; incumbents would adopt advances.

- LLM perspective
  - View: Recursive self-improvement with tiny nets is promising but benchmark hygiene is crucial to validate true general reasoning gains.
  - Impact: If robust, education, robotics, and edge devices gain cheap reasoning; labs pivot to algorithmic advances over mere scale.
  - Watch next: Independent replications under standard ARC‑AGI protocol; ablations vs unrolled baselines; transfers to text tasks or hybrid systems.
