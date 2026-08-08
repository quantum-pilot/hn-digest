# Microsoft Edge stores all passwords in memory in clear text, even when unused

- Score: 364 | [HN](https://news.ycombinator.com/item?id=48012735) | Link: https://twitter.com/L1v1ng0ffTh3L4N/status/2051308329880719730

### TL;DR

A responsible-disclosure post says Microsoft Edge keeps every saved password in process memory as clear text, including credentials unused in the session and passwords belonging to disconnected users, and that Microsoft described this as intentional. HN commenters disputed the practical severity: an administrator or same-user attacker able to read browser memory can often invoke decryption or export passwords anyway. Others argued that prompt memory wiping still matters as defense in depth, especially for partial memory-read bugs, cold-boot scenarios, unattended machines, and multi-user terminal servers.

### Comment pulse

- Chromium excludes local-administrator compromise from its threat model → such attackers can alter binaries, inspect processes, or impersonate the user.
- Cleartext retention still enlarges exposure → memory-disclosure flaws and brief unattended access may reveal credentials — counterpoint: administrators can already export or decrypt them.
- Chrome’s elevated encryption service may not answer this claim → commenters noted the cited protection appears focused on storage at rest.

### LLM perspective

- **View:** Threat-model exclusion does not make secret minimization pointless; it changes the guarantee from prevention to damage reduction.
- **Impact:** Enterprise administrators should treat unlocked Edge sessions as exposing the full saved-password vault.
- **Watch next:** Microsoft’s technical explanation, reproducible extraction code, cross-Chromium comparisons, and measurements of password lifetime in memory.
