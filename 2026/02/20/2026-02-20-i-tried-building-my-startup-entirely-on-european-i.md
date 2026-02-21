# I tried building my startup entirely on European infrastructure

- Score: 677 | [HN](https://news.ycombinator.com/item?id=47085483) | Link: https://www.coinerella.com/made-in-eu-it-was-harder-than-i-thought/

## TL;DR

A founder tried to build a startup using only European infrastructure for cost, data-sovereignty, and independence from US hyperscalers. They ended up with Hetzner for compute, Scaleway for gaps and email, Bunny.net for CDN, Nebius for AI GPUs, Hanko for auth, and a lot of self-hosted services on Kubernetes. The hardest parts were transactional email, leaving GitHub’s ecosystem, and odd domain pricing. Some US pieces remain unavoidable: app stores, social logins, and frontier AI models like Claude.

---

## Comment pulse

- EU-first stacks are increasingly common → Hetzner/OVH/Scaleway/Bunny plus self-hosted Gitea/Forgejo; registrar choice matters but .coms stay under US control anyway.  
- Baremetal sovereignty camp → run Mac Studios + MinIO + Postgres in-house for huge AWS savings—counterpoint: managed databases buy you tested disaster recovery.  
- Social login friction vs privacy → techies avoid Google/Apple SSO, but most users (especially at work) pick the fastest, passwordless-feeling option.

---

## LLM perspective

- View: EU-only infra is operationally heavier but realistic; the real barrier is ecosystem maturity, not raw performance or price.  
- Impact: Most relevant for privacy-sensitive or regulated products with EU customers; others may adopt a hybrid “EU-first, US-when-necessary” approach.  
- Watch next: Better EU transactional email, GPU clouds, auth; concrete benchmarks vs AWS; legal shifts around data transfers and AI model hosting.
