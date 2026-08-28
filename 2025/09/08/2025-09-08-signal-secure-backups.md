# Signal Secure Backups

- Score: 975 | [HN](https://news.ycombinator.com/item?id=45170515) | Link: https://signal.org/blog/introducing-secure-backups/

### TL;DR

Signal began testing opt-in, end-to-end encrypted daily cloud backups in its Android beta. The free tier retains all text and 45 days of media; a $1.99 monthly plan retains older media to cover storage costs without advertising or data monetization. Archives are separated from payment and account identity through zero-knowledge mechanisms and unlocked only by a device-generated 64-character recovery key that Signal cannot recover. Each daily archive replaces the previous one and excludes view-once content or messages scheduled to disappear within 24 hours.

### Comment pulse

- Users welcomed planned cross-platform restores, particularly after losing histories during Android-to-iOS migrations.
- Others requested test restores, user-chosen storage providers, and assurance that existing local Android backups will remain available.

### LLM perspective

- View: The uncompromising recovery key preserves Signal’s threat model while moving availability responsibility onto users.
- Impact: Managed backups solve device-loss risk, but create new operational dependence on key storage and Signal’s archive service.
- Watch next: Public rollout, iOS and Desktop support, cross-platform fidelity, local destinations, restore testing, and metadata audits.
