# FBI used iPhone notification data to retrieve deleted Signal messages

- Score: 559 | [HN](https://news.ycombinator.com/item?id=47716490) | Link: https://9to5mac.com/2026/04/09/fbi-used-iphone-notification-data-to-retrieve-deleted-signal-messages/

### TL;DR
FBI agents recovered “deleted” Signal messages from an iPhone by pulling them from Apple’s internal notification database. Because Signal’s notification previews were enabled, incoming message contents were stored by iOS—even after the Signal app itself was removed. The case underscores that end‑to‑end encryption doesn’t protect data once it’s surfaced into OS-level notifications or backups, and that defaults and usability (notification previews, disappearing messages, backup behavior) can quietly undermine “secure messenger” promises far more than the crypto itself.

---

### Comment pulse
- Secure app, insecure platform → OS notifications, backups, and complex stacks leak content and metadata, so E2EE alone doesn’t guarantee privacy.  
- Defaults decide security → most users never change settings; secure messengers should ship with the most privacy-preserving notification and backup defaults. — counterpoint: some see this case as user OPSEC failure, not Signal’s.  
- Notifications as evidence → notification databases are queryable (e.g., SQLite on macOS/Android); court cases reveal real-world forensic capabilities more reliably than marketing claims.

---

### LLM perspective
- View: Treat notifications as plaintext copies of messages; design apps assuming OS and cloud notification paths are adversarial.  
- Impact: Messengers, OS vendors, and high‑risk users must harden defaults, especially notification previews and backup encryption policies.  
- Watch next: OS changes to notification token handling, default-on encrypted backups, and secure notification payload standards becoming table stakes for “private” messaging apps.
