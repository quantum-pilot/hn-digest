# The Postmark backdoor that’s downloading emails

- Score: 214 | [HN](https://news.ycombinator.com/item?id=45395957) | Link: https://www.koi.security/blog/postmark-mcp-npm-malicious-backdoor-email-theft

### TL;DR

Security vendor Koi reports that npm's unofficial `postmark-mcp` package added a hidden BCC recipient in version 1.0.16, copying every sent email to a developer-linked domain after 15 apparently legitimate releases. The package impersonated an official Postmark repository name and was later removed, but installed copies remain. Koi advises removing affected versions, checking mail logs, and rotating exposed credentials. Its estimate of hundreds of organizations and thousands of daily emails is speculative; npm download counts do not measure unique active deployments.

### Comment pulse

- Commenters call this a familiar software supply-chain trust failure, intensified by autonomous tools holding email credentials.
- Others reject MCP exceptionalism and Koi's inflated impact arithmetic, while agreeing that default sandboxing remains inadequate.

### LLM perspective

- View: The malicious line was simple; unattended privilege and invisible dependency updates created the real leverage.
- Impact: Agent deployments need inventories, version controls, outbound monitoring, and narrowly scoped credentials before convenience scales exposure.
- Watch next: Confirmed victim counts, registry response, domain takedown, forensic disclosures, and permission-model improvements.
