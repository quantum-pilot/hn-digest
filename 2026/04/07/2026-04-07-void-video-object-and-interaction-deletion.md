# VOID: Video Object and Interaction Deletion

- Score: 180 | [HN](https://news.ycombinator.com/item?id=47627998) | Link: https://github.com/Netflix/void-model

### TL;DR

Netflix researchers released VOID, an Apache-licensed video inpainting system that removes a selected object plus its physical and visual effects on the scene. Unlike ordinary deletion, removing a person holding a guitar can make the instrument fall, while masks distinguish the primary object, overlaps, affected regions, and preserved background. Built on CogVideoX, VOID offers sequential base and warped-noise refinement checkpoints; Gemini and SAM2 generate masks. Running the notebook needs at least 40 GB of GPU memory, and training used eight A100 80GB GPUs.

### Comment pulse

- Examples exposed inconsistent causal handling: a removed kettlebell restored its pillow, while removing a child’s hands left spinning tops upright.
- Filmmakers welcomed cheaper VFX and open research — counterpoint: mass-access video doctoring could amplify deception, censorship, and AI-generated spam.
- Commenters expected richer controls to restore artistic intent, paralleling image generation’s evolution from text prompts to depth maps and ControlNets.

### LLM perspective

- **View:** Counterfactual scene editing meaningfully advances beyond pixel replacement, but demonstrated physical reasoning remains brittle.
- **Impact:** Small creators could attempt effects once requiring specialist teams, while evidentiary video becomes easier to alter plausibly.
- **Watch next:** Longer-horizon causality, controllable interaction scope, temporal artifacts, compute reductions, provenance marking, misuse safeguards, and independent benchmark results.
