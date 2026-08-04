# Mullvad exit IPs are surprisingly identifying

- Score: 559 | [HN](https://news.ycombinator.com/item?id=48143880) | Link: https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/

### TL;DR

Testing 3,650 WireGuard public keys across nine Mullvad servers found only 284 exit-IP combinations, not the trillions naïvely possible. Each key tended to select roughly the same percentile within every server’s IP pool, enabling cross-server correlation until key rotation. The author framed this as a >99% narrowing signal, though commenters challenged that as individual-identification accuracy. Mullvad’s co-founder said some behavior was unintended, the proposed cause was incomplete, and a patch was already under test while the company reassessed privacy-versus-usability trade-offs.

### Comment pulse

- Correlation is meaningful, not identification → narrowing candidates can strongly flag sockpuppets in context, but does not produce >99% certainty by itself.
- Stable exit IPs protect sessions → frequent randomization would break transports, trigger fraud controls, and itself create a fingerprint — counterpoint: keys should rotate.
- Trust remained high → users praised Mullvad’s rapid disclosure and patching, while disputing whether VPNs promise anonymity or only practical privacy.

### LLM perspective

- View: This is a linkage weakness, not automatic deanonymization; its value rises when observers possess contextual or breached logs.
- Impact: Mullvad users switching servers under one key gain less compartmentalization than expected.
- Watch next: Mullvad’s patch details, revised assignment semantics, and independent measurements after deployment.
