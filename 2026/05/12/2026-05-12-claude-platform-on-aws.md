# Claude Platform on AWS

- Score: 218 | [HN](https://news.ycombinator.com/item?id=48103042) | Link: https://claude.com/blog/claude-platform-on-aws

## TL;DR
Claude Platform on AWS is a new way to use Anthropic’s full Claude Platform while tying access, identity, and billing into an organization’s existing AWS setup. Unlike Claude on Amazon Bedrock (where AWS runs the service and data stays inside AWS), Anthropic itself operates this new platform and processes data outside the AWS boundary, but it still uses AWS IAM, CloudTrail, and consolidated AWS invoices. HN commenters focus on naming confusion, procurement/billing benefits, and tradeoffs with Bedrock’s stricter data-residency model.

---

## Comment pulse
- Naming is confusing → “on AWS” but data processed outside AWS; practically it lets enterprises route AI spend and IAM/SSO through AWS — counterpoint: muddies Bedrock’s clear data-governance story.  
- Capabilities vs Bedrock → this exposes full Claude Platform (agents, tools, console) vs just models; some unsure if benefits justify refactoring from Bedrock or fit with credits.  
- Data and regions → Bedrock keeps AWS as data processor for strict residency; this new option doesn’t, and people question whether EU-based inference is supported.

---

## LLM perspective
- View: This is mainly a distribution and procurement play, not a new model, but important for serious enterprise adoption.  
- Impact: Security, finance, and compliance teams gain fewer blockers; startups with AWS-centric stacks may still prefer Bedrock’s multi-model flexibility.  
- Watch next: Clearer regional inference options (EU), Terraform/CloudFormation resources, and benchmarks comparing latency, throughput, and reliability vs Bedrock.
