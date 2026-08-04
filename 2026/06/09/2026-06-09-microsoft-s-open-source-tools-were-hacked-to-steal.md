# Microsoft's open source tools were hacked to steal passwords of AI developers

- Score: 523 | [HN](https://news.ycombinator.com/item?id=48457830) | Link: https://techcrunch.com/2026/06/08/microsofts-open-source-tools-were-hacked-to-steal-passwords-of-ai-developers/

### TL;DR

Microsoft disabled at least 70 GitHub repositories after attackers injected credential-stealing malware into open-source Azure and developer tools. Opening compromised content through AI coding tools or VS Code could expose passwords and other credentials; Microsoft notified a small number of customers who may have downloaded it, but total exposure remains unknown. This followed May’s Durable Task breach and may be a re-compromise. HN disputed TechCrunch’s framing, stressing that this is a longstanding supply-chain problem whose blast radius grows when developer machines and AI agents hold broad repository and cloud permissions.

### Comment pulse

- Cause versus amplifier → Commenters said dependency compromise predates AI — counterpoint: agent experimentation increases project overlap, local installs, and privileged credentials available to steal.
- Access design → AI agents should be separate security principals with repository-specific, fine-grained tokens; reusing human credentials turns compromise into organization-wide lateral movement.
- Response debate → Some praised Microsoft for disabling repositories quickly, while others viewed a second breach within weeks as evidence containment or workflow security failed.

### LLM perspective

- **View:** Repository trust must be continuous and artifact-specific; organizational ownership alone cannot establish code integrity after publication.
- **Impact:** Developers, CI runners, and agents can transform one poisoned dependency into credential theft across source control and clouds.
- **Watch next:** Require signed releases, pinned hashes, ephemeral credentials, isolated execution, repository audits, and verified eradication before restoration.
