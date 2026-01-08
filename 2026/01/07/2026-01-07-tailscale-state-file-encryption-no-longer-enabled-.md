# Tailscale state file encryption no longer enabled by default

- Score: 164 | [HN](https://news.ycombinator.com/item?id=46531925) | Link: https://tailscale.com/changelog

### TL;DR
Tailscale 1.92.5 changes its earlier decision to enable TPM-backed node state encryption and hardware attestation by default on Linux and Windows. The mechanisms, added in 1.90, are now opt‑in, and failing to load attestation keys no longer blocks startup; Kubernetes images also stop storing those keys in Secrets so workloads can move nodes more freely. HN commenters dig into why: field experience shows diverse TPM and virtualization setups make default-on encryption brittle, despite its clear security advantages.

### Comment pulse
- Default-on encryption became support nightmare → Tailscale engineer cites unreliable TPMs, BIOS updates, VMs and containers losing keys, leaving nodes bricked and tickets piling up.  
- Some want strict tamper response → say refusing to start on TPM reset thwarts physical attacks — counterpoint: benign resets are common, making systems unusable.  
- Others fear political pressure → ask if weakening at-rest protection aids surveillance; replies stress TPM behavior lies outside Tailscale’s control and feature remains opt-in.

### LLM perspective
- View: Treat TPM-backed encryption as a tiered control, enabled via policy only on hardware you inventory and test.  
- Impact: Small teams lose some default hardening, but gain fewer mysterious outages across laptops, VMs, cloud instances, and Kubernetes.  
- Watch next: better remote attestation APIs, TPM reliability metrics, and admin tooling so encrypted state might become the default again.
