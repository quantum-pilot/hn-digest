# Anthropic Cowork feature creates 10GB VM bundle on macOS without warning

- Score: 349 | [HN](https://news.ycombinator.com/item?id=47218288) | Link: https://github.com/anthropics/claude-code/issues/22543

### TL;DR
Claude Desktop’s Cowork feature spins up a full Linux VM via Apple’s virtualization framework / Windows HCS, creating a 10–20GB disk image and heavy caches on macOS. Users report severe slowdown, high idle CPU, swap usage, and the VM bundle silently reappearing even after deletion or without knowingly using Cowork. An Anthropic engineer explains the VM is for sandboxing and safety, especially for non-technical users, but HN focuses on the lack of warnings, opt-out controls, and already-fragile macOS disk “System Data” bloat.

---

### Comment pulse
- Hidden local bloat is common → Apple Podcasts, Messages, Time Machine, Docker, etc. can quietly consume 100+GB as “System Data,” forcing painful reinstalls.
- VM sandbox seen as correct architecture → strong isolation for code execution and normals’ safety—counterpoint: the issue is surprise 10–20GB + performance regressions, not sandboxing itself.
- Many devs already prefer isolation → Vagrant, Lima, devcontainers, VPS shells; some want an official Claude VM image to self-host instead of opaque desktop behavior.

---

### LLM perspective
- View: Strong sandboxing is right, but must be paired with explicit consent, sizing info, and a “delete / disable Cowork VM” switch.
- Impact: Disk- and RAM-constrained laptops, plus corporate machines with ZTNA/DNS agents, will be most sensitive to hidden VMs.
- Watch next: Anthropic’s follow-up: VM size caps, lazy provisioning, UI disclosures, and per-folder host mounts vs full-system hooks.
