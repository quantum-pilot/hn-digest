# GitHub Is Having Issues

- Score: 191 | [HN](https://news.ycombinator.com/item?id=47237088) | Link: https://www.githubstatus.com/incidents/n07yy1bk6kc4

### TL;DR

GitHub suffered a roughly 70-minute incident on March 3 affecting Git operations, webhooks, APIs, Issues, pull requests, Actions, Codespaces, and Copilot. It identified the problem and applied mitigation by 19:17 UTC, restored individual services over the next 40 minutes, and resolved the incident at 20:09, promising a root-cause analysis. HN noted that Git itself is distributed, so commits can continue locally or over SSH, but modern review, SSO, CI, and deployment workflows remain centralized. The practical recommendation was a locally runnable break-glass pipeline.

### Comment pulse

- A bare repository over SSH is a simple fallback; reproducing GitHub’s surrounding identity and automation ecosystem is the hard part.
- Keep CI logic portable in scripts or containers → infrastructure-independent builds can launch locally when hosted runners and production fail together.
- AI-driven traffic growth may pressure GitHub — counterpoint: the incident report did not identify traffic as the cause.

### LLM perspective

- **View:** Distributed version control protects source history, not the centralized operational control plane teams assembled around it.
- **Impact:** Developers can keep coding, while releases, reviews, access, and incident response stall without prebuilt alternatives.
- **Watch next:** Failure-domain details, recurrence, service-level trends, local pipeline drills, repository mirrors, and emergency credential procedures.
