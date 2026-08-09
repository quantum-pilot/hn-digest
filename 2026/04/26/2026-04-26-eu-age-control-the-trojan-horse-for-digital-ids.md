# EU Age Control: The trojan horse for digital IDs

- Score: 328 | [HN](https://news.ycombinator.com/item?id=47907130) | Link: https://juraj.bednar.io/en/blog-en/2026/04/17/eu-age-control-the-trojan-horse-for-digital-ids/

### TL;DR

The author argues the EU age-verification project offers weaker privacy than its zero-knowledge marketing suggests. The current reference flow uses selectively disclosed, rotating signed credentials rather than active ZK proofs, so unlinkability depends on wallet behavior and breaks if credentials are reused. Hardware attestation may exclude alternative mobile operating systems, while cross-device relay attacks can let an adult proxy authorize a child. Ordinary KYC remains an allowed fallback. HN challenged the “Trojan horse” framing, noting that broader digital identity is explicit policy and that hardware-backed rotation reflects practical security tradeoffs.

### Comment pulse

- Supporters compare proxy use to adults buying restricted goods — counterpoint: critics say online relays could industrialize the bypass.
- Some identify corporate mobile operating systems, not the wallet, as the real lock-in because owners cannot attest self-built software.
- Debate shifted toward governance: revocation is necessary for lost credentials, yet centralized disabling powers could threaten access or citizenship rights.

### LLM perspective

- Evaluate national deployments, not only reference code; server-side attestation and permitted verification paths may differ.
- Publish formal privacy and threat models covering issuer-verifier collusion, replay, relay, device loss, and revocation.
- Measure adoption of privacy-preserving credentials versus passport-scanning vendors after enforcement begins.
