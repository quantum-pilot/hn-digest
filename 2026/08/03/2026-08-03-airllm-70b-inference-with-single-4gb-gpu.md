# AirLLM 70B inference with single 4GB GPU

- Score: 230 | [HN](https://news.ycombinator.com/item?id=49154228) | Link: https://github.com/lyogavin/airllm

### TL;DR

AirLLM minimizes VRAM by loading one transformer layer—or one routed expert for sparse MoE models—at a time from disk, claiming 70B inference on 4 GB and Kimi K3’s 2.8T parameters in 3.72 GB. It supports many Hugging Face families, optional weight compression, prefetching, CPUs, and Apple Silicon, but still requires downloading and storing the model. HN’s central caveat was speed: Kimi K3 reportedly needs 292 seconds per token, making feasibility very different from usability and inviting comparisons with mmap, llama.cpp, and CPU inference.

### Comment pulse

- Tiny VRAM is real but misleading → layer streaming shifts the bottleneck to storage; reported K3 throughput is one token every 292 seconds.
- Existing alternatives deserve comparison → readers asked whether llama.cpp, mmap, CPU offload, or expert-streaming flags already provide a more maintained path.
- Disk remains mandatory → the complete checkpoint must be downloaded and split, even when only one layer occupies VRAM.

### LLM perspective

- View: AirLLM expands what can technically execute, not what is interactively useful.
- Impact: Researchers can inspect oversized models cheaply; coding assistants and chat users will usually prefer smaller, resident models.
- Watch next: End-to-end latency benchmarks against CPU and llama.cpp, storage-bandwidth scaling, and sustained maintenance.
