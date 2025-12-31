# FediMeteo: A €4 FreeBSD VPS Became a Global Weather Service

- Score: 188 | [HN](https://news.ycombinator.com/item?id=46436889) | Link: https://it-notes.dragas.net/2025/02/26/fedimeteo-how-a-tiny-freebsd-vps-became-a-global-weather-service-for-thousands/

## TL;DR
On a €4/month FreeBSD VPS, the author runs FediMeteo, a federated weather bot network pushing localized forecasts to ~7,700 followers across ~2,900 cities in 38 countries. Using FreeBSD jails, snac (ActivityPub), a small Python script, and Open‑Meteo, each city is a lightweight bot user posting markdown every six hours. Coordinate caching, ZFS snapshots, and minimal design keep RAM near 500 MB and CPU mostly idle. HN readers see it as proof that simple, non‑cloud‑native stacks still scale.

## Comment pulse
- FreeBSD + simple stack can be fast → several report tiny FreeBSD VMs with very low RAM use—counterpoint: others say Alpine Linux feels equally lean and responsive.  
- Modest hardware is enough → HN itself and FediMeteo both run on 4‑core FreeBSD machines, yet comfortably serve sizable global audiences.  
- Cheap VPS hunting is a hobby → commenters swap sub‑€5 providers and promo deals, noting the emotional “lock‑in” once you start owning a VPS.

## LLM perspective
- View: This design validates “bots over ActivityPub” as a lightweight pattern for practical, subscription‑style services like weather, alerts, and status feeds.  
- Impact: Shows sysadmins they can deliver global services with BSD jails, cron, and small scripts instead of Kubernetes or hyperscale cloud stacks.  
- Watch next: More utilities leveraging fediverse protocols plus minimal backends; systematic measurements of cost, reliability, and reach versus commercial weather and notification APIs.
