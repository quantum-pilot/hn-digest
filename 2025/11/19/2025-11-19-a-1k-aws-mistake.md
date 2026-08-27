# A $1k AWS mistake

- Score: 267 | [HN](https://news.ycombinator.com/item?id=45977744) | Link: https://www.geocod.io/code-and-coordinates/2025-11-18-the-1000-aws-mistake/

### TL;DR

Geocodio moved large datasets between S3 and EC2 in one region, expecting the transfer itself to be free. Because its private-subnet traffic followed the default route through an AWS NAT Gateway, one day processed about 20TB and generated $907.53 in charges. Adding a free S3 Gateway Endpoint to the relevant VPC route tables bypassed the gateway. Cost Anomaly Detection limited the damage. The broader lesson is to test actual routing and billing with small volumes before scaling, not infer total cost from service-transfer pricing alone.

### Comment pulse

- Readers debated making S3 endpoints default, noting cross-region behavior and security boundaries can make that unsafe.
- Several shared much larger surprise bills and criticized delayed alerts and the absence of simple hard spending caps.

### LLM perspective

- View: Cloud cost is an architectural property of the route taken, not just the source and destination.
- Impact: A single implicit network hop can turn nominally free service traffic into a material operating expense.
- Watch next: Route-level cost tests and anomaly alerts should become deployment checks for high-volume data paths.
