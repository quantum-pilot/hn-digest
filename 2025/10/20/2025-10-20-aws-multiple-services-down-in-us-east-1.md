# AWS Multiple Services Down in us-east-1

- Score: 1549 | [HN](https://news.ycombinator.com/item?id=45640838) | Link: https://health.aws.amazon.com/health/status?ts=20251020

### TL;DR

This entry tracks the October 20 US-East-1 disruption through user reports, but its frozen AWS dashboard capture is dominated by later, unrelated regional incidents and therefore cannot reliably establish the original timeline or root cause. Contemporary comments describe prolonged failures across Redshift, Airflow, Lambda, networking, and consumer services, plus recovery that varied by product. One operator's multi-region failover was blocked because Identity Center itself depended on US-East-1, illustrating how centralized authentication can defeat otherwise redundant application architecture.

### Comment pulse

- Operators reported uneven recovery, control-plane failures, queued work, and difficulty measuring the remaining blast radius.
- A multi-region design failed operationally because its identity and credential path was still regional and circular.
- Consumer effects ranged from disabled retail discounts and smart-home commands to limited football officiating technology.

### LLM perspective

- View: Redundancy fails when control, identity, or recovery credentials retain a hidden single-region dependency.
- Impact: Teams need to test administrative failover, not merely replicate application data and compute.
- Watch next: AWS's preserved incident report and customer reviews of identity, DNS, and emergency-access dependencies.
