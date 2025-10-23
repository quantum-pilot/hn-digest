# MinIO stops distributing free Docker images

- Score: 644 | [HN](https://news.ycombinator.com/item?id=45665452) | Link: https://github.com/minio/minio/issues/21647#issuecomment-3418675115

- TL;DR
    - MinIO quietly stopped publishing official Docker images and shifted to source-only builds, landing alongside a critical CVE fix. Maintainers say the decision predated the CVE; critics argue it strands containers without updates and breaks auto-updaters, risking vulnerable deployments. Defenders reply it’s open source—folks can build their own images. The practical fallout is operational toil and trust costs; expect community-maintained images, possible forks, and migrations to alternatives like Ceph RGW, Garage, or RustFS.

- Comment pulse
    - Halting official images leaves fleets unpatched; auto-updaters stop, users miss CVE fixes. Better: warn, deprecate Docker Hub, hand off builds — counterpoint: OSS; build your own.
    - Trust erosion: prior console/OIDC removal, community docs pulled to AIStor, pricey opaque support; this change landed mid-CVE without notice, then thread locked.
    - Expect forks and exits: Bitnami images uncertain; history says lock-downs spawn replacements (Valkey, OpenTofu, Nextcloud).

- LLM perspective
    - View: Distribution withdrawal shifts update burden to users; reputational damage likely outweighs CI/CD savings and nudges community toward forks.
    - Impact: Breaks auto-update pipelines (Helm charts, Watchtower), forces orgs to build/sign images; downstream packs disabling MinIO; buyers reassess support value.
    - Watch next: Look for community-maintained images, a fork announcement, MinIO updating DockerHub with deprecation/CVE notice, or a licensing shift; track security advisories post-change.
