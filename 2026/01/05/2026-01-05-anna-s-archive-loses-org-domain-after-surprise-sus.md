# Anna's Archive loses .org domain after surprise suspension

- Score: 633 | [HN](https://news.ycombinator.com/item?id=46497164) | Link: https://torrentfreak.com/annas-archive-loses-org-domain-after-surprise-suspension/

### TL;DR
Anna’s Archive’s primary .org domain was abruptly placed in “serverHold” by the .org registry, removing it from DNS while the site remains reachable via several alternative TLDs. Because .org suspensions are rare and Public Interest Registry won’t comment, many infer a court order, possibly tied to earlier WorldCat scraping or its recent 300‑TB Spotify backup, though that’s unproven. HN discussion centers on DNS and PKI as chokepoints, and the case for Tor, .onion, and other decentralized naming.

---

### Comment pulse
- ServerHold is registry‑level and usually follows court or law‑enforcement orders, not discretionary abuse handling → suggests formal legal action behind the suspension.  
- DNS and TLS PKI are viewed as centralized censorship levers → calls to migrate to GNU Name System, Tor, IPFS, etc. — counterpoint: states can still block IPs.  
- Users ask why no .onion/Yggdrasil addresses → onion domains increase resilience but Tor’s very poor download speeds limit usefulness for large media libraries.

---

### LLM perspective
- View: This is a concrete example of infrastructure providers becoming de‑facto policy enforcers, even in namespaces (.org) once seen as reluctant censors.  
- Impact: Shadow libraries will double down on multi‑TLD, onion, and p2p addressing; ordinary users learn that domain names are fragile identifiers.  
- Watch next: Look for published injunctions, parallel actions against other TLDs, and whether major archives standardize on onion/IPFS mirrors as “primary” endpoints.
