# PCs refuse to shut down after Microsoft patch

- Score: 222 | [HN](https://news.ycombinator.com/item?id=46656998) | Link: https://www.theregister.com/2026/01/16/patch_tuesday_secure_launch_bug_no_shutdown/

### TL;DR

Microsoft says January security updates can leave some Windows 11 23H2 systems with Secure Launch unable to shut down, restart, or hibernate, risking battery drain. The temporary workaround is the command-line `shutdown /s /t 0`; affected users should save work while awaiting an unspecified future fix. A separate update issue can freeze classic Outlook POP profiles. HN commenters mocked Windows requiring a terminal, criticized Microsoft’s QA priorities and Copilot focus, and debated whether Windows’ declining revenue share explains neglect; others defended CLI efficiency and shutdown’s complexity.

### Comment pulse

- Patch reliability appears to be worsening → readers blamed reduced QA and incentives to prioritize AI, though claims about staffing were unverified.
- Command-line workaround reverses Windows’ usability pitch → counterpoint: several users find CLI fixes faster, safer, and valuable on every operating system.
- Windows remains strategically important despite a smaller revenue share → commenters disputed whether its multibillion-dollar business could be neglected.

### LLM perspective

- View: A security update that breaks power-state transitions exposes the operational cost of insufficient regression coverage.
- Impact: Mobile users and administrators face battery loss, forced procedures, and another reason to delay otherwise necessary patches.
- Watch next: Microsoft’s affected-device count, root-cause detail, emergency fix timing, and confirmation that Outlook’s separate regression is resolved.
