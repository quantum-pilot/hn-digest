# US has investigated claims WhatsApp chats aren't private

- Score: 140 | [HN](https://news.ycombinator.com/item?id=46838635) | Link: https://www.bloomberg.com/news/articles/2026-01-29/us-has-investigated-claims-that-whatsapp-chats-aren-t-private

## TL;DR
US regulators have probed claims that WhatsApp’s end‑to‑end encryption is illusory and that Meta can read messages. Cryptographers and an ex‑WhatsApp engineer in the thread say the Signal‑based protocol is robust and Meta cannot just decrypt stored ciphertext. The real risks are structural: WhatsApp’s servers control group membership and key assignment, the client is closed‑source (so a backdoored build is theoretically possible), and extensive metadata plus app‑level leaks can still expose users’ behavior and social graph.

---

## Comment pulse
- Protocol mostly solid → Independent crypto review finds no obvious way for Meta to read ciphertext; main weakness is server-controlled group membership and public-key mapping — counterpoint: app behavior, side channels, and push notifications can still leak plaintext elsewhere.
- Trust gap in closed-source clients → Even if E2EE is correct, a proprietary client can hide targeted backdoors; reproducible open-source builds make such attacks riskier but not impossible.
- Business and surveillance models → Meta may not need plaintext: WhatsApp Business, metadata, cross‑site tracking and contact graphs already provide huge commercial and investigative value; mass quantum decryption is dismissed as unrealistic.  

---

## LLM perspective
- View: Treat WhatsApp as strong against casual/intermediate adversaries, but not as a defense against a determined platform or state-level attacker.
- Impact: High‑risk users (journalists, activists) should prefer tools with open clients, verifiable keys, and minimal telemetry over convenience-focused messengers.
- Watch next: Independent audits of entire client behavior (not just crypto), publication of key transparency mechanisms, and regulatory scrutiny of metadata and cross‑app tracking.
