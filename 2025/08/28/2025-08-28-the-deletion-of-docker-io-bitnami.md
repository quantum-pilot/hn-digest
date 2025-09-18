# The Deletion of Docker.io/Bitnami

- Score: 348 | [HN](https://news.ycombinator.com/item?id=45048419) | Link: https://community.broadcom.com/tanzu/blogs/beltran-rueda-borrego/2025/08/18/how-to-prepare-for-the-bitnami-changes-coming-soon

- TL;DR
    - Bitnami will remove docker.io/bitnami; deletion is postponed to Sep 29 with rolling 24‑hour brownouts beforehand. New container builds/Helm charts stop on Docker Hub; users must retarget registries. Options: paid Bitnami Secure Images (hardened Photon, some dev‑only free) or a temporary, unsupported Bitnami Legacy archive. Helm charts’ source remains Apache‑2 on GitHub. Broadcom cites security/compliance costs; HN debates Bitnami’s added value, “paywall/extortion” claims, Broadcom’s enterprise playbook, EU CRA pressure, alternatives, and rumored ~$50k pricing.

- Comment pulse
    - Bitnami’s value is “just packaging” → others say their Makefiles/configs and Helm charts are nontrivial; official upstream images often suffice.
    - “Extortion” vs right to stop freebies → critics cite Broadcom’s acquire‑and‑monetize strategy—counterpoint: users should self‑maintain if unhappy.
    - CRA drives compliance posture → opponents say free images could continue. Alternatives touted; opaque enterprise pricing (~$50k) undercuts “democratization.”

- LLM perspective
    - View: Treat public images as temporary; pin digests, mirror privately, prefer official upstream images when feasible.
    - Impact: CI/CD, Helm releases, and Kubernetes clusters must update image paths; air‑gapped and IaC templates need coordinated changes.
    - Watch next: Exact Legacy EOL, brownout image lists, competitor price transparency, and CRA enforcement milestones shaping enterprise procurement.
