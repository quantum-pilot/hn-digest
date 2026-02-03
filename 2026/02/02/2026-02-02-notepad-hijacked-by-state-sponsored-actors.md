# Notepad++ hijacked by state-sponsored actors

- Score: 857 | [HN](https://news.ycombinator.com/item?id=46851548) | Link: https://notepad-plus-plus.org/news/hijacked-incident-info-update/

- TL;DR  
  Notepad++’s shared hosting provider was compromised from mid‑2025, letting likely Chinese state-sponsored attackers selectively hijack the app’s update checks and serve malicious installers via forged manifests. The app itself wasn’t directly exploited; the weak point was update verification plus provider infrastructure. The project has migrated hosting and strengthened WinGup to verify certificates, signatures, and signed XML, enforced from v8.9.2. HN discussion centers on disabling auto‑updates, using outbound firewalls/package managers, and the project’s prior anti‑CCP political messaging as a possible motive.

- Comment pulse  
  Auto-update is dangerous → Outbound firewalls and blocking app internet access reduce exposure to compromised update channels.  
  Delaying updates can be safer → Older versions missed the malicious campaign; some argue auto-updates create a bigger attack surface than skipped patches — counterpoint: known vulnerabilities also accumulate.  
  Use package managers → Tools like winget/Chocolatey add independent checksum verification and bypass vendor updaters, which spared some users from the hijacked Notepad++ update mechanism.  
  Politics invited targeting → Past Taiwan/Uyghur releases likely angered China, making Notepad++ and specific users attractive targets; some argue politics doesn’t belong in OSS project messaging.

- LLM perspective  
  View: Treat updater infrastructure as critical: signed metadata, certificate pinning, and independent distribution channels should be standard for desktop apps.  
  Impact: Developers relying on shared hosting or DIY updaters must reevaluate trust boundaries and consider third‑party audits and hardened CDNs.  
  Watch next: Publication of IoCs, other projects found in the same campaign, and package managers tightening policies for upstream-hosted binaries.
