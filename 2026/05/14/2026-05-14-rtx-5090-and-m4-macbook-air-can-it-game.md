# RTX 5090 and M4 MacBook Air: Can It Game?

- Score: 457 | [HN](https://news.ycombinator.com/item?id=48137145) | Link: https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/

### TL;DR
A developer bolts an RTX 5090 onto an M4 MacBook Air via Thunderbolt and makes it usable inside an ARM Linux VM with QEMU/Hypervisor.framework GPU passthrough. They work around Apple Silicon’s DART IOMMU limits (1.5 GB window, ~64k mappings, no alignment control) using a custom virtual PCI device, guest driver, DMA “clustering,” and kprobe-based patches for NVIDIA’s ARM driver, plus Apple’s hardware TSO mode. Result: big gains for high‑res gaming and massive speedups for LLM prefill, but still far from a native Windows PC.

---

### Comment pulse
- Apple should have first‑class GPU passthrough → Mac Pro and Virtualization.framework already hint at internal support; exposing it would avoid these hacks.  
- This unlocks serious local LLM use → RTX 5090 obliterates Apple Silicon on prefill/TTFT, making long‑context work practical—counterpoint: MLX/oMLX may still be under‑optimized.  
- Not a normal eGPU on macOS → GPU is only usable inside the Linux VM; macOS apps still can’t render or accelerate on it.

---

### LLM perspective
- View: Treat this as a proof‑of‑concept that Apple hardware plus NVIDIA can be an excellent local‑LLM workstation, if software barriers fall.  
- Impact: Power users needing long‑context, multi‑session inference gain the most; mainstream gamers are still better off with native Windows PCs.  
- Watch next: Apple’s stance on PCI passthrough/DART limits, NVIDIA ARM64 Windows drivers, and better-optimized Metal/MLX prefill kernels and batching.
