# Show HN: Duplicate 3 layers in a 24B LLM, logical deduction .22→.76. No training

- Score: 235 | [HN](https://news.ycombinator.com/item?id=47431671) | Link: https://github.com/alainnothere/llm-circuit-finder

## TL;DR
This repo automates David Ng’s “repeat-yourself” trick: it searches for 3–4-layer “reasoning circuits” in transformer LLMs, then duplicates those layers in the forward pass (no training, weights unchanged). On Devstral-24B, repeating layers 12–14 boosts BBH logical deduction from 0.22 to 0.76, and improves GSM8K and MBPP without observed regressions; Qwen2.5-32B sees a large reasoning gain too. Different duplication patterns create distinct “modes” (math vs EQ). Overheads are modest: a few extra layers’ VRAM and latency.

## Comment pulse
- Novelty claim → Ng showed the phenomenon; this adds an automated sweep, benchmarks, and concrete layer locations—counterpoint: prior LLaMA/image-model hacks already duplicated layers.  
- Mechanism debate → some argue duplication just breaks harmful RLHF/refusal circuits; others point to residuals and shared representations enabling extra “refinement depth.”  
- Architectural implications → suggests training models with explicit loopable blocks, recursive circuits, or shuffled block training to encourage modular, reusable reasoning sub-networks.

## LLM perspective
- View: Treat transformers as containing overlapping, loopable circuits; architecture surgery can yield sizeable gains before any fine-tuning.  
- Impact: Model hackers and small labs get a cheap reasoning boost; framework authors might expose layer-routing as a first-class feature.  
- Watch next: Independent replications on many models, full-task regressions, and training-time designs with native loops or dynamic depth control.
