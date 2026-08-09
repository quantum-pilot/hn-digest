# You can't trust macOS Privacy and Security settings

- Score: 414 | [HN](https://news.ycombinator.com/item?id=47719602) | Link: https://eclecticlight.co/2026/04/10/why-you-cant-trust-privacy-security/

### TL;DR

A test app demonstrates that macOS Files & Folders controls can misreport effective access. After direct Documents permission is granted and then disabled, selecting Documents through an Open panel creates a user-intent exception; the app can list and read the folder while Settings still shows access off. The grant is folder-specific and appears tied to a `com.apple.macl` extended attribute beneath TCC’s visible controls. Resetting TCC may not remove that attribute, leaving no reliable GUI revocation path. Exploitation requires folder selection, but the persistence breaks the panel’s promise.

### Comment pulse

- Readers initially confused explicit selection with broad permission. — counterpoint: later UI revocation neither removes nor reveals the persistent exception.
- App Sandbox and TCC are distinct; properly sandboxed apps reportedly receive narrower, temporary picker extensions unless they store security-scoped bookmarks.
- Permission prompts may reduce carte-blanche access, but hidden grants and Terminal-or-recovery cleanup turn protective friction into misleading security theater.

### LLM perspective

- **View:** A privacy dashboard must describe effective authority, not merely one policy database, or users cannot make informed decisions.
- **Impact:** Mac users and administrators may falsely believe sensitive folders are protected after toggling access off.
- **Watch next:** Apple’s bug response, MACL documentation, reproducibility across versions, a GUI revocation mechanism, and tests involving sandboxed apps.
