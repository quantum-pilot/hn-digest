# Devpush – Open-source and self-hostable alternative to Vercel, Render, Netlify

- Score: 246 | [HN](https://news.ycombinator.com/item?id=45501279) | Link: https://github.com/hunvreus/devpush

- TL;DR
  - Devpush is an open-source, self-hosted PaaS aiming to replicate Vercel’s push-to-deploy UX: GitHub-based builds, blue‑green zero‑downtime rollouts/rollbacks, runtime logs, RBAC teams, env management, and automatic SSL/custom domains. It runs Dockerized apps across languages and installs via scripts on Ubuntu/Debian; MIT-licensed. HN compares it to Coolify, CapRover, and Dokploy—favoring maturity or simplicity—while others prefer k3s for control. Several report success running many apps cheaply on Hetzner/OVH; one critic flags Python dependency bloat.

- Comment pulse
  - CapRover favored for simplicity; Coolify called buggy at times; some prefer Dokploy over Coolify → perceived stability/UX differences drive choices.
  - Git-based deploys, zero-downtime, and no Dockerfiles for common runtimes; roadmap adds custom images and Docker Swarm for multi-server.
  - Self-hosted PaaS vs k3s → some prefer helm/k9s control on cheap Hetzner; others value UI convenience. — counterpoint: Python stack seen as unnecessary dependency bloat.

- LLM perspective
  - View: Targets teams avoiding vendor lock-in, prioritizing streamlined deploys over Kubernetes complexity.
  - Impact: Could lower ops burden for small startups on Hetzner/OVH; less suitable for bespoke infra or extreme scale.
  - Watch next: Validate multi-node story: Docker Swarm support, backup/restore UX, autoscaling, metrics/alerts, and reproducible zero-downtime rollbacks under failure.
