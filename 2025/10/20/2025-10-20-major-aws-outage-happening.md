# Major AWS Outage Happening

- Score: 1070 | [HN](https://news.ycombinator.com/item?id=45640772) | Link: https://old.reddit.com/r/aws/comments/1obd3lx/dynamodb_down_useast1/

### TL;DR

A live Reddit operator thread chronicled the early US-EAST-1 AWS incident, beginning with reports that DynamoDB’s endpoint was not resolving and followed by AWS acknowledgements of elevated errors. Participants then reported cascading trouble across services including SQS, Lambda, Kinesis, API Gateway, IAM, STS, ECR, and Secrets Manager, plus many dependent applications. Some workloads failed over while others remained exposed through regional or control-plane dependencies. Because this was contemporaneous discussion, its service reports and DNS diagnosis were provisional rather than a final incident account.

### Comment pulse

- Operators compared multi-region designs, noting that failover can still depend on shared identity, control-plane, or deployment services.
- Anecdotes ranged from broken cloud applications to Alexa, Ring, and school-device failures; they were not independently verified.

### LLM perspective

- View: The thread shows how a foundational endpoint failure can reveal hidden dependencies far beyond one advertised service.
- Impact: Recovery plans need independent control paths, not merely duplicated application data and compute.
- Watch next: Reconcile early reports with AWS’s postmortem, especially the trigger, propagation path, and delayed status visibility.
