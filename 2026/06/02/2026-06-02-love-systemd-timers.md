# Love systemd timers

- Score: 337 | [HN](https://news.ycombinator.com/item?id=48367904) | Link: https://blog.tjll.net/you-dont-love-systemd-timers-enough/

### TL;DR

The author argues scheduled Linux jobs should usually be systemd timer/service pairs rather than literal cron entries. Services provide a controlled environment, journaled output, manual reproducibility, failure and restart hooks; timers add human-readable calendar or event-relative schedules, validation, fleet-wide randomization, suspend wakeups, missed-run catch-up, and a unified status view. HN operators endorsed easier debugging, monitoring, non-overlap, and laptop backup reliability, while cron defenders noted PATH can be explicit, anacron catches missed runs, and @reboot handles startup tasks; one commenter also reported timer bugs involving leap-day schedules and restarts.

### Comment pulse

- Operational clarity → A timer triggers the same service used for manual tests, while journalctl preserves output and existing service monitors can alert on failure.
- Cron parity → Critics said explicit PATH, anacron, @reboot, and documented field headers solve several complaints without adopting systemd’s two-file model.
- Reliability → Persistent timers recovered daily backups after downtime — counterpoint: a report alleged leap-day and restart logic could silently stop schedules.

### LLM perspective

- **View:** The main advantage is lifecycle composition: scheduling delegates execution, logging, isolation, recovery, and alerting to reusable service semantics.
- **Impact:** Administrators trade compact crontabs for more files, but gain testing and richer controls across servers, laptops, and user sessions.
- **Watch next:** Calendar-expression regression tests, distribution defaults, user-target portability, clock-jump behavior, missed-run semantics, overlap policy, and journal retention.
