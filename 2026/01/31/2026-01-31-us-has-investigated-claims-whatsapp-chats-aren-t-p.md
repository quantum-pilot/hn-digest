# US has investigated claims WhatsApp chats aren't private

- Score: 140 | [HN](https://news.ycombinator.com/item?id=46838635) | Link: https://www.bloomberg.com/news/articles/2026-01-29/us-has-investigated-claims-that-whatsapp-chats-aren-t-private

### TL;DR

Bloomberg says Commerce agents examined former Accenture moderators’ allegations that they and some Meta staff could access WhatsApp content despite end-to-end encryption. A July 2025 agent report called the inquiry ongoing, but its target, legal theory and status remain unclear; BIS says the assertions are unsubstantiated and it is not investigating export-law violations. Meta says such access is impossible, and the report offers no technical mechanism. WhatsApp does receive up to five recent messages when a user files a report. HN debate separated cryptographic-core assurances from closed-client and metadata risks.

### Comment pulse

- A published audit supported WhatsApp’s cryptographic core but did not review all source code; researchers noted servers still control chat membership and key association.
- Skeptics argued opaque clients can leak plaintext after decryption — counterpoint: an ex-engineer and a cryptographer found the broad allegations technically unconvincing.
- Metadata may reveal relationships, timing and interests without message content, a distinct privacy risk often blurred with claims of plaintext access.

### LLM perspective

- View: An investigated allegation is not technical proof; endpoint behavior, reported-message flows and protocol encryption require separate evaluation.
- Impact: Users face uncertainty about closed-client trust even if protocol encryption remains sound.
- Watch next: Investigation disposition, whistleblower evidence, reproducible client audits, key-verification behavior and findings in the federal lawsuit.
