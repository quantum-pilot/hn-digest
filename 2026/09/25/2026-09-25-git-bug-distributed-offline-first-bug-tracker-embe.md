# Git-bug: Distributed, offline-first bug tracker embedded in Git

- Score: 334 | [HN](https://news.ycombinator.com/item?id=49843174) | Link: https://github.com/git-bug/git-bug

### TL;DR

Git-bug embeds a distributed, offline-first issue tracker in Git without adding project files. Bugs travel through normal remotes, remain locally searchable, and can be managed through a CLI, terminal interface, bundled web UI, or GraphQL API. Bridges import and export issues for GitHub, GitLab, Jira, and Launchpad, while a formal on-disk specification supports alternative tooling. Discussion highlighted ambitions for authenticated public portals and pull requests, but also recurring adoption barriers, nontechnical-user needs, and an SSH-agent compatibility problem the author plans to address.

### Comment pulse

- Local-first issues improve resilience → repositories carry an offline backup and avoid dependence on one tracker vendor.
- Broader adoption needs accessible collaboration → commenters requested desktop-friendly workflows and secure hosted portals for non-Git users.
- Transport reliability remains a practical blocker → a reported SSH-agent issue prompted plans to optionally invoke the Git binary.

### LLM perspective

- View: Git-bug is strongest as portable issue infrastructure, not merely another tracker interface.
- Impact: Distributed teams can synchronize work offline while bridging existing centralized systems.
- Watch next: External authentication, remote-serving support, identity redesign, Git transport fixes, and proposed pull-request workflows.
