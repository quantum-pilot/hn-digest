# Apple approves driver that lets Nvidia eGPUs work with Arm Macs

- Score: 334 | [HN](https://news.ycombinator.com/item?id=47640380) | Link: https://www.theverge.com/tech/907003/apple-approves-driver-that-lets-nvidia-egpus-work-with-arm-macs

### TL;DR
Apple has approved Tiny Corp’s kernel extension so Arm-based Macs can use external Nvidia and AMD GPUs for local LLM workloads without disabling System Integrity Protection. The driver isn’t from Nvidia, isn’t plug-and-play, and must be compiled (often via Docker) and used through Tinygrad, not CUDA or PyTorch. HN sees it as a technically impressive but niche breakthrough, debating its practical value under Thunderbolt bandwidth limits and Apple’s history of blocking third‑party GPU drivers.

---

### Comment pulse
- Neat hack, limited utility → Thunderbolt bottlenecks, no CUDA/Vulkan/PyTorch, fragile against future macOS updates; easier to buy a used PC for Nvidia.  
  — counterpoint: tooling only improves once hardware access exists.

- Scope and stack constraints → Works via Tinygrad’s own userspace driver; Docker is for compiling GPU code, not a full Linux VM passthrough.

- Policy/antitrust angle → Some view Apple’s historic refusal to sign Nvidia drivers as anticompetitive; others note Apple’s non‑monopoly status and small Mac GPU market.

---

### LLM perspective
- View: Makes Apple Silicon Macs more relevant for open-source LLM tinkering, but only for users willing to adopt Tinygrad’s ecosystem.

- Impact: Helps indie AI devs and researchers reuse existing Nvidia/AMD hardware with Macs instead of maintaining separate Linux boxes.

- Watch next: Whether PyTorch/JAX backends appear atop Tinygrad’s driver, and if Apple formalizes broader third‑party GPU driver support.
