# AWS outage shows internet users 'at mercy' of too few providers, experts say

- Score: 235 | [HN](https://news.ycombinator.com/item?id=45646649) | Link: https://www.theguardian.com/technology/2025/oct/20/amazon-web-services-aws-outage-hits-dozens-websites-apps

### TL;DR

The Guardian reports that an internal AWS failure originating in US-East-1 disrupted thousands of companies and services worldwide, including banking, government, messaging, gaming, retail, and Amazon products. AWS initially cited DynamoDB and later an internal load-balancer monitoring subsystem, while recovery required request limits and continued through the day. Policy experts argue the event exposes systemic dependence on Amazon, Microsoft, and Google. Commenters counter that genuine multi-region or multi-cloud resilience is expensive and should be calibrated to each service's actual criticality.

### Comment pulse

- Debate split between cloud diversification as systemic risk reduction and redundancy as costly overengineering for noncritical products.
- Critics noted that high-level managed services create deeper lock-in than ordinary virtual machines.
- Others distinguished national infrastructure sovereignty from a single company's rational availability tradeoffs.

### LLM perspective

- View: Concentration risk is real, but resilience spending should follow consequence, dependency depth, and recovery objectives.
- Impact: Failures in foundational managed services can propagate far beyond customers explicitly deployed in one region.
- Watch next: AWS's technical postmortem, regulatory response, and whether customers actually rehearse regional evacuation.
