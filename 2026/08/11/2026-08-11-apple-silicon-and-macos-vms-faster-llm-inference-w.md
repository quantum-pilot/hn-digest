# Apple Silicon and macOS VMs: Faster LLM Inference with llama.cpp

- Score: 292 | [HN](https://news.ycombinator.com/item?id=49259339) | Link: https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md

### TL;DR

A Cua research release uses a process-scoped Metal capability shim inside macOS Virtualization.framework guests, reporting Apple family 9 and 64 KB threadgroup memory so llama.cpp selects newer GPU kernels. On one M1 Ultra, TinyLlama improved 11.08× for prompts and 16.36× for generation; Gemma 4 12B reached 99.59% and 94.82% of bare-metal speeds. Muse Glimmer also gained 7.55–8.87×. The method does not accelerate bare-metal inference, stayed flat for MLX-LM, and depends on private, version-sensitive behavior.

### Comment pulse

- Several readers said the title obscured the VM-only scope; authors agreed and emphasized that stock capability reporting caused slow kernel selection.
- Why Apple advertises a conservative virtual GPU profile remained unanswered, with safety, VM portability, and product policy offered as possibilities.
- Broader Metal apps might benefit — counterpoint: each API, chip, host, and guest combination requires independent validation.

### LLM perspective

- **View:** Benchmark selected kernel paths before concluding virtualized hardware is inherently slow.
- **Impact:** VM inference can approach host speed without device passthrough, but compatibility testing becomes release-specific operational work.
- **Watch next:** Apple guidance, broader host/guest matrices, other Metal applications, and fail-safe behavior after macOS updates.
