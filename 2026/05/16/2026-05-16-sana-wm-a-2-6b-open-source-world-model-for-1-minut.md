# SANA-WM, a 2.6B open-source world model for 1-minute 720p video

- Score: 284 | [HN](https://news.ycombinator.com/item?id=48159445) | Link: https://nvlabs.github.io/Sana/WM/

### TL;DR

SANA-WM is a 2.6B image-and-camera-trajectory model for controllable 60-second 720p video. It combines Gated DeltaNet with periodic softmax attention, dual-branch metric 6-DoF control, a 17B refinement stage, and pose labels from roughly 213,000 public clips. Training took 15 days on 64 H100s; one H100 serves it, while a distilled RTX 5090 variant reportedly denoises a minute in 34 seconds. HN praised the efficiency but questioned open-source readiness and whether generated game worlds can preserve human intentionality rather than multiply polished, hollow content.

### Comment pulse

- Open-source status was contested → the page said weights were forthcoming, while commenters found a checkpoint and separate Apache code and NVIDIA model licenses.

- Generative scale can erode intentionality → plausible scenery may lack authored meaning — counterpoint: richer controls and human curation can make procedural worlds coherent.

- More output changes discovery economics → average quality may fall and noise rise, even if the absolute number of exceptional games increases.

### LLM perspective

- **View:** Game-design world models need persistent state and editable causality, not merely long photorealistic rollouts.

- **Impact:** Creators gain cheaper previs and environment prototyping; authored gameplay still needs structured objects, rules, and revision tools.

- **Watch next:** Test released weights, license compatibility, trajectory error, object permanence, branching consistency, controllable edits, prompt diversity, and deployment latency.
