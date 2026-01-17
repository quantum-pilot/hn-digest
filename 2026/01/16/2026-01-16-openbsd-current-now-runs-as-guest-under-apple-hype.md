# OpenBSD-current now runs as guest under Apple Hypervisor

- Score: 392 | [HN](https://news.ycombinator.com/item?id=46642560) | Link: https://www.undeadly.org/cgi?action=article;sid=20260115203619

### TL;DR
OpenBSD-current for arm64 now runs as a guest on Apple’s first‑party Virtualization/Hypervisor stack, thanks to fixes in the virtio GPU and network drivers. The patches correct viogpu framebuffer mapping and add VIRTIO_NET_F_MTU support, preventing panics and black screens under Apple’s hypervisor and fixing X11 hangs in arm64 QEMU since 7.3. This makes OpenBSD far more practical on Apple Silicon laptops for pf labs, small services, and experimentation, though some users still prefer purely headless, automatable VMs.

### Comment pulse
- Apple Silicon devs: OpenBSD guest now useful for pf/mail testing etc., with viogpu graphics instead of serial-only installs — counterpoint: automation folks prefer headless.
- Fix also stops arm64 QEMU VMs hanging when starting X, so stock OpenBSD 7.3+ desktops work again and newcomers can actually try it.
- Thread clarifies this targets Virtualization.framework; OpenBSD already ran via Hypervisor.framework+QEMU, UTM uses that path; some confusion over naming and Tahoe/Apple stack history.

### LLM perspective
- View: Enables a first-class OpenBSD experience on Apple Silicon without third-party hypervisors, closing long-standing virtio MTU and viogpu gaps.
- Impact: Most useful for Mac-based network engineers and security folks wanting reproducible pf labs or lightweight mail/dns appliances on their laptops.
- Watch next: Next steps: better memory ballooning, polished tooling for Virtualization.framework, and performance benchmarks versus Linux/BSD guests on M-series chips.
