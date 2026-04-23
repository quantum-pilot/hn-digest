# Apple fixes bug that cops used to extract deleted chat messages from iPhones

- Score: 266 | [HN](https://news.ycombinator.com/item?id=47868867) | Link: https://techcrunch.com/2026/04/22/apple-fixes-bug-that-cops-used-to-extract-deleted-chat-messages-from-iphones/

### TL;DR
Apple patched an iOS/iPadOS bug where notification text—such as Signal’s disappearing messages—was cached locally for up to a month, even after messages or apps were deleted. The FBI exploited this by using forensic tools to read “deleted” Signal messages from an iPhone’s notification database. Signal pressed Apple to fix the issue, which is now backported to older iOS 18 versions. HN discussion centers on notification pipelines, OS-level logging, and the limits of app-level end‑to‑end encryption for real privacy.

---

### Comment pulse
- Notification path debate → Some claim Apple/Google see all notification text; others clarify push payloads can be E2EE and only decrypted on-device—counterpoint: OS APIs still see plaintext to render.
- Storage details matter → Fix is logged as a “logging issue” (CVE-2026-28950); speculation over DB vs logs and advice to disable content previews in notifications.
- OS vs app privacy → Forensic digs show iOS caches lots of “detritus”; commenters note privacy often stops at the app boundary once text hits OS render paths.

---

### LLM perspective
- View: Disappearing messages are only as private as the OS, backups, and logs; protocol-level E2EE is necessary but insufficient.
- Impact: High-risk users must revisit notification settings, backup habits, and possibly device choices, not just which chat app they use.
- Watch next: Demand for transparent documentation of notification/storage behavior, Android-side scrutiny, and “truly ephemeral” system-level modes.
