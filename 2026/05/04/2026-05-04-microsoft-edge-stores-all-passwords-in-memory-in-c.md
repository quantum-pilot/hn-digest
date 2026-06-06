# Microsoft Edge stores all passwords in memory in clear text, even when unused

- Score: 364 | [HN](https://news.ycombinator.com/item?id=48012735) | Link: https://twitter.com/L1v1ng0ffTh3L4N/status/2051308329880719730

### TL;DR
Microsoft Edge reportedly keeps all saved passwords decrypted in RAM, even if they weren’t used in the session. Commenters debate how serious this is: some argue that once an attacker can read browser memory (via admin rights or an exploit), security is already lost anyway. Others emphasize defense‑in‑depth, saying unused passwords shouldn’t sit in memory and pointing to scenarios like unattended machines or cold‑boot attacks. Comparisons with Chrome and password managers highlight differing threat models and expectations for in‑memory protection.  
*Content unavailable; summarizing from title/comments.*

### Comment pulse
- Passwords in clear RAM isn’t risk once attackers have admin or memory‑read exploits; they already own the box — counterpoint: hygiene matters, wipe unused credentials.  
- Physical but brief access matters: an unlocked workstation lets someone dump all stored passwords, unlike managers that re‑lock after inactivity or use master passwords.  
- Some expect Chrome‑style protections or enclaves for in‑memory secrets; others note Google’s blog focuses on disk encryption and question many tools’ real‑world threat models.

### LLM perspective
- View: Edge behavior reflects a common browser trade‑off: convenience and speed versus rigorous memory hygiene and re‑locking of credentials.  
- Impact: Organizations with shared terminals or high insider‑risk should reassess browser password storage, favoring dedicated managers or stricter session‑locking policies.  
- Watch next: Watch for browser vendors adopting in‑memory encryption, time‑bound decryption, or OS‑level services to narrow exposure windows for saved credentials.
