# Scammed out of $130K via fake Google call, spoofed Google email and auth sync

- Score: 410 | [HN](https://news.ycombinator.com/item?id=45264726) | Link: https://bewildered.substack.com/p/i-was-scammed-out-of-130000-and-google

- TL;DR
    - A caller posing as “Google Support” and a convincing email “from” legal@google.com led the author to read back a code. The attacker likely already had his Gmail password (leak/malware); the code completed takeover. Because Google Authenticator was cloud‑synced, they accessed Coinbase and drained ~$80k (≈$130k now). The author blames Gmail/iOS UX and Authenticator sync. HN advises distrusting inbound contacts, notes banks still ask for OTPs (training bad habits), and debates spoofed email vs a legitimate Google recovery flow.

- Comment pulse
    - Treat inbound contacts as hostile: never trust caller ID or “official” emails; call back via published numbers — counterpoint: search/SS7 poisoning can fake “official” numbers.
    - Some banks and Google support still ask for SMS/OTP over phone, training users to fail; many users avoid unknown calls or use Do Not Disturb.
    - Dispute on root cause: spoofed @google.com vs legit Google recovery flow; either way, Authenticator cloud sync collapses 2FA once Gmail is compromised.

- LLM perspective
    - View: Phone+email spoofing plus cloud-synced TOTPs turns MFA into single-factor. Prefer hardware keys/passkeys and app-based code storage separated from email.
    - Impact: Google, Coinbase, banks: default to phishing-resistant MFA; show full headers on mobile; add withdrawal holds after device/account changes.
    - Watch next: Publish Google’s response on Authenticator sync defaults; audit recovery flows; measure fraud after hardware-key mandates and Coinbase device-change delays.
