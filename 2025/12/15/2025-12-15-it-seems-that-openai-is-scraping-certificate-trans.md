# It seems that OpenAI is scraping [certificate transparency] logs

- Score: 184 | [HN](https://news.ycombinator.com/item?id=46274478) | Link: https://benjojo.co.uk/u/benjojo/h/Gxy2qrCkn1Y327Y6D3

### TL;DR

Minutes after minting a TLS certificate, the author observed an OAI-SearchBot request for the new host’s robots.txt and inferred that OpenAI monitors certificate-transparency logs to discover crawl targets. A commenter checked that the source address fell within OpenAI’s published crawler range, supporting attribution, though the mechanism itself was not demonstrated. The discussion emphasizes that monitoring public CT logs is routine among search engines, archives, security firms, and attackers. Wildcard certificates obscure individual subdomains but increase key-compromise blast radius and require DNS-based issuance.

### Comment pulse

- CT logs are intentionally public → rapid discovery is expected behavior, not evidence of secret access.
- Wildcards hide hostnames but widen certificate exposure and complicate automation, making the privacy trade-off workload-specific.
- User agents alone are spoofable; source-range verification provided stronger attribution in this instance.

### LLM perspective

- View: The observation supports rapid certificate-triggered discovery, while the exact feed and crawler workflow remain inferred.
- Impact: A publicly certified hostname should be treated as immediately discoverable even without incoming links.
- Watch next: Compare issuance-to-request timing, crawler IP validation, robots compliance, and repeated versus newly observed domains.
