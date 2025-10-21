# Docker Systems Status: Full Service Disruption

- Score: 323 | [HN](https://news.ycombinator.com/item?id=45640877) | Link: https://www.dockerstatus.com/pages/incident/533c6539221ae15e3f000031/68f5e1c741c825463df7486c

- TL;DR
    - An AWS incident triggered a broad Docker outage affecting Hub, Registry, Auth, Build Cloud, and more from 07:16–10:05 UTC; services recovered after monitoring. Docker confirmed the cloud-provider link, promised a post‑mortem, and acknowledged developer impact. HN reports widespread build failures due to docker.io defaults, with partial relief via AWS’s public ECR and Google’s mirror—though mirrors also saw flakiness and rate limits. Discussion centers on resilience: avoid single‑provider dependencies, pin images, run private registries or proxy caches, and make CI tools’ registry sources configurable.

- Comment pulse
    - AWS outage cascaded to Docker services → Docker confirmed provider issue; auth.docker.io errors halted pulls and builds — counterpoint: multi-cloud isn't trivial; mirrors also failed.
    - Use registry mirrors to bypass docker.io → public.ecr.aws and mirror.gcr.io worked for some; rate limits and 5XX flakiness persisted during AWS incident.
    - Own or cache base images → Harbor/Nexus proxy caches reduce upstream dependency; default docker.io in tools/CI can still force pulls you can't redirect.

- LLM perspective
    - View: Container supply chain has SPOFs; treat registries as critical infra with redundancy, caching, pinning, and tested failovers.
    - Impact: Teams will add proxy caches, explicit registry domains, alternate mirrors, and reroute CI images to reduce docker.io dependence.
    - Watch next: Docker/AWS post-mortems, auth endpoint redundancy plans, mirror reliability benchmarks, and CI actions adding configurable registries with sane fallbacks.
