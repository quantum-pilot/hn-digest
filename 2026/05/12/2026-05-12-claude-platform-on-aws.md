# Claude Platform on AWS

- Score: 218 | [HN](https://news.ycombinator.com/item?id=48103042) | Link: https://claude.com/blog/claude-platform-on-aws

### TL;DR

Claude Platform on AWS is generally available, exposing Anthropic’s native API through AWS IAM, CloudTrail, consolidated billing, and spend commitments, with same-day models, features, and betas. It includes Managed Agents, Advisor, web tools, code execution, Files, Skills, MCP, caching, citations, batches, and Console eval tools. Unlike Bedrock, Anthropic operates this service and processes data outside the AWS boundary; Bedrock retains AWS as processor for residency needs. Commenters saw procurement and feature parity as the main benefits but found the branding confusing and questioned migration, credits, throughput, operations, and EU inference.

### Comment pulse

- Enterprises can reuse IAM, SSO, FinOps, contracts, invoices, and commitment discounts instead of establishing separate Anthropic procurement rails.
- Startups questioned whether AWS credits apply and whether added features justify refactoring from Bedrock’s multimodel interface.
- Native features arrive immediately — counterpoint: Bedrock offers clearer AWS-bound governance and potentially stronger operational reliability.

### LLM perspective

- View: This is an AWS access and commercial wrapper around Anthropic-operated infrastructure, not a new residency option.
- Impact: Procurement-heavy organizations gain faster adoption, but reviews must distinguish two similarly named data-processing paths.
- Watch next: EU inference, credit eligibility, Terraform support, throughput, uptime, pricing parity, and private-offer discounts.
