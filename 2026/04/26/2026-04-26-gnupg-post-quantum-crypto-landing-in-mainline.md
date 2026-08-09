# GnuPG – post-quantum crypto landing in mainline

- Score: 160 | [HN](https://news.ycombinator.com/item?id=47907018) | Link: https://lists.gnupg.org/pipermail/gnupg-announce/2026q2/000504.html

### TL;DR

GnuPG 2.5.19 advances the 2.5 series toward post-quantum OpenPGP encryption through Kyber, standardized as ML-KEM/FIPS 203, alongside improved 64-bit Windows support. The release remains compatible with older versions and arrives two months before the 2.4 branch reaches end-of-life. It also adds OCB and session-hash options while fixing certificate, SSH signature-padding, key-refresh, and RSA-key validation issues. HN discussion framed the work as a compatibility migration whose urgency depends on how long protected data must remain secret.

### Comment pulse

- Confidentiality lifetime matters more than quantum-computer forecasts: five-year messages face harvest-now-decrypt-later risk; ninety-day backups may not.
- Hybrid ML-KEM plus X25519 offers fallback against either algorithm failing — counterpoint: post-quantum sizes and performance still impose costs.
- SHA-1 fingerprint complaints resurfaced, though replies said proposed standards use SHA-256 and practical fingerprint collisions differ from generic SHA-1 attacks.

### LLM perspective

- Inventory encrypted data by confidentiality horizon and identify recipients unable to process composite keys.
- Benchmark key generation, decryption, message size, and smartcard workflows before organization-wide defaults change.
- Watch distribution packaging, 2.6 stabilization, and hardware-token roadmaps rather than assuming library support completes migration.
