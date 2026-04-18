# Show HN: Smol machines – subsecond coldstart, portable virtual machines

- Score: 200 | [HN](https://news.ycombinator.com/item?id=47808268) | Link: https://github.com/smol-machines/smolvm

## TL;DR

smolvm is a Rust-based CLI for running microVMs with sub-200ms cold start on macOS and Linux, using Hypervisor.framework or KVM plus libkrun. It lets you sandbox untrusted code in hardware-isolated VMs with opt‑in networking and SSH agent forwarding, run persistent dev machines, and “pack” workloads into single-file `.smolmachine` executables that include a Linux userspace and dependencies. The HN thread sees it as a container replacement and backend equivalent of Electron, with interest from AI sandboxing and per‑customer backend use cases, plus questions on live migration, signing, and orchestration.

---

## Comment pulse

- VM-as-container replacement → author aims to remove Docker’s extra layer, marrying Firecracker-like isolation with container ergonomics and subsecond startup for general workloads, including local dev.

- Self-contained binaries as packaging → devs see `smolvm pack` as an easier alternative to GraalVM and akin to Electron-for-backends, simplifying dependency hell for Python/JVM apps.

- Feature and ecosystem questions → users ask about k3s-in-VM, live migration, digital signatures, auto resource sizing, image sources (Ubuntu?), and hot-resize—counterpoint: typical “cloud-native” stacks often ignore these needs.

---

## LLM perspective

- View: MicroVMs with container UX and portable artifacts are a strong fit for AI tool sandboxes, per-customer backends, and “works-everywhere” CLIs.

- Impact: Could erode Docker’s dominance for local dev, secure execution, and packaged tools, especially on macOS and heterogeneous fleets.

- Watch next: Benchmarks vs containers/Firecracker, image registry story, signing/verification, hot-resize and migration support, and how SDK embedding gets used in apps/agents.
