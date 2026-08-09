# Proton meet isn't what they told you it was

- Score: 159 | [HN](https://news.ycombinator.com/item?id=47624558) | Link: https://www.sambent.com/proton-meet-isnt-what-they-told-you/

### TL;DR

Proton Meet’s encryption protects call content, but the article argues its sovereignty marketing obscures a US-controlled metadata path. Proton’s Swiss servers handle MLS key exchange, while LiveKit Cloud routes encrypted media through Oracle and Amazon, sees participant IPs and connection records, and stores telemetry in the United States regardless of pinned region. The author also found a 90-day pre-login cookie and incomplete processor disclosure. HN largely criticized the presentation and stressed threat-model nuance: CLOUD Act exposure for metadata does not mean LiveKit can decrypt end-to-end-encrypted conversations.

### Comment pulse

- Readers called the page repetitive and engagement-driven, arguing its format buried useful findings and that the author should have sought Proton’s response.
- Central relays conceal participants’ IPs from one another but expose connection metadata to LiveKit, a distinct risk from conversation decryption.
- Targeted software updates could theoretically defeat client encryption — counterpoint: privacy is layered, and theoretical compromise does not erase meaningful protections.

### LLM perspective

- **View:** “Nobody can access calls” needs explicit separation between encrypted content, routing metadata, telemetry, and compelled client changes.
- **Impact:** Privacy-sensitive users must decide whether LiveKit’s legal jurisdiction and metadata visibility fit their threat model.
- **Watch next:** Proton’s response, implementation audits, retention periods, regional routing evidence, processor disclosures, and any move to self-hosted SFUs.
