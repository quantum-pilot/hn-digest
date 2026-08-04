# European digital ID wallets rely on safety services of Google and Apple

- Score: 675 | [HN](https://news.ycombinator.com/item?id=48730729) | Link: https://waag.org/en/article/european-digital-id-wallets-are-gift-google-and-apple/

### TL;DR

European digital identity wallets in countries including Italy and the Netherlands use Google Play Integrity, tying access to Google-certified Android builds, Play installation, and accounts; Apple provides a parallel attestation service. The article argues this can exclude GrapheneOS and e/OS users, undermine interoperability and EU sovereignty, and violate the Digital Markets Act despite an open hardware-attestation alternative and Switzerland’s less dependent design. HN widened the objection from vendor lock-in to remote attestation itself, while noting EU rules permit smart cards or hardware tokens rather than mandatory smartphones.

### Comment pulse

- Implementation is fragmented → the EU framework recommends attestation, but states interpret it differently; commenters said Italy’s reference implementation effectively requires Google services.
- Hardware attestation may overreach → critics said replacing Play Integrity preserves state control over acceptable platforms — counterpoint: others support hardware security without restricting software.
- Alternative access must be real → proposed options include free dedicated tokens, smart cards, device public keys, selective-disclosure cryptography, and revocation without smartphone ownership.

### LLM perspective

- **View:** A public credential fails technological neutrality when eligibility depends on a private platform’s certification and distribution policies.
- **Impact:** Exclusion from identity tools can make alternative operating systems impractical, reinforcing incumbents beyond ordinary app-market competition.
- **Watch next:** Audit national wallets for fallback access, data flows, attestation scope, appeal procedures, and compliance with interoperability requirements.
