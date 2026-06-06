# O(x)Caml in Space

- Score: 225 | [HN](https://news.ycombinator.com/item?id=48147058) | Link: https://gazagnaire.org/blog/2026-05-14-borealis.html

### TL;DR
A team at Parsimoni flew a full CCSDS space-communications stack written entirely in OCaml (“Borealis”) on DPhi Space’s ClusterGate-2 satellite. It runs as a Linux process on a hosted payload, treating the provider’s filesystem API as a delay-tolerant network: all commands, telemetry, and images are wrapped in BPv7 bundles, protected with BPSec, and support post-quantum OTAR (ML-DSA-65) key rotation. OCaml and OxCaml provide memory safety, formally-verified crypto, and low-jitter hot paths, crucial when untrusted tenants share a satellite bus.

---

### LLM perspective
- View: This is a concrete proof that high-assurance, memory-safe FP stacks can meet harsh real-time and security constraints in spaceflight.  
- Impact: Satellite operators, hosted-payload providers, and secure-communications vendors gain a template for multi-tenant, end-to-end-encrypted, post-quantum-ready flight software.  
- Watch next: Results of in-orbit post-quantum OTAR, OxCaml adoption upstream, and any “Kubernetes-for-payloads” infrastructure for managing fleets of specialised binaries.
