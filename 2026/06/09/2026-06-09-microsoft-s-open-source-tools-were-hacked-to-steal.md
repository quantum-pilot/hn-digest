# Microsoft's open source tools were hacked to steal passwords of AI developers

- Score: 523 | [HN](https://news.ycombinator.com/item?id=48457830) | Link: https://techcrunch.com/2026/06/08/microsofts-open-source-tools-were-hacked-to-steal-passwords-of-ai-developers/

## TL;DR
Attackers breached dozens of Microsoft-maintained GitHub repositories, inserting credential-stealing malware into open source tools used by AI-focused developers and Azure users. Microsoft disabled about 70 repos, restored some after review, and notified a subset of affected customers; this is its second similar open-source compromise in weeks. HN commenters link it to the broader Miasma supply-chain campaign targeting dev ecosystems, debate TechCrunch’s framing and Microsoft’s culpability, and dig into RBAC, GitHub token practices, and how hard this worm is to eradicate.

## Comment pulse
- AI-assisted “vibe coding” and weak RBAC raise supply-chain risk → experimental tools on personal machines hold powerful creds — counterpoint: others say this predates AI.  
- TechCrunch article seen as sensational and anti–open source → some say Microsoft responded responsibly; others cite repeated breaches as evidence of systemic security failures.  
- Miasma worm campaign spans dev hosts, CI, and multiple package managers → acts like ecosystem-wide malware; mitigation tools exist but full cleanup looks extremely difficult.  

## LLM perspective
- View: Treat AI coding agents as untrusted machines; give them separate identities, least-privilege tokens, and read-only access wherever possible.  
- Impact: Orgs using GitHub, Azure, or AI assistants must treat developer machines as prime targets and invest in supply-chain monitoring.  
- Watch next: Transparent Microsoft postmortem, GitHub tightening token defaults, and playbooks for safely integrating AI coding tools into enterprise CI/CD.
