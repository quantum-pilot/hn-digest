# FediMeteo: A €4 FreeBSD VPS Became a Global Weather Service

- Score: 188 | [HN](https://news.ycombinator.com/item?id=46436889) | Link: https://it-notes.dragas.net/2025/02/26/fedimeteo-how-a-tiny-freebsd-vps-became-a-global-weather-service-for-thousands/

### TL;DR

FediMeteo publishes localized weather forecasts through ActivityPub accounts and RSS using Python, Open-Meteo, snac, and FreeBSD jails. A €4 monthly VPS with four shared cores, 8 GB RAM, and 75 GB storage runs 39 jails covering 2,937 cities across 38 countries, serving about 7,707 direct followers. Updates run every six hours; the system uses 501 MB RAM and averages roughly 25% load. HN celebrated the efficient design and traded sources for similarly inexpensive virtual servers.

### Comment pulse

- Small systems can serve globally → FreeBSD and snac sustain thousands of feeds without Kubernetes or hyperscale services.
- Cheap VPS capacity surprises readers → commenters compared providers, dedicated versus shared cores, storage, and egress deals.

### LLM perspective

- View: Simple serialization and strong isolation outperform speculative scaling when workload shape is predictable.
- Impact: Community services can remain affordable, inspectable, and locally controlled without sacrificing geographic reach.
- Watch next: Monitor API quotas, backup restores, single-maintainer continuity, moderation load, and performance as coverage expands.
