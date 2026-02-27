# Show HN: Terminal Phone – E2EE Walkie Talkie from the Command Line

- Score: 281 | [HN](https://news.ycombinator.com/item?id=47164270) | Link: https://gitlab.com/here_forawhile/terminalphone

### TL;DR
TerminalPhone is a single Bash script that turns any Linux box or Android+Termux device into an anonymous, end-to-end encrypted walkie-talkie over Tor onion services. Each v3 `.onion` acts as both identity and rendezvous point—no servers, no accounts, no NAT punching. Audio is recorded, Opus-compressed, OpenSSL‑encrypted with a pre-shared secret, then sent as discrete chunks; optional HMAC signs all protocol messages. HN discusses Tor latency (~2–3s), bandwidth ethics, cipher sprawl, and practical ways to trade secrets/addresses.

---

### Comment pulse
- Tor latency and model → ~2–3s delay makes full-duplex unusable; walkie-talkie semantics match real performance and keep 20KB bursts tolerable on Tor.  
- Onion-as-backend trend → Using onion services for IRL comms plus upcoming Arti client could normalize Tor, but enterprise admins often block it as “inherently shady”.  
- Many ciphers exposed → Author surfaces 21 OpenSSL ciphers mostly “because we can”; some like the agility—counterpoint: more options increase complexity and potential misconfiguration.  
- Credential exchange → For serious use, share secrets and onions in person or via existing secure messengers; others suggest offline “broadcast” (codes on paper, signs, etc.).

---

### LLM perspective
- View: Cleverly leverages Tor’s addressing to avoid infrastructure, trading real-time interactivity for simplicity and strong anonymity properties.  
- Impact: Useful niche for activists, journalists, and tinkerers who already use Tor and want voice without phones or centralized services.  
- Watch next: Arti-based rewrite, formal cryptographic review, streamlined Android packaging, and measurement of traffic patterns for fingerprinting resistance.
