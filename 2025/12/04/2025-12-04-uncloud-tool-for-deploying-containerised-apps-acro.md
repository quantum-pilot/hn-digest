# Uncloud - Tool for deploying containerised apps across servers without k8s

- Score: 352 | [HN](https://news.ycombinator.com/item?id=46144275) | Link: https://uncloud.run/

### TL;DR

Uncloud targets self-hosted fleets with a Docker Compose workflow spanning machines, a WireGuard mesh, service discovery, Caddy HTTPS, rolling deployments, and peer-synchronized state instead of a central control plane. Its CLI can build and distribute images without an external registry, then scale replicas across providers or on-premises hardware. The project says it is not yet production-ready. Commenters like the space between Compose and Kubernetes but question root-level bootstrap commands, secrets, network isolation, engineer onboarding, CI access, and advantages over k3s, Swarm, Kamal, or Ansible.

### Comment pulse

- Control-plane absence simplifies tiny clusters → counterpoint: Kubernetes users consider reconciliation and scheduling the core benefit, especially when managed.
- Current gaps affect trust → secrets lack encrypted-at-rest support, stacks share network reach, and onboarding documentation appears incomplete.
- The practical niche is narrow but real → operators with two to seven nodes want more than Compose without Kubernetes administration.

### LLM perspective

- View: Its value depends on operational simplicity surviving the distributed-state and security complexity it absorbs.
- Impact: Small teams could gain multi-host resilience without adopting a full scheduler or external registry.
- Watch next: Audit installer privileges, partition behavior, recovery, secret handling, tenant isolation, and production-readiness milestones.
