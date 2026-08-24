# Malicious skills targeting Claude Code and Moltbot users

- Score: 164 | [HN](https://news.ycombinator.com/item?id=46827731) | Link: https://opensourcemalware.com/blog/clawdbot-skills-ganked-your-crypto

### TL;DR

An updated OpenSourceMalware post reports 28 malicious ClawHub skills published January 27–29 and a second wave of 386 through February 2. Disguised as crypto, finance, social, and utility tools, polished documentation told macOS or Windows users to install a required “AuthTool.” The commands downloaded password-protected executables or decoded shell payloads designed to steal wallets, exchange keys, browser passwords, SSH keys, cloud credentials, and source secrets. The campaign used social engineering, not an exploit; the post does not document confirmed victim losses.

### Comment pulse

- Privilege concentration was the core hazard → commenters compared unsandboxed agents holding crypto credentials to publicly advertising an unlocked vault.
- The lure seemed self-selecting → crude urgency, typos, and extraordinary access requests may filter for victims least likely to question them.
- Permission models split practice → some allowed narrowly approved calendar actions — counterpoint: others would run any agent only inside a VM.

### LLM perspective

- View: This is conventional malware distribution wearing an agent-skill interface; trust and privilege, not model intelligence, create the opening.
- Impact: Registries and users inherit package-ecosystem duties: scanning, provenance, sandboxing, least privilege, revocation, and incident response.
- Watch next: Removal status, registry review controls, confirmed infections, credential rotation, reproducible scanning, and whether duplicate-name flooding continues.
