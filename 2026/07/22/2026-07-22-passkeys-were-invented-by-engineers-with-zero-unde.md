# Passkeys were invented by engineers with zero understanding of consumer brain

- Score: 438 | [HN](https://news.ycombinator.com/item?id=49007374) | Link: https://twitter.com/nikitabier/status/2079787406300266743

### TL;DR

A viral critique says passkeys improve security while hiding where credentials live or how users should manage them, turning login into unexplained magic. HN’s experienced technologists echoed practical uncertainty about synchronization across devices and browsers, recovery after loss, shared household accounts, hardware keys, and whether sites treat passkeys as replacement, second factor, or optional fallback. Defenders reported nearly frictionless use through Apple, Android, or 1Password and emphasized phishing resistance. The consensus problem was less public-key cryptography than inconsistent vendor interfaces, account policies, and migration controls.

### Comment pulse

- Cross-device ownership is opaque → users cannot tell whether a credential is hardware-bound, cloud-synced, duplicable, exportable, revocable, or portable between managers.
- Integrated ecosystems can feel effortless → biometric prompts replace reused passwords across synced devices — counterpoint: Windows, Firefox, QR, and third-party redirects often break consistency.
- Fallbacks create a security paradox → retaining passwords, email links, SMS, or extra TOTP preserves recovery but can restore phishing paths and erase convenience.

### LLM perspective

- **View:** Passkeys shifted complexity from memorizing secrets to understanding credential custody, but products rarely expose that custody model.
- **Impact:** Consumers gain phishing resistance yet risk ecosystem lock-in; support teams inherit recovery and cross-device failures users cannot self-diagnose.
- **Watch next:** Standardize provider selection, portable exports, household sharing, device-loss recovery, site semantics, and warnings before passwords disappear.
