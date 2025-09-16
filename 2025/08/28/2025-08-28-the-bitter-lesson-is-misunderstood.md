# The Bitter Lesson Is Misunderstood

- Score: 367 | [HN](https://news.ycombinator.com/item?id=45057283) | Link: https://obviouslywrong.substack.com/p/the-bitter-lesson-is-misunderstood

- TL;DR
    - The essay argues we misread Sutton’s Bitter Lesson: under Chinchilla-optimal scaling, compute is yoked to data. With C ∝ D², doubling compute needs ~1.41× more data; otherwise, extra GPUs underperform. Internet-grade text (~10T usable tokens) is near exhaustion, so progress shifts to two levers: Architect (architectures that raise data efficiency: SSMs, HRM, ParScale) and Alchemist (verifiable-reward engines—self-play/RL/agentic loops—creating new high-signal data). HN debates real-world grounding and RL-driven synthesis versus transformer limits at 4–8h METR tasks.

- Comment pulse
    - Verifiable rewards unlock scalable data for 4–8h tasks → build checkable environments for RL/self-play — counterpoint: what lacks metrics gets ignored, risking blind spots.
    - Data scarcity disputed → humans learn with less; real-world grounding and synthetic loops could be ‘infinite’; overparameterization and quantization hint inefficiency.
    - Consensus trend → transformer pretraining hits D bottleneck; paths: new architectures, better RL, or real-world interaction; confusion clarified: doubling compute needs ~1.41× data under C∝D².

- LLM perspective
    - View: Treat data as the scarce asset; optimize for verifiable-reward generation and architectures that raise data efficiency.
    - Impact: Budgets shift from GPU procurement to data pipelines, simulators, evals; orgs need measurable long-horizon tasks and closed-loop training.
    - Watch next: Benchmarks on 4–8h METR tasks, releases enabling verifiable agentic loops, and licensing moves unlocking new high-quality corpora.
