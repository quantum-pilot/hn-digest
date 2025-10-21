# AWS Multiple Services Down in us-east-1

- Score: 1549 | [HN](https://news.ycombinator.com/item?id=45640838) | Link: https://health.aws.amazon.com/health/status?ts=20251020

- TL;DR
  - A widespread us‑east‑1 outage hit 90+ AWS services. It began with DNS failures to DynamoDB endpoints, then an internal Network Load Balancer health‑check subsystem degraded connectivity and throttled EC2 launches. Lambda SQS polling and control‑plane actions backlogged; recovery is partial, with some services still “degraded.” HN discussion centers on blocked multi‑region failover due to IAM Identity Center being regional, renewed skepticism of us‑east‑1, debates over diversification vs inevitable cloud outages, and visible consumer knock‑ons (Whole Foods, Alexa, Premier League VAR).

- Comment pulse
  - Resilience gap → Identity Center only in us‑east‑1 blocked failover; DNS-dependent auth/vault paths created circular dependencies that locked teams out of the control plane.
  - Region strategy → us‑east‑1 seen as outage-prone; move workloads elsewhere/multi‑cloud, and today’s downtime dents 99.99% targets — counterpoint: all providers suffer outages; ‘global’ means us‑east‑1.
  - Real-world impact → Whole Foods discounts, Alexa commands, Amazon.com search, and Premier League VAR degraded—showing consumer-facing dependencies on a single AWS region.

- LLM perspective
  - View: Single shared subsystems and control-plane regionality became hidden single points; DNS issues amplified the blast radius beyond individual services.
  - Impact: Infra teams must decouple identity, DNS, and failover from any one region; pre-provision capacity; maintain offline break-glass and cross-account access.
  - Watch next: AWS postmortem on the NLB health subsystem; regionalized Identity Center/STS; guidance on global-service independence; third-party outage metrics; customer migration signals.
