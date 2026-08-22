# I accidentally logged hundreds of thousands of phone calls to military bases

- Score: 633 | [HN](https://news.ycombinator.com/item?id=49387570) | Link: https://lina.sh/blog/hijacking-e164-arpa

### TL;DR

A researcher bought expired `ns.enum.org.uk` for €5, unintentionally gaining DNS control over ENUM delegations for Saint Helena, Diego Garcia, and Ascension Island. Months later, logs showed hundreds of thousands of lookup queries, mainly for the two military-base territories, exposing reversed phone numbers, timestamps, and resolver IPs. The server returned NXDOMAIN, so it did not reroute traffic; a malicious operator could have supplied SIP routes. The researcher deleted logs, reported again, and eventually transferred the domain to Britain’s NCSC. Commenters cautioned queries may be internal-routing leakage, not confirmed calls.

### Comment pulse

- Telecom veterans disputed ENUM’s death → private and carrier-internal deployments still use its query format for routing and number portability.
- A likely alternative explanation emerged → unsupported international ranges may have leaked from private resolvers into public ENUM.
- Disclosure reactions mixed relief and concern → readers expected harsher treatment, while noting the researcher received neither payment nor reported recognition.

### LLM perspective

- View: The evidence establishes sensitive ENUM queries and routing control, not that completed phone calls were recorded or intercepted.
- Impact: One expired dependency exposed metadata and a potential call-redirection path for strategically important territories.
- Watch next: Delegation cleanup, expired-nameserver audits, query-source identification, confirmation of routing behavior, and formal vulnerability-response procedures.
