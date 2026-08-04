# My security camera shipped a GitHub admin token in its login page

- Score: 489 | [HN](https://news.ycombinator.com/item?id=49034292) | Link: https://hhh.hn/hanwha-github-token/

### TL;DR

A researcher unpacked Hanwha security-camera firmware and found a GitHub token duplicated across roughly 30 frontend files, apparently because a Vite build embedded the CI job’s entire environment. The credential had administrator access to hundreds of company repositories and appeared in three of about 500 downloaded firmware images; Hanwha revoked it within 12 hours of disclosure. The firmware also exposed hardcoded decryption material and unexplained U.S. Defense Department IP addresses. HN framed it as systemic IoT insecurity, debating containment, open firmware, and what the address data implied.

### Comment pulse

- Camera containment beats vendor trust → commenters recommended an internet-blocked VLAN plus ONVIF-compatible recorders, limiting consequences even when proprietary firmware is compromised.
- Alternative firmware has practical footholds → Thingino, OpenIPC, Wyrecam, and supported SD-card flashing offer varying routes beyond sealed vendor software.
- DoD addresses prompted suspicion → some inferred organizational ties or product risk — counterpoint: others noted companies sometimes misuse public address space internally.

### LLM perspective

- **View:** The root cause was build-boundary collapse: secret-bearing CI state became client-side product content through unchecked environment serialization.
- **Impact:** One leaked token could expose source, releases, and supply-chain controls across hundreds of repositories, far beyond any single camera.
- **Watch next:** Verify token rotation, audit its historical use, purge firmware artifacts, narrow CI scopes, and add release-time secret scanning.
