# Operational issue – Multiple services (UAE)

- Score: 150 | [HN](https://news.ycombinator.com/item?id=47209781) | Link: https://health.aws.amazon.com/health/status

### TL;DR
An AWS availability zone in the ME-CENTRAL-1 (UAE) region went down after external objects struck a data center, causing sparks and fire. Fire crews cut power, including generators, and AWS is waiting for permission to re-energize, with recovery estimated to take hours. Other AZs in the region remain operational, so customers architected across multiple AZs are largely unaffected. The discussion focuses on physical risk to data centers, cloud high-availability assumptions, and whether DCs could become deliberate military targets.

### Comment pulse
- This incident validates multi-AZ design → apps spread across AZs continued running; single-AZ workloads lost access.  
- Data centers as wartime targets → easier to bomb 50 DCs than hack thousands of services — counterpoint: cloud still has logical single points of failure.  
- Physical safety vs uptime → AWS must weigh restoring service against risk of repeated strikes and on-site staff safety.

### LLM perspective
- View: Treat AZs as failure domains vulnerable to physical events; design for region-level or multi-cloud redundancy for critical services.
- Impact: Enterprises with single-AZ deployments in ME-CENTRAL-1 face downtime; SREs and architects will revisit resilience assumptions.
- Watch next: AWS post-incident report, changes to regional design, and any industry guidance on data centers as potential conflict targets.
