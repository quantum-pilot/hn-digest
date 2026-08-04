# We stopped AI bot spam in our GitHub repo using Git's –author flag

- Score: 386 | [HN](https://news.ycombinator.com/item?id=48181125) | Link: https://archestra.ai/blog/only-responsible-ai

### TL;DR

Archestra says AI-generated activity turned a $900 bounty issue into 253 comments, produced 27 mostly untested PRs for one feature, and consumed half a maintainer-day weekly. After reputation scoring failed and an automated sheriff rejected legitimate work, the project limited interaction to prior contributors. Newcomers complete a CAPTCHA-backed rules onboarding; an Action then commits their handle to main with their GitHub identity as Git author, satisfying GitHub’s prior-contributor check. HN supported platform controls but warned the workaround can elevate workflow trust and remains vulnerable to farmed reputations.

### Comment pulse

- The workaround changes security posture → prior-contributor status can bypass first-timer approval gates — counterpoint: requiring approval for every external contributor contains that risk.
- GitHub should own the abuse layer → maintainers compared AI PR spam to email spam and requested platform rate limits, tokens, and archival.
- Reputation scores invite gaming → Sybil accounts can boost one another until one bot gains trust, then propagate credibility to peers.

### LLM perspective

- **View:** Admission control preserves maintainer attention, but identity remains a weak proxy for contribution quality.
- **Impact:** Legitimate newcomers accept onboarding friction; maintainers regain signal, while GitHub Actions policies require independent hardening against newly trusted accounts.
- **Watch next:** Measure spam reduction, false rejection, onboarding conversion, account farming, workflow abuse, and whether GitHub ships native controls.
