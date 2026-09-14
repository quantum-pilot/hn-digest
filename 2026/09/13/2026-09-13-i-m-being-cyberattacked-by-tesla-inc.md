# I'm being cyberattacked by Tesla, Inc

- Score: 429 | [HN](https://news.ycombinator.com/item?id=49686766) | Link: https://dreamstation.systems/personal/tesla.html

### TL;DR

An NTP Pool volunteer observed more than 50,000 exploit-probe requests from AWS addresses carrying Assetnote identifiers and Tesla-related hostnames. He theorized Tesla’s pool-ntp subdomain, a CNAME to the volunteer-operated pool, caused an exposure scanner to misclassify rotating third-party IPs as Tesla assets. The probes reportedly caused no successful compromise. The post’s later update says Assetnote’s Patrik contacted the author and resolved the issue, strengthening scanner attribution while not establishing that Tesla directly initiated or controlled the traffic.

### Comment pulse

- Vendor DNS practices caused concern → NTP Pool guidance discourages default pool names and recommends dedicated vendor zones.
- Scanner providers should be contacted → Unauthorized targeting creates liability and is normally treated seriously by exposure-management companies.
- CNAME scope is risky → Pointing a corporate hostname at infrastructure outside company control can confuse ownership and certificate boundaries.

### LLM perspective

- View: The evidence fits an asset-discovery scope error, not a deliberate Tesla cyberattack.
- Impact: Automated security tooling can externalize aggressive probes onto volunteers when DNS aliases are mistaken for asset ownership.
- Watch next: Assetnote’s root-cause explanation, scope-validation changes, Tesla’s DNS correction, and recurrence across pool operators.
