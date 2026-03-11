# Intel Demos Chip to Compute with Encrypted Data

- Score: 214 | [HN](https://news.ycombinator.com/item?id=47322815) | Link: https://spectrum.ieee.org/fhe-intel

### TL;DR
Intel’s Heracles is a prototype accelerator for fully homomorphic encryption (FHE), letting servers compute on data that never gets decrypted. Built on 3 nm FinFET with 64 specialized cores and 48 GB of high‑bandwidth memory, it speeds key FHE operations by 1,000–5,500× versus Xeon CPUs, shrinking some workloads from days to minutes. But FHE still runs roughly 20–100× slower than plaintext, so near‑term uses are niche: private queries, e‑government, regulated analytics, and small encrypted ML models.

---

### Comment pulse
- Fear of DRM/attestation abuse → some see this as another step in “war on general‑purpose computing” and user tracking.— counterpoint: FHE needs decryption keys, so it’s ill‑suited to DRM.
- Performance perspective → current FHE is 10,000–100,000× slower than plaintext; Heracles may cut this to ~20–100×, enabling batch analytics but not latency‑sensitive apps.
- Deployment and politics → skepticism it will reach consumer chips; concerns about export controls or hidden backdoors, and that it protects against snooping hosts, not malicious code.

---

### LLM perspective
- View: Dedicated FHE silicon makes “encrypted inference” and private search realistic for narrow, high‑value workloads, not as a universal privacy silver bullet.
- Impact: Cloud providers, healthcare, finance, and e‑government can offer stronger guarantees against insider access, competing with TEEs and data‑minimization schemes.
- Watch next: End‑to‑end benchmarks on real ML models, energy costs vs GPUs/CPUs, and whether regulators treat FHE as a compliance enabler or a surveillance obstacle.
