# Tailscale didn't stop the Hugging Face intrusion

- Score: 379 | [HN](https://news.ycombinator.com/item?id=49127306) | Link: https://tailscale.com/blog/hugging-face-intrusion

- TL;DR
    - Tailscale published a post on the Hugging Face intrusion explaining that attackers abused a long‑lived Tailscale auth key leaked from HF’s CI environment, not a software bug. They frame it as a failure of secure defaults and advertise features like key expiry, tags, ACLs, SSO and device posture that could have limited impact. HN readers praise the transparency yet note it’s also smart marketing, arguing mesh VPN tools must better discourage reusable credentials and detect anomalous node enrollment at scale.
    - *Content unavailable; summarizing from title/comments.*

- Comment pulse
    - Transparent post builds trust; owning responsibility despite no exploit is rare—counterpoint: tone doubles as humblebrag marketing that sells paid “secure default” features.
    - Hugging Face leaked a reusable auth key from CI; critics say systems should make such practices harder, with enforced expiry, scopes, or “high‑security” modes.
    - 181 new nodes joining a tailnet seems alert‑worthy, but CI and autoscaling routinely spawn hundreds—determining what’s “unexpected” at scale is non‑trivial.

- LLM perspective
    - View: Secure defaults should assume credential leaks; vendors should ship short‑lived, scoped tokens and strong default alerts for anomalous node growth.
    - Impact: Incidents like this push VPN/mesh providers toward opinionated configurations, reducing flexibility but improving real‑world security for less‑mature teams.
    - Watch next: Watch for vendors auto‑curbing blast radius via mandatory key rotation, per‑environment segmentation, CI‑specific roles, and anomaly detection on enrollment behavior.
