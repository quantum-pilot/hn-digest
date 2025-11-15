# Why Fei-Fei Li and Yann LeCun are both betting on "world models"

- Score: 133 | [HN](https://news.ycombinator.com/item?id=45923326) | Link: https://entropytown.com/articles/2025-11-13-world-model-lecun-feifei-li/

TL;DR
- “World model” now spans three bets: Marble turns prompts into editable 3D assets (Gaussian splats/meshes); DeepMind’s Genie 3/SIMA 2 generates interactive simulators for agent learning; LeCun’s JEPA pursues latent predictive cognition for planning. HN debates stress LLMs’ limits for control, enthusiasm for self‑supervised representation (e.g., Dreamer), and whether language’s compression advantages translate to vision/physics. The piece urges separating interface vs simulator vs cognition and checking what each system outputs, for whom, and what it remembers.

Comment pulse
- LLMs struggle at real-time control; aim for continuous self-supervised world models → batch training misses nonstationary dynamics — counterpoint: math is the needed world model.
- Dreamer-style agents train purely in imagined rollouts → evidence: Dreamer4 learns Minecraft diamond acquisition from video, no environment interaction; Hafner’s departure raises where-next speculation.
- LLMs piggyback on language’s compression; unclear analog for world models → video and interaction supply rich priors; physics-grounded embeddings may outperform text co-occurrence.

LLM perspective
- View: Disambiguate three “world model” senses: human-facing assets, simulators for learning, and latent predictive cognition; evaluate claims accordingly.
- Impact: Game/VR pipelines benefit now; robotics and autonomous agents hinge on simulators plus predictive latents; LLM vendors may rebrand without advances.
- Watch next: Comparable benchmarks: long-horizon control, persistence/memory tests, sim-to-real transfer; LeCun startup plans, Genie latency/controllability, Hafner’s next project.
