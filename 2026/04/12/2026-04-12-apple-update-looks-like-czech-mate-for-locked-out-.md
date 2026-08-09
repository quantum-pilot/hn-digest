# Apple update looks like Czech mate for locked-out iPhone user

- Score: 323 | [HN](https://news.ycombinator.com/item?id=47737383) | Link: https://www.theregister.com/2026/04/12/ios_passcode_bug/

### TL;DR

After updating an iPhone 13 from iOS 18 to 26.4, a student could no longer enter the háček used in his alphanumeric passcode. The Czech character remains elsewhere, but the lock-screen password field ignores its key, leaving unbacked photos inaccessible; restoration would erase them, while Face ID and wired keyboards cannot operate before the first unlock. The Register reproduced the bug on iOS 26.4.1, and Apple did not respond. Commenters emphasized backups, downgrade options, and permanent fallback input for every character ever accepted in a passcode.

### Comment pulse

- Readers saw a reproducible lock-screen bug, not necessarily an intentional keyboard change, because the visible key animates but enters nothing.
- Backups would prevent data loss — counterpoint: users should never bear blame when a device accepts a password it later cannot input.
- Recovery-mode updates may deliver a future fix without unlocking, but Apple’s restricted pre-unlock state blocks external-keyboard workarounds.

### LLM perspective

- **View:** Authentication input is persistent data infrastructure; accepted characters require permanent compatibility, independent of later interface changes.
- **Impact:** A localization regression can transform strong security into irreversible data loss for users without backups.
- **Watch next:** Apple acknowledgment, a recovery-installable fix, regression tests across locales, fallback input, and safer downgrade paths.
