# Key IOCs for Pegasus and Predator Spyware Removed with iOS 26 Update

- Score: 213 | [HN](https://news.ycombinator.com/item?id=45700946) | Link: https://iverify.io/blog/key-iocs-for-pegasus-and-predator-spyware-cleaned-with-ios-26-update

- TL;DR
    - iVerify reports iOS 26 now overwrites shutdown.log on every reboot, erasing historical entries that once exposed Pegasus/Predator infections—removing a key IOC used by investigators. Prior heuristics (e.g., “cleared shutdown.log implies compromise”) are now invalidated. They advise saving a sysdiagnose before upgrading or delaying until Apple clarifies or fixes. HN debates whether this is a bug or a policy choice, Apple’s privacy posture vs practice, and if wiping logs helps security or just blocks owner visibility.

- Comment pulse
    - Apple undercuts privacy stance → Update erases a vital forensic artifact; looks intentional to some — counterpoint: likely a late bug, not policy-driven.
    - Heuristic broken → Cleared shutdown.log once implied compromise; post-update behavior makes that signal meaningless, reducing confidence in past detection playbooks.
    - Security trade-off → Reducing logs can limit attacker recon, but owners lose inspection; users want deeper visibility, not increasing black-box restrictions.

- LLM perspective
    - View: Forensic dependence on shutdown.log was brittle; pivot to multi-source telemetry, integrity attestations, and user-accessible diagnostics.
    - Impact: Hurts civil-society investigators, incident responders, and EDR apps; benefits stealth malware until Apple clarifies or restores retention.
    - Watch next: Apple advisory or fix, Lockdown Mode telemetry changes, new MDM/APIs for logs, and community-developed iOS triage playbooks.
