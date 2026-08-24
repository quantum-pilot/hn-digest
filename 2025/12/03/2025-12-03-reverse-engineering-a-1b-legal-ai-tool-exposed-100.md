# Reverse engineering a $1B Legal AI tool exposed 100k+ confidential files

- Score: 437 | [HN](https://news.ycombinator.com/item?id=46137514) | Link: https://alexschapiro.com/security/vulnerability/2025/12/02/filevine-api-100k

### TL;DR

By enumerating a Filevine subdomain and inspecting its minified client code, the researcher found an unauthenticated API that returned what appeared to be a fully scoped Box administrator token for a law firm. A search for confidential material produced nearly 100,000 results; testing stopped immediately, without reported extraction. Filevine acknowledged the October 27 disclosure, confirmed remediation on November 21, and cooperated with publication. Discussion stresses least privilege and vendor diligence, while noting the flaw was a conventional SaaS integration failure, not inherently an AI bug.

### Comment pulse

- Naming supports responsible disclosure → counterpoint: one reader argues cooperative remediation should earn vendor anonymity after a detailed technical writeup.
- Patch latency often reflects bureaucracy → ownership discovery, triage queues, approvals, and incentives can wrap a small code change in weeks.
- Centralized legal data magnifies ordinary mistakes → one over-privileged integration token can expose institutional memory across many clients.

### LLM perspective

- View: The failure chain was basic: discoverable endpoint, missing authentication, excessive token scope, and no blast-radius containment.
- Impact: Law firms need evidence of vendor IAM, isolation, logging, and incident response before centralizing sensitive files.
- Watch next: Confirm token revocation, access-log review, client notification, independent audit, and redesigned least-privilege scopes.
