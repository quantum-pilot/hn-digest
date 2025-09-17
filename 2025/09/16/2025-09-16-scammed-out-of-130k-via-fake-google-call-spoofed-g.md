# Scammed out of $130K via fake Google call, spoofed Google email and auth sync

- Score: 259 | [HN](https://news.ycombinator.com/item?id=45264726) | Link: https://bewildered.substack.com/p/i-was-scammed-out-of-130000-and-google

TL;DR
Victim lost $130K after a convincing “Google Support” call. Attacker likely initiated Google’s official account-recovery, prompting a real email with a code; the victim read it aloud, enabling takeover of Gmail/Drive. Because Google Authenticator was cloud-synced, 2FA codes became accessible, letting the attacker reset Coinbase and withdraw funds. HN advises: never share codes; hang up and reinitiate via official channels; caller ID/email can be spoofed and search results poisoned. Many criticize OTP-by-phone practices and recommend isolating finance email and disabling sync.
Content unavailable; summarizing from title/comments.

Comment pulse
- Verify by calling a number you find on the company’s site; caller ID and emails are spoofable—counterpoint: SS7 and poisoned search results can still mislead.
- Never read one-time codes to callers; instead, hang up and initiate support yourself. Some banks still ask for OTPs, training users to ignore this.
- Phone hygiene: let unknowns go to voicemail; use callback-only; watch for 1–2s dialer delay as a red flag; lock unknown callers on parents’ phones.

LLM perspective
- View: Account-recovery social engineering plus Authenticator sync created a single point of failure; phone/email spoofing amplified trust.
- Impact: High risk for users tying finances to Gmail; companies must stop OTP-by-phone verification; platforms should default to stronger isolation.
- Watch next: E2EE for Authenticator backups, clearer recovery UX, hardware key adoption, Coinbase withdrawal delays/allowlists, better search ads policing for fake support.
