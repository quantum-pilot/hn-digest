# Bytecode VMs in surprising places (2024)

- Score: 137 | [HN](https://news.ycombinator.com/item?id=48236122) | Link: https://dubroy.com/blog/bytecode-vms-in-surprising-places/

### TL;DR

Patrick Dubroy surveys bytecode virtual machines embedded far beyond language runtimes: eBPF extends the Linux kernel, DWARF and GDB agents evaluate debugger expressions, RAR archives can run transformation filters, and GPU interpreters trade peak efficiency for flexibility or freedom from shader-compilation stalls. TrueType and PostScript add further examples. HN expanded the catalog with Blender, tensor frameworks, JBIG2 exploits, OpenFirmware FCode, ACPI, Bitcoin Script, and EFI, while stressing the central tradeoff: compact extensibility can elegantly cross hardware boundaries but creates additional interpreters, JITs, and security surfaces.

### Comment pulse

- GPU VMs can be practical → one giant kernel avoids repeated compilation and warp divergence, sometimes outperforming cleaner designs despite no-op work and theoretical inefficiency.
- Portable boot code has long used this pattern → OpenFirmware translated device PROM FCode into native Forth, letting one card image span CPU generations.
- Extensibility magnifies attack surface → every embedded evaluator must constrain untrusted programs correctly — counterpoint: small instruction sets can simplify time, memory, and safety analysis.

### LLM perspective

- **View:** A bytecode VM is often an interface-stability tool: producers emit portable intent while consumers retain control over execution strategy.
- **Impact:** Systems designers gain late binding and sandboxing opportunities, but security teams inherit another parser, verifier, interpreter, and possibly compiler.
- **Watch next:** Verifier guarantees, fuzzing coverage, JIT parity, resource bounds, and performance against ahead-of-time specialization under realistic workloads.
