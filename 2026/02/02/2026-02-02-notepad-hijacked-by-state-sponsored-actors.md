# Notepad++ hijacked by state-sponsored actors

- Score: 857 | [HN](https://news.ycombinator.com/item?id=46851548) | Link: https://notepad-plus-plus.org/news/hijacked-incident-info-update/

### TL;DR

Notepad++ says attackers compromised its former shared host and selectively redirected update requests to malicious manifests from June through late 2025. The provider reports server access ended September 2 but stolen internal credentials remained usable until December 2; another analysis dates the attack’s end to November 10. Researchers assess a likely Chinese state-sponsored actor, though the project initially had no concrete indicators. Notepad++ moved hosts, strengthened installer certificate and signature checks, signed update XML, and recommends manually installing version 8.9.1.

### Comment pulse

- Users wanted clearer victim guidance and a verification tool, since malicious updates may have dropped files beyond the editor installation.
- Package-manager users favored pinned checksums and separate distribution paths; others argued self-updaters legitimately need network access.
- Debate split between delaying updates to avoid supply-chain attacks and updating promptly to close known vulnerabilities.

### LLM perspective

- View: Authenticating downloaded installers is insufficient if the server’s manifest can redirect clients without its own verified signature.
- Impact: Selectively targeted users may remain unidentified because the project initially lacked hashes, domains or IP indicators.
- Watch next: Version 8.9.2 enforcement, published compromise indicators and concrete remediation steps for potentially affected machines.
