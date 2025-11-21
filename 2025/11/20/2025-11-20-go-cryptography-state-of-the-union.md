# Go Cryptography State of the Union

- Score: 116 | [HN](https://news.ycombinator.com/item?id=45994895) | Link: https://words.filippo.io/2025-state/

### TL;DR
- Go’s crypto team reports another year with no serious vulnerabilities and a clean Trail of Bits audit for core primitives and assembly.  
- Post‑quantum ML‑KEM is now in the standard library and enabled by default via hybrid X25519+ML‑KEM in TLS and SSH, mostly “just working” after you upgrade.  
- A new pure‑Go, FIPS 140‑3 validated module replaces the BoringCrypto+cgo path, while preserving APIs and security (hedged ECDSA, stronger RNG) and speeding AES, RSA, SHA‑3, and keygen.  
- Heavy investment in testing (assembly mutation, accumulated vectors, external suites) and upcoming work on TLS profiles and passkey support aim to keep secure defaults easy.  

---

### Comment pulse
- FIPS 140 is too conservative and slow → NIST’s process turns a minimum standard into a de‑facto ceiling, discouraging stronger-than-required designs.  
- Crypto API design debate → Go’s use of `[]byte` and error‑returning constructors is intentional to avoid panics, silent truncation, and misuse of “deterministic” randomness.  
- GC and secrets worry people → mitigations today include `mlockall`, explicit zeroing, and proposals like `runtime/secret`; consensus: local compromise beats language guarantees anyway.  

---

### LLM perspective
- View: Go is converging on “secure by default” crypto, hiding complexity while still offering sharp tools for experts and auditors.  
- Impact: Cloud, infra, and tooling vendors gain simpler FIPS compliance and PQ‑ready stacks without bespoke forks or cgo-heavy builds.  
- Watch next: TLS profile APIs, runtime/secret progress, and broader PQ signature deployment will show how far defaults can be safely opinionated.
