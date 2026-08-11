# Right-sizes LLM models to your system's RAM, CPU, and GPU

- Score: 257 | [HN](https://news.ycombinator.com/item?id=47211830) | Link: https://github.com/AlexsJones/llmfit

### TL;DR

llmfit is a Rust terminal tool that detects RAM, CPUs, GPUs, unified memory, and acceleration backends, then ranks local models by estimated quality, speed, memory fit, and context. It chooses the highest fitting quantization, handles multiple GPUs and MoE offloading, supports Ollama, llama.cpp, and MLX downloads, emits JSON, and can invert the calculation to recommend hardware. Its throughput formula uses bandwidth, model size, and an efficiency factor rather than running benchmarks. Commenters liked the interface but reported stale recommendations and false negatives, treating results as a first-pass estimate.

### Comment pulse

- A website would avoid installing binaries — counterpoint: browser sandboxes cannot automatically inspect detailed GPUs, VRAM, backends, or installed models.
- Parameter size and memory bandwidth provide useful bounds, while context caches, offloading, quantization, and kernels complicate actual performance.
- Fast model releases already outpace the embedded database; one user ran a model the tool marked impossible.

### LLM perspective

- **View:** Automated triage is valuable when its estimates are presented as hypotheses rather than compatibility verdicts.
- **Impact:** New local-model users can narrow hundreds of choices before spending bandwidth and time on downloads.
- **Watch next:** Database freshness, calibration against measured throughput, unsupported quantizers, false-negative rates, and user-supplied hardware planning.
