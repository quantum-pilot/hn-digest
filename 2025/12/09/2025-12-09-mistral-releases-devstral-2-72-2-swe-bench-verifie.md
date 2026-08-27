# Mistral Releases Devstral 2 (72.2% SWE-Bench Verified) and Vibe CLI

- Score: 462 | [HN](https://news.ycombinator.com/item?id=46205437) | Link: https://mistral.ai/news/devstral-2-vibe-cli

### TL;DR

Mistral released Devstral 2, a 123B coding model with a claimed 72.2% SWE-bench Verified score, alongside 24B Devstral Small 2 at 68.0% and the open-source Vibe CLI agent. Both support 256K context; the larger model uses a modified MIT license and needs at least four H100-class GPUs, while Small uses Apache 2.0 and targets local hardware. Mistral’s own human evaluation beat DeepSeek V3.2 but still preferred Claude Sonnet 4.5, tempering its efficiency and open-model positioning.

### Comment pulse

- Early users report competent, localized changes → anecdotes remain too limited to establish reliability across production codebases.
- Local deployment attracts hobbyists → hardware choices involve sharp tradeoffs among VRAM, speed, CUDA support, power, and cloud rental.
- SVG demos look impressive → commenters warn that familiar prompts may be trained or benchmark-optimized and are not executable-code tests.

### LLM perspective

- View: The smaller model’s deployability may matter more than leaderboard proximity if independent evaluations confirm useful agent behavior.
- Impact: Teams gain another private, customizable coding stack without depending entirely on proprietary model providers.
- Watch next: Reproduce SWE-bench, audit the modified license, benchmark real repositories, and measure regression rates and local throughput.
