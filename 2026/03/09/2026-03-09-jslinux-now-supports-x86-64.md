# JSLinux Now Supports x86_64

- Score: 219 | [HN](https://news.ycombinator.com/item?id=47311484) | Link: https://bellard.org/jslinux/

### TL;DR
JSLinux, Fabrice Bellard’s in-browser emulator, now runs 64-bit x86 Alpine Linux with AVX-512 and Intel APX, broadening its collection of emulated Linux, RISC-V, Windows 2000 and DOS systems. HN commenters see this as a step toward serious browser-based development and experimentation environments, from safer sandboxes to OS nostalgia trips. Discussion ranges over how to hook such VMs to automation, trade-offs versus other WebAssembly/container approaches, and questions about how open the new x86_64 implementation is.

### Comment pulse
- Browser Linux VMs as agent backends → people prototype LLM coding agents driving shell tools; alternatives cited include container2wasm, browserpod/webvm, v86, Apptron, and devcontainers.
- Windows 2000 UI sparks strong nostalgia → several prefer its clarity to modern UIs—counterpoint: some complain this tangent is irrelevant to the JSLinux technical update.
- Licensing and openness debated → missing x86_64 sources push some to container2wasm or v86; others share TempleOS-on-JSLinux forks and marvel at Bellard’s performance wizardry.

### LLM perspective
- View: In-browser 64-bit x86 with AVX-512/APX makes the web a viable testbed for modern OS, tooling, and agent experiments.
- Impact: Developers, educators, and security researchers gain zero-install sandboxes for demos, training, malware analysis, and reproducible environments directly embedded into documentation or courses.
- Watch next: Benchmarks versus native containers, open-sourcing the x86_64 layer, and integration patterns for LLM coding agents controlling these browser VMs.
