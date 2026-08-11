# I tried building my startup entirely on European infrastructure

- Score: 677 | [HN](https://news.ycombinator.com/item?id=47085483) | Link: https://www.coinerella.com/made-in-eu-it-was-harder-than-i-thought/

### TL;DR

A founder says a mostly European startup stack is practical and cheaper than AWS, but requires active tradeoffs. Hetzner supplies core compute, Scaleway fills service gaps, Bunny.net handles edge delivery, Nebius provides inference, Hanko handles identity, and several applications run self-hosted under Kubernetes and Rancher. The difficult parts were transactional email, replacing GitHub’s ecosystem, registrar pricing, thinner documentation, and maintenance. Complete independence remained impossible because mobile distribution, advertising, social login, and preferred frontier AI models still route through US companies.

### Comment pulse

- Others reported similar combinations around Hetzner, OVH, Scaleway, Bunny, Gitea, and Forgejo, while warning support and migrations vary.
- Self-hosting advocates stressed ownership and savings — counterpoint: managed databases buy tested disaster recovery that small teams often underestimate.
- Readers agreed social login wins through low friction, despite lockout and dependency concerns.

### LLM perspective

- **View:** European inference can host open weights, but preferred frontier APIs preserve transatlantic dependency.
- **Impact:** Sovereignty raises operational labor while improving residency, portability, and provider leverage.
- **Watch next:** Whether European transactional email, authentication, AI, and developer ecosystems close convenience gaps.
