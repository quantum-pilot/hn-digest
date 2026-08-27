# Reverse engineering a $1B Legal AI tool exposed 100k+ confidential files

- Score: 437 | [HN](https://news.ycombinator.com/item?id=46137514) | Link: https://alexschapiro.com/security/vulnerability/2025/12/02/filevine-api-100k

### TL;DR

A researcher reports finding a Filevine-linked subdomain whose frontend exposed an unauthenticated recommendation endpoint. By reconstructing its request format from minified JavaScript, he received a fully scoped Box administrator token for a law firm’s filesystem. A search for “confidential” returned nearly 100,000 results; he stopped testing and disclosed the issue. Filevine acknowledged the report, confirmed remediation by November 21, and supported later publication. The incident combined a public endpoint with excessive token privilege, creating a potentially institution-wide confidentiality breach.

### Comment pulse

- Readers defended naming Filevine after remediation → customers deserve disclosure, and technical details help other vendors find similar errors.
- Slow response often reflects ownership and approval bottlenecks → commenters still considered this exposure urgent enough for immediate escalation.
- Several rejected an AI-specific diagnosis → ordinary SaaS integration failures caused the bug, though centralized document access enlarged its blast radius.

### LLM perspective

- View: An unauthenticated endpoint should never mint credentials broader than the single operation a user requested.
- Impact: Legal clients face exposure across privileged communications, regulated records, and court-controlled documents from one integration mistake.
- Watch next: Vendors should audit token scope, public subdomains, secret-bearing responses, revocation logs, and disclosure escalation paths.
