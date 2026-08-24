# Major European payment processor can't send email to Google Workspace users

- Score: 432 | [HN](https://news.ycombinator.com/item?id=46989217) | Link: https://atha.io/blog/2026-02-12-viva

### TL;DR

Viva.com’s account-verification messages omit a Message-ID header, causing Google Workspace to reject them before spam filtering. A personal Gmail address worked, but support treated the workaround as proof no defect existed. RFC 5322 labels Message-ID SHOULD rather than MUST because submission servers may add it, yet Google enforces it and production mail tooling normally supplies it automatically. The author argues this small compatibility failure matters for a business payments provider with limited Greek-market alternatives. Commenters debated standards wording but agreed ignored bounces and absent escalation were the larger operational failures.

### Comment pulse

- Standards readers stressed SHOULD permits exceptions—counterpoint: automated production senders need a deliberate reason, and receiver rules determine practical deliverability.
- Former email operators found ignored Workspace bounces less defensible than the missing header; delivery compatibility matters more than theoretical standards purity.
- Broken plain-text MIME parts illustrated a wider pattern: transactional email pipelines often satisfy nominal formats while failing actual user workflows.

### LLM perspective

- View: The header bug is trivial; failure detection, ownership, and escalation reveal the deeper reliability gap.
- Impact: Businesses may abandon preferred domains or processors; support workarounds conceal affected users from engineering metrics.
- Watch next: Add Message-ID, audit bounce handling, test major providers, fix MIME alternatives, and publish compatibility status.
