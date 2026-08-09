# Cloudflare targets 2029 for full post-quantum security

- Score: 258 | [HN](https://news.ycombinator.com/item?id=47675625) | Link: https://blog.cloudflare.com/post-quantum-roadmap/

### TL;DR

Cloudflare is targeting 2029 for post-quantum protection across both encryption and authentication. It says more than 65% of human traffic already uses hybrid post-quantum encryption, reducing “harvest now, decrypt later” exposure; the harder phase is replacing long-lived authentication, signing, and root keys whose forgery could be catastrophic. Cloudflare cites faster quantum algorithms and accelerating hardware and error-correction work, though no cryptographically relevant quantum computer exists. Migration requires disabling classical fallbacks, rotating exposed secrets, and coordinating browsers, applications, origins, and third parties.

### Comment pulse

- Cloudflare can phase changes at its proxy boundary, much like HTTPS — counterpoint: firmware, stored data, and decentralized systems are harder.
- Browser enforcement could accelerate adoption but strand old devices and software.
- Readers want practical scanners and configuration profiles to verify end-to-end post-quantum support.

### LLM perspective

- **View:** A 2029 deadline is prudent risk management, not evidence that current public-key crypto has been broken.
- **Impact:** Platform operators can abstract migration, but long-lived hardware and unmanaged dependencies remain exposed.
- **Watch next:** Published quantum details, browser defaults, downgrade-resistant standards, and inventories of classical-only signing keys.
