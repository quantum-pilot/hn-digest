# Kerberoasting

- Score: 141 | [HN](https://news.ycombinator.com/item?id=45196437) | Link: https://blog.cryptographyengineering.com/2025/09/10/kerberoasting/

TL;DR (70–90 words)
“Kerberoasting” abuses AD’s Kerberos: attackers request service tickets (TGS) encrypted under service-account secrets. If admins used human passwords and legacy RC4/NT-hash, tickets are cracked offline at billions guesses/second—around 1000× faster than AES+PBKDF2. This persists because Microsoft still supports RC4 for legacy systems; guidance urges strong/managed passwords and disabling RC4, but defaults and enforcement lag. HN adds protocol corrections (TGS vs TGT), notes AES defaults since 2022, provides detection scripts, and argues gMSA/keytabs, least privilege, and monitoring RC4 requests. Ascension’s 2024 ransomware illustrates impact.

Comment pulse
- Clarifications: Kerberoasting targets TGS, not TGT; Kerberos “salt” is domain+principal; RC4 can be disabled via Group Policy—legacy apps keep it alive.
- Mitigations: prefer gMSA or keytabs, least privilege; disable RC4; monitor RC4 via 4768 events; audit msDS-SupportedEncryptionTypes with PowerShell; PingCastle misses RC4.
- Hashing vs “cracking” stats: 4.18B/s is hash rate; long random service passwords resist offline attacks — counterpoint: rotation windows rarely limit fast cracks.

LLM perspective
- View: Legacy-compatibility defaults expose offline attack surfaces; ban RC4-by-default and require non-password service keys.
- Impact: Enterprises running old apps, hospitals, manufacturing; IAM teams must audit service accounts and migrate to gMSA/keytabs.
- Watch next: Microsoft enforcement timelines, per-account RC4 exemptions, telemetry for RC4 requests, and public metrics on environment RC4 usage.
