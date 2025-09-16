# The Deletion of Docker.io/Bitnami

- Score: 348 | [HN](https://news.ycombinator.com/item?id=45048419) | Link: https://community.broadcom.com/tanzu/blogs/beltran-rueda-borrego/2025/08/18/how-to-prepare-for-the-bitnami-changes-coming-soon

- TL;DR
    - Bitnami will remove its public Docker Hub images, now postponed to Sept 29, with scheduled brownouts; no new Docker Hub OCI since Aug 28. Users must switch to Bitnami Secure Images (Photon-based, paid) or Legacy (unsupported, temporary). Sources and Helm remain open on GitHub. HN reactions: value-add vs mere packaging, Broadcom-style monetization, and CRA-driven compliance; some defend charging; alternatives appear; rumored pricing around $50k challenges the “democratizing security” claim. Brownouts on Aug 28–29, Sep 2–3, and Sep 17–18.

- Comment pulse
    - Paywalling OSS packaging adds little value → images mirror upstream; Helm charts carry more value — counterpoint: maintaining Makefiles, env config, tests is substantial work.
    - Broadcom playbook → squeeze embedded enterprise software with price hikes; expect little regard for community uproar.
    - Compliance shift → EU CRA pushes enterprises toward supported, attestable images; others argue CRA doesn’t force removing free tiers.

- LLM perspective
    - View: Short-term fix is mirroring and pinning digests; medium-term migrate to upstream official images or self-built equivalents.
    - Impact: CI/CD pipelines, Helm values, imagePullSecrets, and allowlists must change; watch for restart storms in clusters pulling deleted tags.
    - Watch next: Brownout image lists, Photon vs Debian compatibility gaps, and whether competitors publish clear pricing and credential helpers.
