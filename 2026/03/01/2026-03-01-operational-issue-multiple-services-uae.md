# Operational issue – Multiple services (UAE)

- Score: 150 | [HN](https://news.ycombinator.com/item?id=47209781) | Link: https://health.aws.amazon.com/health/status

### TL;DR

AWS reported that objects struck a ME-CENTRAL-1 data center, causing sparks and fire; responders shut down utility and generator power in mec1-az2. EC2, EBS, databases and networking APIs degraded while services shifted traffic and customers restored resources elsewhere. Hours of partial recovery were followed by another localized power failure in mec1-az3, leaving mec1-az1 unable to accept launches and raising DynamoDB and S3 errors. AWS then recommended another Region. Hacker News focused on correlated physical failures, staff safety and the limits of zone-only redundancy.

### Comment pulse

- Early multi-zone redundancy protected many applications → the later loss of a second zone exposed correlated regional risk.
- Fire response legitimately cut every power source → equipment continuity yields to responder safety.
- Geographic separation improves resilience — counterpoint: cross-region designs add cost, latency, complexity and operational burden.

### LLM perspective

- **View:** Availability Zones reduce routine failures but cannot guarantee independence during regional physical events.
- **Impact:** Recovery plans need tested backups, spare regional capacity and procedures that avoid relying on impaired control-plane APIs.
- **Watch next:** Power restoration, resource-recovery sequencing and AWS's account of why surviving-zone launches and regional services degraded.
