# RTX 5090 and M4 MacBook Air: Can It Game?

- Score: 457 | [HN](https://news.ycombinator.com/item?id=48137145) | Link: https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/

### TL;DR

An engineer made an RTX 5090 work with an M4 MacBook Air, passing the Thunderbolt PCIe device from macOS into an Arm Linux VM, then layering FEX and Proton for x86 Windows games. Custom QEMU, DriverKit, and guest-kernel code works around Apple’s 1.5 GB DMA and 64,000-mapping limits; the GPU cannot accelerate macOS applications. Cyberpunk at 4K ray tracing rose from roughly 3 fps natively to 27 fps, or 111 with frame generation, while one game exceeded the DMA ceiling. HN admired the engineering but emphasized Apple’s missing passthrough support.

### Comment pulse

- Local inference drew practical interest: a 4,000-token prompt reached first output around 113–120 times faster on the 5090 than M4 Air.
- This is Linux-VM passthrough, not native macOS eGPU support; host applications still cannot use the card.
- Apple appears to ship internal passthrough machinery — counterpoint: retail frameworks lack the required support, leaving fragile community workarounds.

### LLM perspective

- View: The project proves feasibility, but FEX’s roughly 50% CPU penalty makes performance workload-dependent rather than universally transformative.
- Impact: GPU-bound games and model prefill accelerate sharply; CPU-bound titles, unsupported workloads, and platform maintenance remain poor fits.
- Watch next: Larger DART windows, fewer mapping limits, upstream QEMU support, native drivers, reproducible setup, and optimized MLX comparisons.
