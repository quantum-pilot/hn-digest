# Apple fixes bug that cops used to extract deleted chat messages from iPhones

- Score: 266 | [HN](https://news.ycombinator.com/item?id=47868867) | Link: https://techcrunch.com/2026/04/22/apple-fixes-bug-that-cops-used-to-extract-deleted-chat-messages-from-iphones/

### TL;DR

Apple patched an iOS and iPadOS bug that retained notifications marked for deletion, sometimes for up to a month. Because notification previews contained message text, forensic tools could recover Signal messages after they disappeared in the app or the app was removed; the FBI reportedly used this in an investigation. Apple backported the fix to iOS 18, describing improved data redaction. The incident did not break Signal’s end-to-end encryption: plaintext leaked after reaching the device’s OS notification layer. Readers recommended hiding preview content and sought clarity about remaining notification history.

### Comment pulse

- Disagreement centered on storage semantics: a notification database, auxiliary log, or delayed cleanup could produce different residual-risk conclusions.
- Push transport was often conflated with local display — counterpoint: apps can send encrypted metadata, then fetch and render plaintext on-device.
- Long-lived iOS caches and “system storage” led forensic users to suspect broader cleanup inconsistencies beyond this CVE.

### LLM perspective

- Apple should document precisely which events mark notifications deleted and which stores the patch purges.
- Messaging apps should default sensitive conversations to sender-only or generic previews, with an explicit privacy warning.
- Independent tests should measure recoverability after dismissal, expiration, app deletion, reboot, backup, and OS upgrade.
