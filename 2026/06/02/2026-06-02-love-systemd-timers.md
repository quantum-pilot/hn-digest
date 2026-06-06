# Love systemd timers

- Score: 337 | [HN](https://news.ycombinator.com/item?id=48367904) | Link: https://blog.tjll.net/you-dont-love-systemd-timers-enough/

### TL;DR
The article argues you should replace cron with systemd timers on systemd-based Linux systems. Timers pair a `.timer` with a `.service`, giving clean, predictable environments, centralized logging via journald, easy manual triggering, and powerful scheduling primitives. These include human-readable calendars, relative timers (e.g., “1h after boot, then every hour”), wake-from-suspend, randomization to avoid thundering-herd traffic, and persistence for missed runs. HN comments broadly agree on ergonomics, while debating cron’s capabilities, timer bugs, and personal/organizational inertia around cron.

---

### Comment pulse
- systemd timers → cleaner, consistent environment and one executable unit for manual or scheduled runs; cron’s PATH and differing environments cause surprises — counterpoint: PATH can be set explicitly in crontab.  
- Timer features → persistence, non-overlapping runs, random delays, and journalctl integration improve backups and maintenance; cron needs add-ons like anacron and @reboot to approximate this.  
- Real-world use → people migrate infra jobs and even printer-keepalive scripts to timers; some still prefer cron or fear systemd timer bugs (e.g., Feb 29 edge cases).

---

### LLM perspective
- View: On a systemd host, timers are the pragmatic default; use cron mainly for portability or extremely simple setups.  
- Impact: Ops, SREs, and homelab users gain observability, safer retries, and saner scheduling for backups, updates, and batch jobs.  
- Watch next: Better timer authoring tools, static checking of unit files, and regression tests for calendar edge cases in systemd.
