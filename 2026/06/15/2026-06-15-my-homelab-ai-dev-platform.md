# My Homelab AI Dev Platform

- Score: 216 | [HN](https://news.ycombinator.com/item?id=48542433) | Link: https://rsgm.dev/post/ai-dev-platform/

### TL;DR

The author turned OpenCode’s web server into a persistent, device-synced homelab coding environment on a TrueNAS VM. The agent can access the internet and Git, install tools as root, create worktrees, and push feature branches, but cannot reach services or deploy directly. Humans review and merge pull requests; GitOps then deploys changes through Arcane, Home Assistant, or Cloudflare Pages. This sped release-note review, container upgrades, health-check additions, and cross-stack networking edits. HN shared Forgejo, n8n, Argo, and k3s variants while noting remote-build resources and missing Forgejo Actions logs as constraints.

### Comment pulse

- Least privilege contains agent risk → dedicated Git credentials, branch-only pushes, no service network access, and human merges limit unintended deployment.

- Persistence improves mobility → synchronized sessions, terminal, file browser, diffs, and worktrees let infrastructure work continue across desktop and phone.

- CI feedback is the gap → Forgejo’s public API omits Actions logs — counterpoint: issue-triggered runners can instead execute OpenCode and return PRs.

### LLM perspective

- **View:** The architecture treats AI as an untrusted contributor, using Git’s review boundary instead of granting production credentials.

- **Impact:** Homelab operators gain asynchronous maintenance from any device; teams could generalize the pattern with ephemeral workers and audit logs.

- **Watch next:** Add documented CI-log access, automated validation, signed commits, resource quotas, secret isolation, rollback checks, and deployment observability.
