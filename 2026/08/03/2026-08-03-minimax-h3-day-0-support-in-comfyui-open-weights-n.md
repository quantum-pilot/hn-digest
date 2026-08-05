# MiniMax H3 Day-0 Support in ComfyUI: Open Weights, Native Audio, and 2K Video

- Score: 329 | [HN](https://news.ycombinator.com/item?id=49155629) | Link: https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui

### TL;DR

MiniMax H3 is an open-weight video model with day-zero ComfyUI support, accepting text, images, video, and audio to generate clips up to 15 seconds and 2K with native stereo sound. ComfyUI replaced roughly 40% of modulation weights with a timestep lookup table, added INT8 convrot quantization and custom kernels, and reduced total memory from 123.6 GB to 42.5 GB before dynamic offloading. Users reported strong 480p results on 16 GB GPUs, but generation still took roughly 3–10 minutes and unusual motion exposed artifacts.

### Comment pulse

- Lookup-table pruning is diffusion-specific → timestep-conditioned normalization values can be precomputed; general LLMs usually lack equivalent modulation weights.
- Local quality impressed → 10-second 480p clips took about three minutes on a 5080 and ten on a 4070 Ti Super.
- Production economics remain difficult → odd scenes break, high resolution disappoints, and professionals need many parallel generations rather than serial waiting.

### LLM perspective

- View: Open weights plus consumer execution matter most for experimentation, privacy, and controllable creative pipelines.
- Impact: Hobbyists gain capable video tooling; studios still benefit from cloud concurrency and conventional rendering for precise shots.
- Watch next: Cross-clip continuity, high-resolution quality, motion benchmarks, and workflow-level comparisons against leading hosted models.
