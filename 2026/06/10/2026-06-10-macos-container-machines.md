# macOS Container Machines

- Score: 1262 | [HN](https://news.ycombinator.com/item?id=48469658) | Link: https://github.com/apple/container/blob/main/docs/container-machine.md

### TL;DR

Apple’s container machine extends its macOS container tooling into persistent Linux environments built from OCI images. It can run an image’s init system, map the host user and home, support long-lived services, configure CPU and memory, and provide per-distribution setups while sharing repositories with native Mac tools. HN clarified that Apple uses a separate lightweight VM per container, improving isolation and selective data sharing but raising overhead questions. Discussion centered on comparisons with Docker, Colima, Tart, and OrbStack, whose developer highlighted richer integrations and dynamic memory reclamation.

### Comment pulse

- VM-per-container isolation is the trade → stronger security and narrower host mounts — counterpoint: users questioned kernel duplication and memory overhead.
- Positioning remains unclear → developers want explicit guidance against Docker, Colima, Tart, and OrbStack for common macOS workflows.
- Native macOS isolation is still missing → commenters wanted Darwin namespaces or jails rather than another Linux-focused runtime.

### LLM perspective

- **View:** Container machines target environment fidelity and service management, sitting between disposable application containers and full developer VMs.
- **Impact:** Mac developers gain Apple-supported Linux workflows, while tool vendors must differentiate on integration, resource efficiency, and orchestration.
- **Watch next:** Benchmark boot time, idle memory reclamation, filesystem throughput, systemd compatibility, networking, and multi-machine density against established alternatives.
