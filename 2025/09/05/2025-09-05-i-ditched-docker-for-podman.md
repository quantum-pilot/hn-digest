# I ditched Docker for Podman

- Score: 1104 | [HN](https://news.ycombinator.com/item?id=45137525) | Link: https://codesmash.dev/why-i-ditched-docker-for-podman-and-you-should-too

- TL;DR
    - The author moved from Docker to Podman for a safer, simpler model: no root daemon, rootless by default, tighter systemd/Kubernetes fit, and near drop-in CLI compatibility. Migration is mostly painless (Dockerfiles work; pods/systemd/Buildah/Skopeo shine), with caveats around rootless ports and volume permissions. HN likes Podman’s security and license posture but flags compatibility gaps (GitLab/buildx/GPU), Ubuntu’s stale packages and missing .deb, and Windows rough edges. Others argue Docker/compose—or even non-container deployments—remain simpler; image-slimming tools and jails were cited.

- Comment pulse
    - Podman breaks on some images (GitLab, buildx, GPU). Workarounds: rootful/rootless split, --capabilities, compatibility layer — counterpoint: others run GitLab and runners fine.
    - Ubuntu ships old Podman; no maintained .deb; Windows uninstalls flaky. Perception: non–Red Hat distros are second-class, pushing users to Fedora/RHEL or back to Docker.
    - Some question containers’ value: simple git hooks worked; jails/chroot did isolation; modern tools slim containers by tracing usage (SlimToolkit, OpenWrt ujail, Bifrost).

- LLM perspective
    - View: Podman’s architecture fits Linux servers; desktop parity and compatibility gaps are the real adoption blockers.
    - Impact: Teams can mix: Podman rootless for apps, Docker or rootful Podman where legacy or performance demands it.
    - Watch next: Official Ubuntu repo/PPA, Windows stability, GPU/runtime parity, buildx/buildkit equivalence, macOS Rosetta performance gains.
