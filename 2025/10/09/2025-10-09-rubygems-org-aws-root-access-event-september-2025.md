# Rubygems.org AWS Root Access Event – September 2025

- Score: 228 | [HN](https://news.ycombinator.com/item?id=45530832) | Link: https://rubycentral.org/news/rubygems-org-aws-root-access-event-september-2025/

### TL;DR

Ruby Central says a former maintainer retained access to a shared AWS root credential after production access was revoked because the organization failed to rotate the password and MFA. An unauthorized actor changed the root password on September 19, altered IAM permissions, later inspected accounts, and accessed credentials before Ruby Central recovered the account on September 30. Ruby Central reports no evidence of changed gems, exposed user or financial data, database access, CI/CD impact, or downtime. It rotated credentials, added monitoring, reviewed IAM, commissioned an audit, and revised departure procedures.

### Comment pulse

- Readers questioned whether available logging can substantiate supply-chain integrity after eleven days of root control.
- Others urged restraint around attribution and requested fuller context amid the broader governance dispute.

### LLM perspective

- View: The primary control failure was treating access removal as vault revocation instead of rotating every shared root secret.
- Impact: Even without observed tampering, unverifiable privileged access damages confidence in a critical package registry.
- Watch next: Independent audit findings, artifact-integrity verification, logging architecture, formal operator controls, and any attributed response.
