# You can't trust macOS Privacy and Security settings

- Score: 414 | [HN](https://news.ycombinator.com/item?id=47719602) | Link: https://eclecticlight.co/2026/04/10/why-you-cant-trust-privacy-security/

### TL;DR
On modern macOS, the Privacy & Security “Files & Folders” pane can claim an app is blocked from Documents even while it still has full access. A demo app shows that once you open Documents for it via the file dialog (user “intent”), sandbox limits are silently relaxed using lower-level filesystem metadata, but the UI never updates. Toggling permissions in Settings won’t revoke that access; you must reset TCC from Terminal, which undermines user trust and auditability.

### Comment pulse
- Clarification theme: the bug isn’t “you granted access”; it’s “you removed access in the UI, but the app still reads Documents afterward.”
- Mechanism hunters: focus on `com.apple.macl` xattrs and intent-based grants that outlive UI toggles—counterpoint: some say the pane only revokes generic, not path-specific, permissions.
- Broader debate: TCC prompts feel like Windows UAC and cause permission fatigue, while fully sandboxed apps with temporary extensions behave more consistently.

### LLM perspective
- View: macOS mixes several authorization layers; when they diverge, the user-facing pane stops being a trustworthy source of effective policy.
- Impact: security-conscious users and admins lose reliable visibility into which apps can touch sensitive folders like Documents or Desktop.
- Watch next: Apple documenting MACL behavior, adding revoke controls for intent grants, and verifying TCC state matches filesystem access.
