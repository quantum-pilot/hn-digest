# Modern email can be built from borrowed parts

- Score: 170 | [HN](https://news.ycombinator.com/item?id=49066639) | Link: https://en.andros.dev/blog/d7ed8b07/modern-email-can-be-built-from-borrowed-parts/

### TL;DR
HMTP is a design experiment that rebuilds “email” entirely over HTTPS using existing standards: WebFinger for user discovery, ActivityPub-style POSTs for delivery, Ed25519 signatures, HPKE content encryption, sigchains for key rotation, and JMAP for reading. Addresses stay `user@domain`, but MX-like delegation uses `.well-known` JSON, messages are signed JSON objects with content-hash IDs, and spam defenses rely on domain-anchored identity, first-contact consent boxes, and optional 402-style postage. HN readers like the composability but question JSON vs MIME, migration paths, and whether protocol changes can overcome email’s economic power structures.

---

### Comment pulse
- History / adoption: Past “ultimate spam fixes” failed; without SMTP compatibility and large-provider support, HMTP risks remaining an elegant but niche experiment.  
- Engineering details: Critics dislike full JSON payloads; propose JSON headers plus MIME bodies to support streaming and reuse mature mail tooling.  
- Product/UX concerns: First-contact inboxes might still bury legitimate requests and create messy endless threads; better workflows and threading models are as important as new protocols.

---

### LLM perspective
- View: Treat HMTP as a reference design and testbed for modern, composable messaging primitives rather than “email replacement.”  
- Impact: Most useful for self-hosters, federated platforms, and client authors experimenting with end‑to‑end encryption and consent-based inboxes.  
- Watch next: Security audits, interop demos with legacy SMTP, and concrete UX studies on spam, onboarding, and conversation management.
