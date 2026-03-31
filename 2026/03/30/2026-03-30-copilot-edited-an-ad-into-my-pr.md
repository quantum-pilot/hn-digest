# Copilot edited an ad into my PR

- Score: 1437 | [HN](https://news.ycombinator.com/item?id=47570269) | Link: https://notes.zachmanson.com/copilot-edited-an-ad-into-my-pr/

### TL;DR
A developer discovered that GitHub Copilot silently edited their human-written pull request description to append promotional copy for Copilot and Raycast, echoing fears of “enshittification” where platforms progressively abuse users. HN commenters show this wasn’t an isolated incident but a widespread “tips” system Microsoft embedded in Copilot-generated PRs. After backlash, a Copilot team member said these tips are now disabled for PRs created or touched by Copilot, but trust, security, and data-usage concerns remain high.

---

### Comment pulse
- Copilot “tips” are effectively ads → they’ve appeared in ~1.5M PRs since launch; Raycast says it didn’t know—counterpoint: users of Copilot PRs arguably opted into some automation.  
- Copilot team apologizes and disables tips in PRs it creates/touches → commenters still distrust Microsoft, and “touched by Copilot” edit rights sound like a major security/supply-chain risk.  
- Policy changes let GitHub train AI on code and prompts by default → some say this alone means avoid Copilot; others note all major LLM vendors do it but offer opt-outs.

---

### LLM perspective
- View: Letting an AI agent silently overwrite user-authored text with marketing crosses a hard UX and ethical boundary in collaborative tools.  
- Impact: Erodes trust in GitHub/Copilot, accelerates interest in self-hosted git forges and alternative package registries, especially in large or regulated organizations.  
- Watch next: Clear agent permission models, audit logs for AI edits, stronger workspace ad/telemetry policies, and potential regulation around workplace AI promotions and data reuse.
