# Arch Linux Now Has a Bit-for-Bit Reproducible Docker Image

- Score: 294 | [HN](https://news.ycombinator.com/item?id=47871519) | Link: https://antiz.fr/blog/archlinux-now-has-a-reproducible-docker-image/

### TL;DR

Arch Linux now publishes a `repro` Docker tag whose independent builds produce identical digests. Determinism comes from reusing its reproducible root filesystem, fixing `SOURCE_DATE_EPOCH`, normalizing image timestamps, and removing `ldconfig`’s variable auxiliary cache. The caveat is substantial: pacman keys are stripped, so users must initialize and populate the keyring before installing packages. Readers welcomed the confidence and debugging value, but treated bit-for-bit output as one operational property rather than a universal answer to container construction, dependency availability, or maintenance.

### Comment pulse

- Reproducibility was called a “boring win” whose value appears when tiny unexplained deltas consume hours of incident investigation.
- Arch users cited containers as clean environments for testing dotfiles, alongside native, WSL, and VM installations.
- Opinions split on `apt-get update` — counterpoint: pinning improves repeatability, but stale images retain known vulnerabilities.

### LLM perspective

- Public rebuilders should independently publish digests, logs, toolchain versions, and signed attestations.
- A deterministic keyring design could move the image from specialist tag to practical default.
- Watch whether Docker and Podman preserve equality across versions, hosts, and registry round-trips.
