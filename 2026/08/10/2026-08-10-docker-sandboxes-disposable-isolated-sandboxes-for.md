# Docker Sandboxes – Disposable, isolated sandboxes for AI agents

- Score: 623 | [HN](https://news.ycombinator.com/item?id=49239751) | Link: https://www.docker.com/products/docker-sandboxes/

### TL;DR

Docker Sandboxes packages unattended coding agents into disposable microVMs with their own kernels, one environment per session, and the project workspace mounted from the host. Agents can install packages, alter configuration, and run nested Docker without permission prompts; the product supports coding CLIs on macOS, Windows, and Ubuntu without Docker Desktop. Docker says its cross-platform VMM uses native hypervisors rather than containers or Firecracker. HN welcomed the convenience and outbound-network controls, while questioning login friction, secret injection, filesystem performance, live-mounted repository risks, and whether microVM isolation substitutes for granular permissions.

### Comment pulse

- MicroVMs provide separate kernels at lower overhead than traditional VMs — counterpoint: commenters requested concrete startup, memory, and macOS filesystem benchmarks.
- Copy-and-diff workflows reduce malicious repository leftovers; live mounts are easier but can expose future hooks, scripts, or IDE tasks.
- Network allowlists and host-side secret injection matter because filesystem isolation cannot protect credentials an autonomous agent legitimately receives.

### LLM perspective

- **View:** Docker is productizing a security pattern teams otherwise assemble from VMs, proxies, worktrees, and policy scripts.
- **Impact:** Developers can grant agents autonomy with less host risk; administrators still own data, credential, and egress boundaries.
- **Watch next:** Authentication fixes, benchmark data, governance pricing, open-source alternatives, and independent escape testing.
