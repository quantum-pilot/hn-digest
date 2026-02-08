# The RCE that AMD won't fix

- Score: 369 | [HN](https://news.ycombinator.com/item?id=46906947) | Link: https://mrbruh.com/amd/

### TL;DR
An AMD Windows utility apparently fetches driver updates over plain HTTP from legacy ATI domains, allowing any attacker who can hijack DNS or a network path to swap the installer and achieve remote code execution. AMD reportedly declined to fix it. HN discussion stresses that Linux’s in-kernel drivers and signed repos avoid such brittle vendor updaters, argues for blocking outbound HTTP entirely, and predicts enterprises may blacklist AMD’s updater or seek a CVE to force remediation.  
*Content unavailable; summarizing from title/comments.*

### Comment pulse
- Linux bundling drivers avoids vendor updaters → distro maintainers prioritize security; vendors rush hardware releases, shipping fragile privileged tools. — counterpoint: priorities differ, not competence.  
- Blocking outbound HTTP hardens hosts → many vendor updaters, including AMD’s, silently fail without plaintext access, leaking metadata and enabling MITM injection on unsigned payloads.  
- Plain-HTTP updater enables RCE via DNS/Wi-Fi MITM → attackers swap driver installer with malware; enterprises may ban AMD tools and push for a CVE.

### LLM perspective
- View: Vendor-side auto-updaters remain a major supply-chain risk; OS-level package managers with HTTPS and signatures should replace them wherever possible.  
- Impact: Security teams will disable AMD’s updater via group policy or packaging, standardizing on curated drivers to meet corporate threat models.  
- Watch next: Watch whether a CVE is issued, AMD ships a signed-HTTPS updater, or OS vendors begin flagging plain-HTTP updaters as insecure.
