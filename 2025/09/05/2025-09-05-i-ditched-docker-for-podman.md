# I ditched Docker for Podman

- Score: 1104 | [HN](https://news.ycombinator.com/item?id=45137525) | Link: https://codesmash.dev/why-i-ditched-docker-for-podman-and-you-should-too

### TL;DR

After six months using Podman in production, the author prefers its daemonless, rootless-by-default design, direct process model, systemd integration, Kubernetes-oriented pods, and separation of image tasks across companion tools. OCI and Docker-style commands made the author’s FastAPI migration mostly familiar, while privileged ports, volume permissions, legacy socket consumers, and Compose workflows required adjustment. Commenters offer a less seamless picture: many value rootless operation, but report compatibility gaps with complex images, GPU tooling, `buildx`, older Ubuntu packages, and cross-platform installations. Several also reject Kubernetes YAML as a universal Compose replacement.

### Comment pulse

- Podman works well for many self-built images, yet some Docker-dependent workloads still force users into fallback environments.
- Ubuntu’s outdated packages and lack of a current official upstream package emerged as recurring adoption barriers.

### LLM perspective

- View: Podman is a strong Linux-native alternative, but “drop-in replacement” depends heavily on workload and distribution.
- Impact: Rootless defaults reduce privilege exposure while compatibility testing becomes an explicit migration cost.
- Watch next: Packaging freshness, Compose and GPU parity, and consistent behavior for images built around Docker quirks.
