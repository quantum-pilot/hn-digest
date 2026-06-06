# I returned to AWS and was reminded why I left

- Score: 636 | [HN](https://news.ycombinator.com/item?id=48073201) | Link: http://fourlightyears.blogspot.com/2026/05/i-returned-to-aws-and-was-reminded-hard.html

- TL;DR  
  - An early AWS evangelist recounts how years of annoyances—no official SDKs early on, slow Python 3 adoption, convoluted IAM, costly data egress, opaque intra‑AWS transfer billing, Lambda complexity/lock‑in, and hostility toward open‑source vendors—flipped him into a critic who mostly left AWS. Returning briefly to test Bedrock and a huge EC2 instance triggered a fraud alert that suspended his account, silently breaking his business email for days with poor support. HN debates whether AWS’s complexity, costs, and services like DynamoDB are justified or avoidable.

- Comment pulse  
  - Leaving is sticky → “free DTO” reportedly involves long forms, approvals and 60‑day waits, extending lock‑in—counterpoint: skeptics note these delays aren’t in policy.  
  - AWS and open source → critics say AWS monetized projects without support, driving restrictive licenses; others note forks like OpenSearch, Valkey followed, not caused, changes.  
  - AWS complexity and cost → some say critics aren’t target scale; others with large deployments report higher bills, painful Lambda/CloudWatch, and mixed experiences with DynamoDB.

- LLM perspective  
  - View: The story highlights cloud-as-utility vs. platform tension: convenience upfront, but compounding complexity, lock‑in, and support risk over time.  
  - Impact: Teams should quantify data egress, support expectations, and portability before adopting managed services like Lambda, Bedrock, or proprietary databases.  
  - Watch next: Expect more interest in simpler stacks (VMs, Postgres, Kubernetes) plus regulation or pressure on cloud exit fees and OSS compensation.
