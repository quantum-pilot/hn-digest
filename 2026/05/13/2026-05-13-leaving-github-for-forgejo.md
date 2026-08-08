# Leaving GitHub for Forgejo

- Score: 516 | [HN](https://news.ycombinator.com/item?id=48121266) | Link: https://jorijn.com/en/blog/leaving-github-for-forgejo/

### TL;DR

The author made self-hosted Forgejo v15 LTS canonical after GitHub’s 257 incidents in a year, absorption into Microsoft CoreAI, default Copilot interaction-data training, and unresolved US-jurisdiction exposure; the Dutch government independently chose Forgejo for sovereign public code. His NUC runs Forgejo, Postgres, and Traefik, while CI is isolated with KVM, gVisor, egress filtering, scoped tokens, and weekly destructive rebuilds. Costs include weaker discovery, incomplete Actions compatibility, Renovate replacing Dependabot, and no enterprise support. Commenters favored multi-host mirrors and federation over simply exchanging one centralized home for another.

### Comment pulse

- Git’s distributed design supports multiple remotes; contributors urged durable GitHub mirrors because niche hosts and personal servers can disappear.
- GitHub’s social graph remains uniquely valuable — counterpoint: GitSocial and planned Forgejo federation aim to enable collaboration across independent forges.
- Self-hosters reported years of cheap NUC reliability, but Pi users saw silent mirror failures and database locks.

### LLM perspective

- View: The CI runner, not the forge application, is the critical security boundary in a self-hosted migration.
- Impact: Ownership reduces platform risk while transferring uptime, backups, patching, and incident response to maintainers.
- Watch next: Federation delivery, Actions compatibility, mirror durability, enterprise support, and repository-training controls.
