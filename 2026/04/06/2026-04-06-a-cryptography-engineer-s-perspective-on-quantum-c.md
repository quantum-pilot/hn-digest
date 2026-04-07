# A cryptography engineer's perspective on quantum computing timelines

- Score: 300 | [HN](https://news.ycombinator.com/item?id=47662234) | Link: https://words.filippo.io/crqc-timeline/

### TL;DR
The author, a practicing cryptography engineer, has shifted from “we have time” to “we’re late” on post-quantum cryptography. Two new papers dramatically reduce qubit and gate estimates needed to break 256-bit elliptic curves, tightening credible timelines for cryptographically relevant quantum computers to around 2029. He argues risk management, not certainty, should drive decisions: assume a non-trivial chance of CRQC this decade. That means deploying ML-KEM for key exchange and ML-DSA-44 for authentication now, skipping hybrids, while leaving 128-bit symmetric crypto unchanged.

---

### Comment pulse
- Skeptics reconsider timelines → Clear risk framing (can’t be 99% sure CRQC won’t exist by 2030) convinces some that “RSA is fine” is no longer defensible.  
- Priority debate: key exchange vs. signatures → Some say only session keys are urgent; author and others note timestamps, crypto identities, and tight timelines make signatures urgent too.  
- Hybrid vs. pure PQ → Some see skipping hybrids as reckless given immature PQ; author argues hybrid auth adds complexity and delays migration—counterpoint: hybrids raise attack cost if PQ breaks.

---

### LLM perspective
- View: Treat CRQC as a looming safety deadline; optimize for migration speed and simplicity, not cryptographic elegance.  
- Impact: TLS/SSH stacks, PKI, cryptocurrencies, TEEs, and archival storage systems must plan full PQ rollouts and deprecation timelines now.  
- Watch next: Concrete hardware roadmaps, large-scale ML-KEM/ML-DSA deployments, and any real-world cryptanalysis or side-channel breaks of lattice schemes.
