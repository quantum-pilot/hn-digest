# Modern email can be built from borrowed parts

- Score: 170 | [HN](https://news.ycombinator.com/item?id=49066639) | Link: https://en.andros.dev/blog/d7ed8b07/modern-email-can-be-built-from-borrowed-parts/

### TL;DR

The proposal sketches HMTP, an HTTP-only mail system retaining `user@domain` addresses while assembling WebFinger discovery, ActivityPub-style delivery, Ed25519 signatures, HPKE encryption, JMAP synchronization, sigchain key rotation, and content-addressed attachments. Sender servers queue retries; content hashes make delivery idempotent; unknown senders enter request boxes, with optional postage. A single-file Python prototype implements the transport subset, but is explicitly unaudited. HN readers found the components plausible yet questioned adoption without SMTP compatibility, spam handling, JSON scalability, and decades of accumulated edge cases.

### Comment pulse

- Backward compatibility may decide adoption → commenters favored dual-protocol gateways or incremental SMTP upgrades because virtually everyone already has an email address.
- Protocol assembly does not erase operational history → reputation systems, provider gatekeeping, identity recovery, and obscure workflows remain harder than basic delivery.
- First-contact consent appealed as inbox protection → some wanted it by default — counterpoint: request folders may merely become another spam graveyard.

### LLM perspective

- **View:** Recombining mature standards reduces invention risk, but integration boundaries create a new protocol’s most consequential failure modes.
- **Impact:** Independent providers gain modern cryptography; users face a separate network until gateways or dominant adopters emerge.
- **Watch next:** Define migration gateways, threat models, streaming formats, abuse economics, key-recovery procedures, interoperability tests, and independent cryptographic review.
