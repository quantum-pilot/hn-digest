# Immich – High performance self-hosted photo and video management

- Score: 557 | [HN](https://news.ycombinator.com/item?id=45165684) | Link: https://github.com/immich-app/immich

- TL;DR
    - Immich is an AGPL, self-hosted photo/video manager with mobile/web apps, auto-backup, facial/object/CLIP search, maps, sharing, and admin tools. It’s fast-evolving and flagged as beta; maintainers advise independent backups. HN likes its near–Google Photos feature set and workable migrations, with users running it on Pi/NAS or low-cost VPS. Debates center on dependency churn vs. responsible updates, mixed Android/iOS performance and background sync, and the lack of first-class S3/object storage pushing CIFS/NAS or E2E alternatives like Ente.

- Comment pulse
    - Concern: fast-moving dependencies risk supply-chain attacks and unstable deployments → prefer Debian-packaged stability — counterpoint: maintainers delay bumps ~5 days and clearly mark beta.
    - Android/iOS experience is mixed → beta timeline helps some; others see slow thumbnails, stalled background uploads, and EXIF dates misread on iCloud imports.
    - Runs on Pi4/NAS and cheap VPS → migration manageable; no S3 backend leads to CIFS/Storage Box; some use one-click cloud installs and VPN/tunnels for access.

- LLM perspective
    - View: Strong self-hosted Google Photos contender; velocity is a strength but hinders distro packaging and risk-averse adopters.
    - Impact: Homelabbers gain control and CLIP-powered search; non-tinkerers and low-reliability locales benefit from managed hosting options.
    - Watch next: Object storage backend, stable release or LTS, background-sync fixes, and performance benchmarks on low-end ARM with AI features enabled.
