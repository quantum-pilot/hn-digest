# Today is when the Amazon brain drain sent AWS down the spout

- Score: 209 | [HN](https://news.ycombinator.com/item?id=45649178) | Link: https://www.theregister.com/2025/10/20/aws_outage_amazon_brain_drain_corey_quinn/

- TL;DR
  - Corey Quinn argues AWS’s US‑EAST‑1 meltdown traced to DNS resolution for the DynamoDB endpoint, cascading across “foundational” services. Beyond “it’s always DNS,” he blames Amazon’s brain drain—layoffs, high regretted attrition, and RTO—hollowing out tribal knowledge, slowing detection and recovery; the status page lagged reality. He recalls Justin Garrison’s LSE warnings and predicts more incidents as leaner teams face old edge cases. HN weighs whether AWS’s incident response met expectations and whether executive incentives now prioritize optics and cost-cutting over resilience.

- Comment pulse
  - Talent drain harms ops → layoffs, RTO, homogenized mediocrity; firms optimize stock, not resilience. — counterpoint: Markets rewarded layoffs and outage with share gains.
  - Recovery cadence skepticism → apparent progress matched US West start-of-day; pre-dawn updates were boilerplate.
  - 75-minute diagnosis debate → some call it strong for complex infra; others expect faster from AWS SREs.

- LLM perspective
  - View: Centralized control-plane and foundational-service dependencies magnify blast radius; automation helps, but missing operators with context stretch MTTR.
  - Impact: Regulated sectors, gaming, retail relying on us-east-1 face SLA breaches; incident postmortems will drive multi-region refactors.
  - Watch next: AWS postmortem on DNS/DynamoDB coupling, status-page SLAs, staffing; customer uptake of Route 53 health checks and cross-region failover.
