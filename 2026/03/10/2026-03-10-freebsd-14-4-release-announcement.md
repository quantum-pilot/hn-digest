# FreeBSD 14.4-Release Announcement

- Score: 147 | [HN](https://news.ycombinator.com/item?id=47321499) | Link: https://www.freebsd.org/releases/14.4R/announce/

## TL;DR
FreeBSD 14.4 is a maintenance point release for the 14-STABLE branch, adding OpenSSH 10.0p2 with a default hybrid post‑quantum key exchange (mlkem768x25519‑sha256), OpenZFS 2.2.9, better cloud‑init compatibility, and host–guest filesystem sharing for bhyve via p9fs. It ships for seven architectures, with ISOs, SD, VM, and cloud images (EC2, GCE; Azure pending), and is supported to end‑2026, with 14.x supported to 2028. The release is dedicated to former release engineering lead Ken Smith. HN discussion centers on FreeBSD’s cohesive design, networking strengths, ZFS boot environments, simple init compared to systemd, Docker gaps, and whether new deployments should choose 14.4 or 15.0.

---

## Comment pulse
- Why FreeBSD? → Cohesive base system, strong docs, excellent networking and ZFS, simpler rc.conf init, fewer abstraction layers; feels smaller and more approachable than Linux.  
  — counterpoint: Linux still leads on breadth of features and container ecosystem.

- Version choice → Some suggest skipping 14.4 for 15.0 or even -CURRENT; a core FreeBSD member clarifies 14.x remains the conservative recommendation while 15.0.0 matures.

- Virtualization and tooling → p9fs for bhyve excites users (share ZFS datasets instead of ZVOLs); others weigh FreeBSD vs openSUSE Tumbleweed, noting lack of first‑class Docker on BSD as a blocker.

---

## LLM perspective
- View: 14.4 is a conservative, infrastructure‑focused release, quietly adding important crypto, storage, and virtualization capabilities without big user‑visible shifts.

- Impact: Best suited for servers needing long support windows, ZFS, bhyve, or EC2/GCE images; desktops/devs may eye 15.x.

- Watch next: Stabilization of 15.x, evolution of container/OCI tooling on FreeBSD, and how hybrid post‑quantum SSH defaults propagate across other OSes.
