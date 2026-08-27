# We pwned X, Vercel, Cursor, and Discord through a supply-chain attack

- Score: 508 | [HN](https://news.ycombinator.com/item?id=46317098) | Link: https://gist.github.com/hackermondev/5e2cdc32849405fff6b46957747a2d28

### TL;DR

A researcher says Mintlify’s shared documentation infrastructure let one customer’s static SVG be served through another customer’s domain. Because directly opened SVG files can execute embedded JavaScript, the missing subdomain check enabled cross-site scripting on domains including Discord and reportedly many other Mintlify customers. Discord temporarily closed its developer docs and reverted platforms; Mintlify worked with researchers on remediation. The disclosed team received about $11,000 in bounties. Specific account-takeover consequences discussed by commenters were partly hypothetical and depended on each site’s protections.

### Comment pulse

- Commenters considered the rewards too small relative to the claimed cross-customer reach and potential abuse.
- Security discussion stressed SVG sanitization, origin isolation, secure HTTP-only cookies, CSP, and auditing third-party infrastructure.
- Some blamed AI-startup practices; others argued complex shared dependencies, rather than AI specifically, created the systemic exposure.

### LLM perspective

- View: The core failure was tenant isolation across trusted customer origins, with script-capable SVG turning it into XSS.
- Impact: A documentation vendor flaw can inherit customers’ domain trust and multiply one bug across many organizations.
- Watch next: Customers should verify patch coverage, origin separation, token exposure, CSP effectiveness, and any evidence of prior exploitation.
