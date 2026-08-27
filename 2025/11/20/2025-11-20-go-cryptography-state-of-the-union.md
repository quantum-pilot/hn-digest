# Go Cryptography State of the Union

- Score: 116 | [HN](https://news.ycombinator.com/item?id=45994895) | Link: https://words.filippo.io/2025-state/

### TL;DR

Go's cryptography maintainers report hybrid X25519 plus ML-KEM-768 key exchange enabled by default in TLS and available for SSH, while post-quantum signatures remain deferred because of size and protocol trade-offs. A new native-Go FIPS 140-3 module replaces the cgo-based BoringCrypto path without changing normal APIs. The year also brought a clean Trail of Bits primitives audit, faster AES-CTR and RSA, stricter tests, server-side ECH and new standard packages. Planned work includes TLS profiles and possible passkey support.

### Comment pulse

- Readers shared frustration that FIPS can become a security ceiling → exceeding prescribed constructions complicates validation.
- API debate highlighted deliberate trade-offs → slices centralize length checks, while opaque keys and standard entropy sources prevent subtler misuse.

### LLM perspective

- View: The strongest achievement is making safer defaults invisible to ordinary application code.
- Impact: Go users gain post-quantum and compliance paths without maintaining parallel cryptographic stacks.
- Watch next: FIPS validation completion, TLS-profile design, signature migration and proposed secret-memory runtime support.
