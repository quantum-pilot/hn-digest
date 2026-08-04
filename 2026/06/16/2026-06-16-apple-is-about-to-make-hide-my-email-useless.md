# Apple is about to make Hide My Email useless

- Score: 357 | [HN](https://news.ycombinator.com/item?id=48559935) | Link: https://arseniyshestakov.com/2026/06/16/apple-is-about-to-make-hide-my-email-useless/

### TL;DR

Apple says Sign in with Apple and Hide My Email aliases will use @private.icloud.com instead of sharing @icloud.com with mailboxes. The author argues this removes plausible deniability: services can reject every relay address without blocking regular iCloud users, potentially turning a low-friction privacy tool into a disposable-email marker. HN agreed the change simplifies blanket filtering but disputed that it becomes useless: many legitimate businesses may still accept relays, and aliases remain valuable for breach containment, spam shutdown, and identifying who leaked an address. Forced-use services remain the hardest case.

### Comment pulse

- Privacy-friendly rejection is not always avoidable → parking, telecom, and other single-provider services can force registration despite users’ objections.
- Self-hosted aliases trade convenience for control → catch-all domains expose a stable identity and introduce spam, reply, SPF/DMARC, and account-recovery complexity.
- Blockability may not equal rejection → generated aliases were already visually distinctive — counterpoint: the dedicated subdomain makes filtering exact and effortless.

### LLM perspective

- **View:** The change converts a privacy feature’s anonymity set from all iCloud users to an explicitly labeled relay population.
- **Impact:** Users lose anti-blocking cover but retain per-site revocation, leak attribution, and protection of their primary address.
- **Watch next:** Measure rejection rates after rollout, legacy alias continuity, Sign in with Apple failures, and Apple’s response to developers.
