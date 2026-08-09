# Show HN: Smol machines – subsecond coldstart, portable virtual machines

- Score: 200 | [HN](https://news.ycombinator.com/item?id=47808268) | Link: https://github.com/smol-machines/smolvm

### TL;DR

SmolVM is an Apache-licensed CLI for running per-workload Linux microVMs with claimed cold starts under 200 milliseconds on macOS and Linux. Using Hypervisor.framework or KVM with libkrun, it provides separate kernels, elastic memory, sleeping idle vCPUs, default-off networking, hostname allowlists, directory mounts, and SSH-agent forwarding. It can create persistent development machines or package a workload and dependencies into one `.smolmachine` artifact for same-architecture hosts. Current limitations include TCP/UDP-only networking, directory-only mounts, signing requirements on macOS, and no cross-architecture portability.

### Comment pulse

- Interest focused on self-contained binaries for JVM, Python, and coding-agent apps without dependency drift.
- Requests included k3s, live migration, artifact signing, hot CPU or memory resizing, and custom images.
- The creator promises container ergonomics with VM isolation — counterpoint: commenters asked how it handles cluster-scale container workloads.

### LLM perspective

- The strongest niche is local untrusted-code sandboxing where hardware isolation and daemonless ergonomics both matter.
- Same-architecture portability remains operational rather than universal; teams still need separate artifacts.
- Security review should cover filesystem, egress, agent forwarding, image provenance, and artifact authentication.
