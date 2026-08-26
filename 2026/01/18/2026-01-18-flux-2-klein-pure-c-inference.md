# Flux 2 Klein pure C inference

- Score: 192 | [HN](https://news.ycombinator.com/item?id=46670279) | Link: https://github.com/antirez/flux2.c

### TL;DR

This snapshot describes flux2.c’s initial FLUX.2-klein-4B implementation: a Claude-generated C library and CLI for text-to-image and image-to-image inference from an approximately 16GB model directory. Inference needs only the C standard library, with optional BLAS or Apple MPS, but uses float32 and no quantization; its recorded M3 Max results were roughly ten times slower than PyTorch MPS. Salvatore Sanfilippo wrote no code but supplied design guidance and reference-feedback loops. HN focused on persistent specifications, auditability, prompt histories, and reviewing generated kernels.

### Comment pulse

- Persistent implementation notes preserved context → commenters saw living specifications and experiment logs as essential infrastructure for long agentic work.
- Reference implementations create feedback → measurable parity can guide generation, but human and cross-model review still catch logic errors.
- Fast AI ports challenge maintainers → rejected generated kernels may spur faster forks, though contributors remain uneasy about code they cannot vouch for.

### LLM perspective

- View: The experiment demonstrates orchestration capacity more clearly than runtime efficiency; the frozen benchmarks favor PyTorch substantially.
- Impact: Experienced developers can prototype inference stacks quickly, shifting effort toward specifications, validation, and maintenance.
- Watch next: Measure correctness, kernel quality, quantization, memory use, and performance against the same Klein model directory.
