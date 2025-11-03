# Using FreeBSD to make self-hosting fun again

- Score: 189 | [HN](https://news.ycombinator.com/item?id=45789424) | Link: https://jsteuernagel.de/posts/using-freebsd-to-make-self-hosting-fun-again/

TL;DR
An author rekindles self-hosting joy by switching to FreeBSD for a fresh, simpler workflow: jails via BastilleBSD, VMs via bhyve, great man‑page docs, and long‑term, stable interfaces. Confusions (e.g., base release vs pkg/ports) were eased by a helpful community. HN echoes the appeal: ZFS and jails make homelabs pleasant; OpenBSD excels for router/DNS roles; automation with Ansible keeps setups reproducible. Caveats surface around FreeBSD’s big.LITTLE scheduling on Alder Lake; some stick with Linux/Nix or pin cores. BSDs also shine on truly old hardware.

Comment pulse
- OpenBSD for network infra → simple, cohesive configs beat Linux’s many daemons; stable base avoids drama.
- FreeBSD homelabs → jails+pf+ZFS enable lightweight isolation; Gitea/CI/blog setups; snapshots and Ansible deliver fast, reproducible rebuilds.
- Hybrid CPUs caveat → ULE underuses big.LITTLE (e.g., Alder Lake); pinning mitigates — counterpoint: choose Linux/Nix or unaffected workloads until scheduler improves.

LLM perspective
- View: Pick BSD by role: FreeBSD for jails+ZFS services, OpenBSD for routing, Linux for bleeding‑edge hardware and broader vendor support.
- Impact: Simpler stacks shift hobbyists from Docker/Kubernetes toward jails plus Ansible, cutting overhead while keeping reproducibility and easy debugging.
- Watch next: Track ULE big.LITTLE patches, BastilleBSD/vm‑bhyve releases, and clear FreeBSD docs on releases vs ports/pkg; request comparative jail/container benchmarks.
