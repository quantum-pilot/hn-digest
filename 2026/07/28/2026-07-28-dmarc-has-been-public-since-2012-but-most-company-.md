# DMARC has been public since 2012 but most company domains still don't enforce it

- Score: 173 | [HN](https://news.ycombinator.com/item?id=49081783) | Link: https://ciphercue.com/blog/dmarc-enforcement-gap-rua-fragmentation-2026

### TL;DR
DMARC, a 2012 standard that lets domains tell receivers what to do with unauthenticated mail (none/quarantine/reject), is still weakly deployed. In CipherCue’s dataset of 67k company domains, 45% have no DMARC record and another 23% sit forever at “p=none” (monitor-only), so 68% don’t actually enforce. The main blocker isn’t the DNS change but the messy research task of mapping DMARC reports to real senders. HN comments debate DMARC’s value for spam vs impersonation, operational pain, and whether email itself is fundamentally broken.

---

### Comment pulse
- DMARC doesn’t stop most spam/phishing → it authenticates domain use, not trustworthiness; content filters still decide inbox placement — counterpoint: strong auth creates accountability and raises spammer costs.  
- Admins see many SPF/DKIM errors from large firms → strict enforcement risks lost mail; some use hardline policies to pressure misconfigured senders into fixing setups.  
- For non-mail domains, lock everything down → SPF `-all`, DMARC `p=reject`, strict alignment, null MX and restricted subdomains to prevent abusive spoofing.

---

### LLM perspective
- View: Biggest gap is analysis of DMARC reports, not standards; automation that clusters senders and suggests policies is ripe for LLMs.  
- Impact: Default “secure-by-default” DNS templates at registrars/hosters would likely dwarf individual tuning in real-world protection.  
- Watch next: Tools that ingest rua XML, identify legit vendors, and safely propose moving from `p=none` to `quarantine`/`reject` with rollback options.
