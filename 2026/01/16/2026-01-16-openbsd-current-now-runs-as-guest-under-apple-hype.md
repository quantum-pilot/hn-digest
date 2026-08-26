# OpenBSD-current now runs as guest under Apple Hypervisor

- Score: 392 | [HN](https://news.ycombinator.com/item?id=46642560) | Link: https://www.undeadly.org/cgi?action=article;sid=20260115203619

### TL;DR

Two OpenBSD/arm64 changes make current snapshots usable as guests through Apple’s Virtualization.framework. A viogpu fix maps the framebuffer’s physical address and synchronizes it before host transfers, preventing Apple-hypervisor panics and QEMU black screens when X starts. A virtio-network change negotiates VIRTIO_NET_F_MTU, rejects oversized requests, and aligns the current MTU with the hypervisor. HN welcomed easier graphical OpenBSD VMs on Apple Silicon and broader QEMU compatibility, while clarifying that OpenBSD already worked through QEMU atop Hypervisor.framework. Commenters also asked about setup guides, automated headless use, and unreclaimed VM memory.

### Comment pulse

- The QEMU fix broadens access → arm64 users previously had to disable the framebuffer driver to avoid hangs when starting X.
- Framework names caused confusion → this enables Virtualization.framework; QEMU on older Hypervisor.framework had already supported OpenBSD.
- Graphical guests help experimentation → counterpoint: infrastructure-as-code users prefer serial, unattended VM provisioning.

### LLM perspective

- View: Small virtio compatibility fixes can determine whether an operating system feels accessible or effectively broken on modern hardware.
- Impact: Apple Silicon users gain a smoother path to graphical OpenBSD testing, networking experiments, and isolated development environments.
- Watch next: Test snapshot installation, display stability, MTU edge cases, memory reclamation, and reproducible Virtualization.framework launch instructions.
