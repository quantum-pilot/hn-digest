# AWS Adds support for nested virtualization

- Score: 291 | [HN](https://news.ycombinator.com/item?id=46997133) | Link: https://github.com/aws/aws-sdk-go-v2/commit/3dca5e45d5ad05460b93410087833cbaa624754e

### TL;DR
AWS has quietly enabled nested virtualization for EC2 via a new EC2 SDK/feature, allowing you to run VMs and microVMs (e.g., Firecracker) inside non–bare metal instances. Initial support is limited to 8th‑generation Intel c8i/m8i/r8i families and disables Virtual Secure Mode, with an expected performance hit. Hacker News sees it as long‑overdue parity with GCP/Azure/OCI and a big win for CI, sandboxes, and platform builders, but flags AWS’s high pricing and possible kernel‑level edge cases.

---

### Comment pulse
- AWS finally offering nested virtualization on EC2 → brings parity with GCP/Azure/OCI and avoids buying pricey bare metal just to host inner VMs.  
- Performance/cost tradeoff → users report up to 50% slowdown on complex builds and already‑high AWS prices — counterpoint: many accept this for tooling and operations.  
- Reliability and scope questions → nested VMX is complex; commenters note LKML debates and AWS restricting support to 8th‑gen Intel, disabling VSM to mitigate risk.  

---

### LLM perspective
- View: Makes AWS more attractive as a base for multi-tenant PaaS offerings that prefer microVM isolation over heavyweight containers.  
- Impact: CI providers, security sandboxes, and self-hosted runner systems gain easier scaling without negotiating bare-metal quotas or managing off-cloud hardware.  
- Watch next: benchmarks versus GCP/Azure nested virt, expansion beyond Intel to AMD/Graviton, and AWS services baking in nested microVM support.
