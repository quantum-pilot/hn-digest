# Flightcontrol: A PaaS that deploys to your AWS account

- Score: 155 | [HN](https://news.ycombinator.com/item?id=45488441) | Link: https://www.flightcontrol.dev/

- TL;DR
  - Flightcontrol is a PaaS that provisions and deploys directly into your AWS account, bundling CI/CD, ECS/Fargate/EC2, Lambda, RDS/Redis, static sites, preview environments, and cost visibility, plus 24/7 support. HN feedback: users like the Heroku-like flow without ceding AWS control, but note AWS quirks leaking through, earlier ECS-EC2 instability and slow teardown, security/default concerns (e.g., RDS), and pricing. Many suggest Fargate unless GPUs, or simpler Docker Swarm/VPS for small teams. Some want open source; Flightcontrol says defaults improved and IaC “blocks” are coming.

- Comment pulse
  - Useful AWS abstraction → Speeds shipping; occasional AWS quirks surface, but better than wrestling AWS directly.
  - Early reliability issues → Docker behavior differences, slow provisioning/teardown; ECS-EC2 agent problems noted; prefer Fargate unless GPUs — counterpoint: vendor claims fixes and preview tooling.
  - Security and lock-in concerns → Past RDS public-by-default, CIS failures, closed-source; desire IaC “blocks” and lower pricing; enterprises compare to internal platforms; FOSS alternatives exist.

- LLM perspective
  - View: Compelling middle path: Heroku-like ergonomics on your AWS. Value depends on how much AWS complexity you can tolerate.
  - Impact: Best for teams needing AWS credits, compliance, or GPUs, but lacking DevOps; less ideal for ultra-lean single-VPS stacks.
  - Watch next: Track IaC “blocks” release, ECS-EC2 stability rollout, Fargate GPU coverage, and transparent pricing/security defaults documented against CIS benchmarks.
