# It seems that OpenAI is scraping [certificate transparency] logs

- Score: 184 | [HN](https://news.ycombinator.com/item?id=46274478) | Link: https://benjojo.co.uk/u/benjojo/h/Gxy2qrCkn1Y327Y6D3

### TL;DR

A newly issued certificate for `autoconfig.benjojo.uk` was followed almost immediately by an OAI-SearchBot request for `/robots.txt`, leading the author to infer that OpenAI monitors certificate-transparency logs to discover sites. The timing shows correlation, not the discovery path, although a commenter checked that the requester’s IP fell within OpenAI’s published crawler range. Readers noted that CT logs are intentionally public and routinely monitored by search engines, archives, security firms, and attackers; the event is therefore unsurprising, even if operationally revealing.

### Comment pulse

- Public CT records make newly certified hostnames discoverable even when no page links to them.
- Wildcard certificates can conceal individual subdomains — counterpoint: sharing one certificate enlarges compromise blast radius and requires DNS-based validation automation.
- Verifying crawler IP ranges distinguishes an authentic bot from imitators copying recognizable user-agent strings.

### LLM perspective

- View: The request plausibly came from OpenAI, but this single observation cannot prove CT logs were its discovery source.
- Impact: Operators should treat certificate names as public signals that can trigger immediate automated probing.
- Watch next: Repeated controlled certificates, timing distributions, alternative discovery channels, and published crawler behavior.
