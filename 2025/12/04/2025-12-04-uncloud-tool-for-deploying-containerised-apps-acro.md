# Uncloud - Tool for deploying containerised apps across servers without k8s

- Score: 352 | [HN](https://news.ycombinator.com/item?id=46144275) | Link: https://uncloud.run/

### TL;DR
Uncloud is an open-source, control-plane-free container orchestrator aimed at teams who’ve outgrown single-node Docker Compose but don’t want Kubernetes. It creates a WireGuard mesh between machines, assigns each container its own IP, and uses Caddy for automatic HTTPS and load balancing. State is synchronized peer-to-peer (via Corrosion), giving a “multi-machine Docker Compose” experience with an imperative CLI and no external registry. HN discussion focuses on its sweet spot versus k3s/Swarm, security tradeoffs, and the value of a control plane.

---

### Comment pulse
- Pitch: multi-machine Compose with p2p state, WireGuard mesh, built-in HTTPS, and image distribution without a registry—counterpoint: small k3s/k3d setups are already easy enough.
- Concerns: curl|bash as root for `uc machine init`, missing features (secrets, routing rules, stack isolation), and unclear stories for multi-user access and CI/CD integration.
- Philosophy split: some see control planes and schedulers as indispensable; others want simpler equal-node meshes for tiny clusters (2–7 nodes, tens of containers).

---

### LLM perspective
- View: If it matures, Uncloud could become the “modern Swarm”: simple, Compose-native clustering with built-in networking and TLS.
- Impact: Most useful for small orgs and homelabbers self-hosting apps across a few heterogeneous machines without managed Kubernetes.
- Watch next: Stability under node failures, clearer security posture, and migration docs from Swarm/Kamal/k3s will determine real-world adoption.
