# Yep, Passkeys Still Have Problems

- Score: 156 | [HN](https://news.ycombinator.com/item?id=46301585) | Link: https://fy.blackhats.net.au/blog/2025-12-17-yep-passkeys-still-have-problems/

### TL;DR
The post argues that, in late 2025, passkeys still suffer from usability, portability, and power-imbalance problems. Platform keychains (Apple, Google, Microsoft) nudge users into opaque, cloud-tied ecosystems, making alternative authenticators and credential managers harder to use and sometimes impossible to back up. Silent data loss, account lockouts, and confusing biometric messaging erode trust. The author recommends: treat passkeys as one tool among many, prioritize a credential manager you control, and use hardware keys and backups for critical accounts like email.

---

### Comment pulse
- Losing a passkey ≈ losing a password → recovery is usually via email/SMS; the real danger is opaque recovery on “root” accounts like Apple/Google.  
- Vendor lock‑in stems from non‑exportable keys and UX nudges toward platform stores; phishing resistance is bought by forbidding plaintext access—counterpoint: encrypted backups still allow controlled export.  
- Many users prefer password+TOTP due to forced MFA prompts, surprise passkey enrollment, and poor stories for inheritance and disaster recovery, despite weaker phishing resistance.

---

### LLM perspective
- View: Passkeys fix phishing but shift risk to ecosystem dependence, UX dark patterns, and brittle recovery—a socio-technical problem, not just a cryptographic one.  
- Impact: Non‑experts gain safer defaults; power users and institutions inherit new failure modes around lockout, portability, and account succession.  
- Watch next: Standardized recovery/estate flows, vendor-agnostic key portability, and OS/browser UI that treats “which authenticator?” as a first-class, memorable user choice.
