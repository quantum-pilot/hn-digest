# Yep, Passkeys Still Have Problems

- Score: 156 | [HN](https://news.ycombinator.com/item?id=46301585) | Link: https://fy.blackhats.net.au/blog/2025-12-17-yep-passkeys-still-have-problems/

### TL;DR

The author uses passkeys but argues their platform implementations still create confusing mental models, persistent vendor friction, fragile cloud-keychain dependence, lockout risk, misleading biometric messaging, and constrained authenticator choice. FIDO Credential Exchange improves provider migration without eliminating day-to-day ecosystem pressure or fragmented credentials. The recommended mitigation is a controllable, backup-capable credential manager; hardware keys plus separately secured password, TOTP, or recovery material for critical accounts; and disaster-recovery planning. Developers should avoid pre-filtering authenticators and obtain consent before enrollment.

### Comment pulse

- Critics say most services can reset lost passkeys, but concede root accounts and credential managers need independent recovery paths.
- Debate focuses on portability, private-key export, platform lock-in, intrusive prompts, and whether alternatives should remain visible.

### LLM perspective

- View: Passkeys improve phishing resistance, but recovery and provider choice remain product-system problems, not cryptographic footnotes.
- Impact: Centralizing credentials without an independent bootstrap path can turn one vendor lockout into many account losses.
- Watch next: Credential Exchange adoption, local backups, authenticator-neutral interfaces, and transparent recovery guarantees for root accounts.
