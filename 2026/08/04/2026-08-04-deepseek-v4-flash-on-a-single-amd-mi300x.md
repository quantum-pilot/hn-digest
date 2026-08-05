# DeepSeek V4 Flash on a Single AMD MI300X

- Score: 370 | [HN](https://news.ycombinator.com/item?id=49166386) | Link: https://github.com/ryanzhou/deepseek-v4-flash-mi300x

### TL;DR

A community configuration runs the 304B-parameter DeepSeek-V4-Flash-0731 on one AMD MI300X without additional weight quantization or offloading, fitting 156.67 GiB of weights in HBM and reaching 168.6 tokens/s median single-stream decode. Eight streams produced 542 tokens/s aggregate; a 64-request burst reached 830 without errors. The setup validates 256K context, below the architecture’s 1M, and required patches for AMD FP8, MoE routing, speculative verification, CPU-KV synchronization, and kernel shapes. HN praised the substantive result but noted MI300X hardware is specialized and costly.

### Comment pulse

- Full weights at high decode speed make this unusually credible → the result avoids tiny-memory demonstrations that merely spill everything to slow storage.
- A 256K validated window is a practical compromise → most workloads fit, though it leaves the advertised 1M architecture unproven.
- MI300X is not a consumer card → OAM packaging, host requirements, availability, and price complicate personal ownership despite cloud rentals.

### LLM perspective

- **View:** Vendor-specific runtime repair, not model compression, is the central achievement.
- **Impact:** MI300X operators gain a reproducible path to serve a frontier-scale sparse model on one accelerator.
- **Watch next:** One-million-token stability, sustained production loads, patch upstreaming, and results on newer AMD hardware.
