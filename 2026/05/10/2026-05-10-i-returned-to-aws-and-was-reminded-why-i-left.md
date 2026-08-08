# I returned to AWS and was reminded why I left

- Score: 636 | [HN](https://news.ycombinator.com/item?id=48073201) | Link: http://fourlightyears.blogspot.com/2026/05/i-returned-to-aws-and-was-reminded-hard.html

### TL;DR

Longtime AWS advocate Andrew Stuart returned to benchmark Claude through Bedrock and code on a 192-core EC2 spot instance. The dormant account’s sudden activity triggered a suspected-breach restriction that disabled resource creation and his business WorkMail; after completing security steps, chat escalation, and four days of waiting, service remained blocked. The incident revived complaints about egress fees, opaque billing, IAM, Lambda lock-in, support, and service complexity. Commenters split: experienced operators confirmed high costs and migration friction, while defenders said complex workloads warrant complexity and specialized services require deliberate architectures.

### Comment pulse

- Departing users said “free” egress requires approval, detailed justification, and months of delay — counterpoint: one requested proof of an alleged 60-day wait.
- Open-source critics blamed AWS monetization for defensive relicensing; others corrected that OpenSearch and Valkey forks followed upstream license changes.
- IAM defenders called granular, auditable permissions inherently complex, while critics blamed inconsistent service-specific models and hostile console behavior.

### LLM perspective

- View: The failure was account-level blast radius: a protective control on compute disabled an unrelated critical email service.
- Impact: Bundling infrastructure and business communications under one provider turns fraud detection and support latency into continuity risks.
- Watch next: Recovery time, anomaly-detection appeals, service isolation options, support SLAs, WorkMail migration, quota approval, and total benchmark cost.
