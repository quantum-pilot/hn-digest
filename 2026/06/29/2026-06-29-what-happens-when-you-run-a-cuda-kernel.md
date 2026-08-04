# What happens when you run a CUDA kernel?

- Score: 195 | [HN](https://news.ycombinator.com/item?id=48718863) | Link: https://fergusfinn.com/blog/what-happens-when-you-run-a-gpu-kernel/

### TL;DR

One million-element CUDA vector add traverses a deep stack. `nvcc` compiles device code through PTX into SASS, embeds both with host registration and launch stubs, and leaves PTX for forward-compatible JIT. At first launch, the driver uploads code, places arguments and geometry in a QMD, queues it via pushbuffer and GPFIFO, then rings an MMIO doorbell. The RTX 4090 spreads blocks across 128 SMs, schedules warps with compiler control metadata and scoreboards, coalesces memory, and returns results through semaphores and DMA. HN praised the end-to-end explanation while correcting control-code details.

### Comment pulse

- The missing bridge became legible → QMD, pushbuffer, GPFIFO, and doorbell details connected launch syntax to the actual CPU-driver-GPU command path.
- CUDA chooses approachable defaults → the default stream implicitly sequences kernels and copies, while explicit streams make parallelism opt-in unlike Vulkan’s manual synchronization.
- Some low-level claims need refinement → commenters pointed to NVIDIA’s open hardware documentation and said control codes involve table lookup, not merely bit fields.

### LLM perspective

- **View:** Kernel launch latency and behavior emerge from orchestration across compiler, runtime, drivers, PCIe queues, schedulers, caches, and copy engines.
- **Impact:** Performance tuning requires locating the bottleneck’s layer; this example is memory-bound despite high occupancy and minimal arithmetic.
- **Watch next:** Validate encodings across GPU generations, separate initialization from steady-state cost, and measure streams, access patterns, and pinned transfers.
