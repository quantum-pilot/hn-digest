# RFC 9849. TLS Encrypted Client Hello

- Score: 270 | [HN](https://news.ycombinator.com/item?id=47244291) | Link: https://www.rfc-editor.org/rfc/rfc9849.html

- TL;DR  
    - TLS Encrypted Client Hello (ECH), standardized as RFC 9849, encrypts the TLS ClientHello using HPKE so on-path observers can’t see SNI, ALPN, or other sensitive extensions. Clients send a public “outer” ClientHello plus an encrypted “inner” one; padding, GREASE, and anonymity sets aim to prevent fingerprinting and ossification while preserving TLS 1.3 security. HN discussion focuses on censorship circumvention, emerging server/client support, DNS operational complexity, and side-effects for bot detection and parental or legal content controls.

- Comment pulse  
    - ECH as censorship bypass → Encrypting SNI helped evade ISP blocks (e.g., Jio); public_name tricks middleboxes—counterpoint: also undermines parental filters, fueling age-verification laws.  
    - Deployment and tooling → Caddy, nginx, Go/Rust stacks, and Android apps already ship ECH; DNS SVCB/HTTPS bootstrapping exists but heterogeneous DNS APIs complicate automation.  
    - Fingerprinting and bots → ECH hides ClientHello from outsiders, weakening JA3/JA4‑style bot signals; origins like Cloudflare still see and fingerprint decrypted inner handshakes.

- LLM perspective  
    - View: ECH plus encrypted DNS shifts confidentiality from network operators toward DNS/CDN providers, consolidating trust but measurably improving user privacy.  
    - Impact: Smaller sites gain censorship resistance via shared ECH frontends; enterprise firewalls and schools lose hostname filtering, need on-device agents.  
    - Watch next: Browser default-on status, major CDNs’ rollout patterns, standardized padding profiles, and regulatory responses around access and content-restriction mandates.
