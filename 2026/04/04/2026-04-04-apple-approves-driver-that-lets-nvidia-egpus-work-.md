# Apple approves driver that lets Nvidia eGPUs work with Arm Macs

- Score: 334 | [HN](https://news.ycombinator.com/item?id=47640380) | Link: https://www.theverge.com/tech/907003/apple-approves-driver-that-lets-nvidia-egpus-work-with-arm-macs

### TL;DR

Tiny Corp says Apple will sign its third-party AMD and Nvidia eGPU driver for Arm Macs, removing the previous need to disable System Integrity Protection. This is not an Nvidia release or plug-and-play restoration of Mac GPU support: users compile components through Docker, and the path is aimed at tinygrad-based LLM workloads. Commenters stressed that CUDA, Vulkan, and PyTorch support do not follow, while Thunderbolt bandwidth, macOS update breakage, and missing native integration limit practicality. Others see hardware access as the prerequisite for broader tooling.

### Comment pulse

- A secondhand PC remains simpler for most Nvidia workloads → an eGPU may still serve specialized Mac-centered development.
- The driver appears tinygrad-specific → general graphics and established CUDA applications remain outside the supplied claim.
- Apple signing removes a security compromise → it does not guarantee future compatibility or performance.

### LLM perspective

- **View:** This is a narrow platform-enablement win, valuable as infrastructure but easy to mistake for complete Nvidia support.
- **Impact:** Arm Mac researchers can experiment with external accelerators without disabling SIP, albeit inside a constrained software stack.
- **Watch next:** Supported GPUs, benchmarked Thunderbolt losses, installation reproducibility, PyTorch interoperability, and survival across macOS updates.
