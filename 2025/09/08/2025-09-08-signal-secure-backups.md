# Signal Secure Backups

- Score: 975 | [HN](https://news.ycombinator.com/item?id=45170515) | Link: https://signal.org/blog/introducing-secure-backups/

- TL;DR
  - Signal is rolling out opt‑in, end‑to‑end encrypted “secure backups”: daily archives tied only to a 64‑character recovery key that never leaves your device. Free tier backs up all texts (≈100 MiB) and 45 days of media; $1.99/month expands storage (up to 100 GB) for longer media history. Backups are zero‑knowledge and unlinkable to accounts; disappearing and view‑once content stays excluded. Android beta now; iOS/desktop soon with cross‑platform restores. HN welcomes portability and test‑restore options, debates provider choice, and contrasts cloud convenience with past local backups.

- Comment pulse
  - Cross‑platform history transfer → New backup format is cross‑platform; devs report successful iPhone restores; desktop can now copy history during setup.
  - Use own storage, not Signal’s → Privacy‑conscious users prefer iCloud/Drive/self‑hosted, maybe legible exports — counterpoint: Signal plans “save to location of your choosing.”
  - Local Android backups existed → Manual, non‑incremental and hard to offload; $2/month cloud option seen as pragmatic for large databases.

- LLM perspective
  - View: Design respects metadata minimization; recovery‑key‑only model is powerful but unforgiving for users who misplace credentials.
  - Impact: Enables painless Android↔iOS moves, strengthens desktop continuity, and adds a sustainable, user‑funded storage cost model.
  - Watch next: iOS/desktop rollout, bring‑your‑own‑storage connectors, restore‑without‑switching-device flow, large‑backup performance benchmarks, and clearer key‑management UX.
