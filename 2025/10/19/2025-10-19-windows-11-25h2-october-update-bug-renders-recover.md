# Windows 11 25H2 October Update Bug Renders Recovery Environment Unusable

- Score: 130 | [HN](https://news.ycombinator.com/item?id=45635287) | Link: https://www.techpowerup.com/342032/windows-11-25h2-october-update-bug-renders-recovery-environment-unusable

- TL;DR
    - The Windows 11 25H2 October update reportedly breaks input in the Windows Recovery Environment, making keyboard/mouse unusable and complicating rollbacks. Commenters also cite installer loops (stalling at 38%), a broken Media Creation Tool near Windows 10’s EOL, and tighter online-account requirements as signs of eroding update quality. Reactions split: pin or disable updates, or switch to Linux; others decry AI/bloat. The common thread: reduced trust in updates—especially alarming when the recovery path itself is impaired.
    - _Content unavailable; summarizing from title/comments._
- Comment pulse
    - Switch to Linux → avoids forced accounts and regressions; KDE Connect and Dolphin praised — counterpoint: many still prefer Windows Explorer’s UX.
    - Disable Windows Update by revoking WaaSMedic/usosvc/wuaueng permissions → stops surprises and rollbacks; reversible — counterpoint: risky; better to pin 23H2 or prioritize stability.
    - Update reliability is poor → installations loop and rollback (e.g., stuck at 38%), wasting 30 minutes per retry without actionable error messages.
- LLM perspective
    - View: Breaking WinRE input undermines the last-resort recovery path; shipping this indicates gaps in release validation.
    - Impact: Home users and IT admins lose safe rollback; BitLocker/firmware passwords complicate alternatives.
    - Watch next: Out-of-band hotfix for WinRE input, installer rollback loops, MCT; clarity on offline installs without mandatory accounts.
