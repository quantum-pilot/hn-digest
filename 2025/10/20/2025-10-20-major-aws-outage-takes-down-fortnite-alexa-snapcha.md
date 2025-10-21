# Major AWS outage takes down Fortnite, Alexa, Snapchat, and more

- Score: 209 | [HN](https://news.ycombinator.com/item?id=45641143) | Link: https://www.theverge.com/news/802486/aws-outage-alexa-fortnite-snapchat-offline

- TL;DR
  - AWS’s US-EAST-1 suffered a major outage early Oct 20, taking down consumer apps (Fortnite, Snapchat, Alexa, ChatGPT) and tools (Airtable, Canva, Zapier, Perplexity, McDonald’s). AWS cited a DNS issue originating in the EC2 internal network, disrupting network load balancer health checks and throttling new EC2 launches. Some platforms recovered within hours; others lagged. The episode reprises US-EAST-1’s past incidents (2020, 2021, 2023) and renews calls for multi-region architectures and clearer dependency/alerting practices.

- LLM perspective
  - View: Single-region reliance magnifies blast radius; internal control-plane faults can cascade across dependent services.
  - Impact: Consumer trust, on-call burnout, potential SLA credits; teams revisit failover, DNS, NLB health-check dependencies.
  - Watch next: AWS postmortem, mitigation roadmap, per-service RCAs; measure adoption of multi-region by major apps in coming quarters.
