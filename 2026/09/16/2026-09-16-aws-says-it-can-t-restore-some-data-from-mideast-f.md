# AWS says it can't restore some data from mideast facilities struck by Iran

- Score: 438 | [HN](https://news.ycombinator.com/item?id=49719249) | Link: https://www.wsj.com/world/middle-east/aws-says-it-cant-restore-some-data-from-mideast-facilities-struck-by-iran-ddcb7e5d

### TL;DR

AWS says some customer data stored in Persian Gulf facilities struck by Iranian drones cannot be restored. Data centers in the UAE and Bahrain have remained mostly offline since attacks during the opening of the U.S.-Iran war, with damage spanning multiple Bahrain facilities; the announcement indicates data kept only in those locations may be permanently lost. HN discussion separated provider infrastructure from customer disaster-recovery choices: service tiers differ, cross-region copies require deliberate design, and local data-residency rules can conflict with geographic resilience.

### Comment pulse

- Redundancy claims require scope → surviving one building differs from simultaneous facility losses, and cheaper storage may not replicate across failure domains.
- Disaster recovery remains shared responsibility → customers must select multi-zone or multi-region architectures and regularly verify recovery procedures.
- Residency mandates can increase correlated risk → keeping all copies inside one jurisdiction may sacrifice resilience for legal control.

### LLM perspective

- View: Physical attacks expose the difference between cloud durability marketing and an application’s configured failure boundaries.
- Impact: Regulated customers face the hardest trade-off when cross-border replicas are restricted or prohibited.
- Watch next: AWS should disclose affected services, durability tiers, availability-zone scope, recoverable metadata, and customer remediation options.
