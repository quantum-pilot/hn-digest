# Google broke reCAPTCHA for de-googled Android users

- Score: 471 | [HN](https://news.ycombinator.com/item?id=48067119) | Link: https://reclaimthenet.org/google-broke-recaptcha-for-de-googled-android-users

### TL;DR
- Google’s new reCAPTCHA on Android can require a QR-code challenge that only succeeds if Google Play Services (v25.41.30+) is present, breaking de-Googled ROMs like GrapheneOS. This quietly-enforced shift turns reCAPTCHA into a device/software-attestation step, effectively excluding users who avoid Google’s proprietary stack while iOS users pass normally. HN discussion focuses on how this resembles remote attestation, enables cross-site identity correlation, may conflict with GDPR, and pushes CAPTCHAs toward “soft KYC” for basic web access.

---

### Comment pulse
- New reCAPTCHA ≈ remote attestation, tying device identity via Play Services keys, enabling cross-site tracking and deanonymization; some argue this may breach GDPR data-minimization rules.  
- Privacy-minded users vow to avoid Google hardware attestation entirely, but worry essential banking and fintech apps will force compliance without protective regulation.  
- Developers reconsider reCAPTCHA due to user-hostility, seeking simpler spam controls; reports show archive.is via Cloudflare already blocking de-Googled users with QR-based checks.

---

### LLM perspective
- View: reCAPTCHA is drifting from bot filter to centralized device-attestation layer, effectively turning Google into a gatekeeper for “human” web access.  
- Impact: Biggest friction hits de-Googled ROMs and rooted devices now, but mainstream users may face mandatory attestation on banking, government sites.  
- Watch next: Track whether Cloudflare, major banks, and regulators endorse or restrict such attestation-based CAPTCHAs, and whether open, privacy-preserving alternatives gain adoption.
