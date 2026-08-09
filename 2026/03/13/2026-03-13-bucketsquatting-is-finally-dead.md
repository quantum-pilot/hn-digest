# Bucketsquatting is finally dead

- Score: 301 | [HN](https://news.ycombinator.com/item?id=47361913) | Link: https://onecloudplease.com/blog/bucketsquatting-is-finally-dead

### TL;DR

AWS has introduced account-regional S3 bucket names, embedding an AWS account ID and region so only that account can create the bucket there. This closes the deletion-and-reclaim path behind bucketsquatting for newly created names, and organizations can enforce the namespace with an SCP. It is not retroactive: existing globally named buckets need migration. HN readers welcomed the safer default but noted operational wrinkles, debated random suffixes, and compared the problem with Azure accounts, package registries, and usernames.

### Comment pulse

- IaC users already append random identifiers → secure defaults make that defensive convention enforceable instead of optional.
- Namespace safety shifts risk into account governance → root-email ownership and MFA recovery remain consequential operational concerns.
- Cloud comparisons need precision → Azure still exposes a global account-name pool; GCS supports domain verification for domain-formatted buckets.

### LLM perspective

- **View:** This is a clean capability-based namespace design, provided teams actually migrate.
- **Impact:** Platform teams gain a policy control; attackers lose predictable orphaned-name takeovers.
- **Watch next:** Adoption rates, migration tooling, and whether Azure offers equivalent tenant-bound naming.
