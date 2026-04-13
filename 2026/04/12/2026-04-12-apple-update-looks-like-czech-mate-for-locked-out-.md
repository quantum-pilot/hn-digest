# Apple update looks like Czech mate for locked-out iPhone user

- Score: 323 | [HN](https://news.ycombinator.com/item?id=47737383) | Link: https://www.theregister.com/2026/04/12/ios_passcode_bug/

### TL;DR
A US student secured his iPhone with an alphanumeric passcode that included the Czech háček (ˇ). After updating from iOS 18 to 26.4, Apple’s lock-screen keyboard stopped allowing that character in passcodes: the key animates and clicks, but no symbol is entered. He’s now permanently locked out of irreplaceable photos, with Apple’s only suggestion being a data-wiping restore. HN sees this as a basic QA and product-responsibility failure, and a reminder to maintain cross-provider backups and downgrade options.

---

### Comment pulse
- This is a bug, not a layout choice → character works elsewhere, only passcode input is broken—counterpoint: if it persists across versions, product decisions are involved.  
- Real lesson: redundant backups, ideally cross-provider → any failure (bug, loss, lockout) can cost everything; big vendors won’t spend on low-value support.  
- Apple broke “userspace” → if a character can be in a passcode, it must always be inputtable; lack of such tests is a deep security design flaw.

---

### LLM perspective
- View: Passcode character sets must be treated as ABI-level contracts; regressions here are security, UX, and trust failures, not mere bugs.  
- Impact: Multilingual users and power users are most exposed; but the reputational hit affects everyone considering strong, non-numeric passcodes.  
- Watch next: Whether Apple adds invariant tests, issues a targeted fix, or documents guaranteed-safe character sets for passcodes across locales.
