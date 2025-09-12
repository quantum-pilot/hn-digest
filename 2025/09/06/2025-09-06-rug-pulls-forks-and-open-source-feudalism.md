# Rug pulls, forks, and open-source feudalism

- Score: 275 | [HN](https://news.ycombinator.com/item?id=45146967) | Link: https://lwn.net/SubscriberLink/1036465/e80ebbc4cee39bfb/

- TL;DR
  - Dawn Foster maps open-source power dynamics: companies can “rug pull” by relicensing or closing development; communities counter with forks. Case studies (Elastic/OpenSearch, Terraform/OpenTofu, Redis/Valkey, Puppet/OpenVox) show forks thrive when user-driven or multi-company-backed; moving into a foundation later attracts fewer new contributors. CLAs correlate with rug pulls; neutral, multi-org governance and DCO reduce risk. Relicensing often depresses usage despite GitHub fork spikes. HN debates CLAs vs copyleft, sustainability vs “purism,” clouds’ role, and practical mitigations.

- Comment pulse
  - CLA empowers relicensing → shifts control to companies; DCO avoids imbalance. AGPL+CLA can trap competitors, as seen with LXD/Incus.
  - Forks as accountability → Valkey/OpenTofu show users regroup under foundations; forks often trail originals — counterpoint: old code persists, so 'rug pull' mislabels harm.
  - Sustainability over purism → maintainers need funding; permissive licenses invite free-riding; clouds’ “contribution” is distribution and infra investment, not always patches.

- LLM perspective
  - View: Treat license and governance as supply-chain risk; avoid CLAs when possible; prefer multi-company projects and foundations from day zero.
  - Impact: Orgs will reassess dependencies, fund critical maintainers, and prepare fork playbooks; teams invest in source-based builds to ease switching.
  - Watch next: Track CLA adoption, relicensing announcements, and contributor concentration; watch OpenTofu/Valkey vs upstream usage; benchmark community health with CHAOSS metrics.
