# IP Crawl: Living atlas of open webcams discovered on the public internet

- Score: 203 | [HN](https://news.ycombinator.com/item?id=48700834) | Link: https://ipcrawl.com/

### TL;DR

IP Crawl is an open-source catalog of thousands of internet-exposed webcams found through Shodan, offering live or cached previews, filters, a map, statistics, random viewing, an API, and a self-check for visitors’ IPs. A daily pipeline deduplicates, blocklists, stores screenshots, and prunes stale entries; the stated goal is zero exposed cameras. HN found the exposure alarming but disputed whether republishing streams helps remediation or magnifies voyeurism, tracing failures to UPnP, hurried installers, confusing defaults, and users who cannot reasonably assess firewall or authentication risks.

### Comment pulse

- Exposure is not informed consent → an unlocked feed may be technically public while occupants still reasonably expect privacy inside homes.
- Remote-access convenience creates structural risk → UPnP or contractors can bypass NAT so nontechnical owners receive working products without understanding exposure.
- Security UX should add deliberate friction → public sharing must never be a default or accidental outcome — counterpoint: catalog visibility can reveal misconfiguration.

### LLM perspective

- **View:** Discovery and publication are different ethical acts; aggregating obscure endpoints materially increases their audience and abuse potential.
- **Impact:** Camera owners and unaware bystanders bear privacy risk; vendors and installers gain evidence that secure defaults are failing.
- **Watch next:** Measure owner notifications, removals, recurrence, blocked private spaces, and whether the self-check reaches affected users rather than spectators.
