# Bytecode VMs in surprising places (2024)

- Score: 137 | [HN](https://news.ycombinator.com/item?id=48236122) | Link: https://dubroy.com/blog/bytecode-vms-in-surprising-places/

## TL;DR
The article catalogs bytecode virtual machines embedded in “non-language” systems: Linux’s eBPF, DWARF and GDB debug evaluators, GDB’s tracing agent VM, WinRAR’s RarVM for compression filters, GPU “ubershaders” that interpret rendering pipelines, and font/page technologies like TrueType and PostScript. These VMs trade complexity for portability, dynamic behavior, and performance in constrained environments. HN adds GPU-rendering and ML examples, firmware/configuration VMs, and even exploit VMs, while debating their power versus the significant security surface they create.

---

## Comment pulse
- GPU VMs can be practical → single ubershaders or shading-graph kernels avoid compilation stalls and warp divergence by keeping threads on one shared opcode stream.  
- Proliferating tiny VMs/JITs hurts security → every format or subsystem adds a Turing-complete attack surface — counterpoint: restricted subsets and formal tooling might reclaim safety.  
- Firmware and configuration stacks rely on VMs → OpenFirmware FCode, ACPI AML, EFI bytecode, Bitcoin Script enable portable drivers and policies instead of fixed logic.  

---

## LLM perspective
- View: Bytecode VMs are now a default abstraction, not an exception, for injecting logic into constrained or heterogeneous environments.  
- Impact: Systems, GPU, and security engineers must treat these “hidden interpreters” as first-class components needing performance tuning, sandboxing, and maintenance.  
- Watch next: Watch for shared intermediate representations, verifier frameworks, and specified safe subsets that multiple subsystems can reuse instead of bespoke VMs.
