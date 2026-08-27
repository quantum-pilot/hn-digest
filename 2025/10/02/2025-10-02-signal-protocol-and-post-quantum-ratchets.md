# Signal Protocol and Post-Quantum Ratchets

- Score: 543 | [HN](https://news.ycombinator.com/item?id=45451527) | Link: https://signal.org/blog/spqr/

### TL;DR

Signal is rolling out the Sparse Post Quantum Ratchet, mixing it with the existing Double Ratchet to form a Triple Ratchet. Earlier PQXDH protected session establishment against future quantum decryption; SPQR continually refreshes post-quantum secrets to preserve forward secrecy and recovery after compromise. Because ML-KEM material exceeds 1,000 bytes, the protocol uses erasure-coded chunks spread across ordinary messages, making selective blocking require noticeable denial of service. Signal says deployment is automatic, bandwidth-conscious, formally verified, and designed to leave user experience unchanged.

### Comment pulse

- Readers explained that a post-quantum ratchet protects session healing, not merely initial key agreement.
- Discussion praised the cryptography while revisiting phone-number identity, third-party APIs, and Signal's product priorities.

### LLM perspective

- View: SPQR addresses the less visible quantum problem: preserving recovery after a device compromise over long-lived conversations.
- Impact: Chunking trades modest bandwidth for robustness against loss, reordering, and selectively blocked key updates.
- Watch next: Rollout interoperability, formal-verification coverage, measured overhead, and independent cryptographic review are key.
