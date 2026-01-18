# PCs refuse to shut down after Microsoft patch

- Score: 222 | [HN](https://news.ycombinator.com/item?id=46656998) | Link: https://www.theregister.com/2026/01/16/patch_tuesday_secure_launch_bug_no_shutdown/

- TL;DR  
  - January’s Patch Tuesday broke power management on some Windows 11 23H2 PCs with Secure Launch enabled: shutdown, restart and hibernate appear to work but the machine keeps running, draining batteries. Microsoft’s current workaround is a command-line `shutdown /s /t 0`, with no detailed root cause or fix timeline, and a separate update is also freezing some classic Outlook POP profiles. Hacker News discussion centers on Windows’ declining quality, gutted QA, rising ads/AI focus, and reliance on CLI-style fixes.

- Comment pulse  
  - Windows feels increasingly “Linux-like” in fragility → GUI features break, users are told to paste CLI commands instead of using reliable controls.  
  - Microsoft under-invests in Windows quality → ads, Copilot and outsourced QA dominate focus, causing regressions. — counterpoint: Windows still earns ~$28B and underpins Microsoft’s ecosystem.  
  - Bug highlights loss of user control → people fear unkillable systems; others note hard power-off always works and shutdown logic is complex.

- LLM perspective  
  - View: Security features like Secure Launch add complexity; without strong regression suites, even basic operations like power management become fragile.  
  - Impact: Admins must choose between delaying patches or scripting workarounds, increasing support costs and eroding trust in Windows updates.  
  - Watch next: Whether Copilot’s weak adoption plus patch failures force Microsoft to redirect AI budget back into Windows quality.
