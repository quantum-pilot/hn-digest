# Nvidia Cosmos 3

- Score: 142 | [HN](https://news.ycombinator.com/item?id=48356654) | Link: https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/

## TL;DR
Nvidia’s Cosmos 3 is an open-source “physical AI” foundation model that unifies perception, physical reasoning, world prediction, and action generation for domains like robotics, autonomous driving, and warehouse monitoring. It uses a two-tower Mixture-of-Transformers: an autoregressive vision-language “reasoner” and a diffusion-based “generator” for physics-aware video and action sequences. Released are 16B (Nano) and 64B (Super) checkpoints, six synthetic world-model datasets, full post-training recipes, a new human eval benchmark (HUE), and optimized NIM microservices for GPU deployment.

## Comment pulse
- SOTA open-source image/video generator → Beats many peers but 64B “Super” is impractically large for typical hardware; 16B “Nano” still hefty.
- Not just another image model → Targeted world model for robots/AVs with physics-aware data and harnesses, not a direct competitor to consumer image-gen tools.
- Architecture debate → Some see the two-tower MoT as over-engineered vs the Bitter Lesson; others argue it’s still “just scaling” over rich multimodal data.

## LLM perspective
- View: This is Nvidia pushing beyond chatbots toward general-purpose world models tightly coupled to their simulation and robotics stack.
- Impact: Most benefit goes to labs and companies with serious GPUs, robots, and AV stacks; hobbyists mostly get benchmarks and datasets.
- Watch next: Third-party robotics/AV benchmarks, real-world policy-learning demos, and whether lighter Cosmos variants reach consumer GPUs.
