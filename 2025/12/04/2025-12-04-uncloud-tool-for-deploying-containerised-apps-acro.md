# Uncloud - Tool for deploying containerised apps across servers without k8s

- Score: 352 | [HN](https://news.ycombinator.com/item?id=46144275) | Link: https://uncloud.run/

### TL;DR

Uncloud aims to run Docker Compose applications across ordinary Linux servers without Kubernetes. It provides a Docker-like CLI, direct image distribution, rolling deployments, Caddy HTTPS, DNS service discovery, load balancing, and a WireGuard mesh with peer-synchronized cluster state instead of a central control plane. The creator targets small deployments needing several machines but not Kubernetes scheduling overhead, and says the agent uses under 150 MB RAM. Commenters liked the Compose-to-multihost niche but questioned installation safety, secrets, isolation, onboarding, CI access, and why k3s or simpler automation is insufficient.

### Comment pulse

- Supporters saw useful territory between single-host Compose and Kubernetes, especially for mixed cloud, bare-metal, and NATed machines.
- Skeptics preferred k3s, Podman with Ansible, Kamal, or Swarm and questioned abandoning declarative reconciliation.
- Root-level `curl | bash` installation and incomplete secrets or network isolation blocked some early adopters.

### LLM perspective

- View: Uncloud trades scheduler sophistication for a smaller mental and operational model tailored to known services.
- Impact: Small teams could gain multi-host resilience without maintaining etcd or a managed control plane.
- Watch next: Harden installation, document partitions, add secrets and isolation, benchmark recovery, and clarify CI onboarding.
