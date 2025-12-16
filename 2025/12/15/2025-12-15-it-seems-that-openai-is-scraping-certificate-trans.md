# It seems that OpenAI is scraping [certificate transparency] logs

- Score: 184 | [HN](https://news.ycombinator.com/item?id=46274478) | Link: https://benjojo.co.uk/u/benjojo/h/Gxy2qrCkn1Y327Y6D3

### TL;DR
OpenAI’s OAI-SearchBot hit a brand‑new subdomain’s `robots.txt` within seconds of a TLS certificate being issued, strongly implying it monitors certificate transparency (CT) logs to discover crawl targets. That’s not unusual: many actors—from search engines to security firms and scammers—systematically read CT logs, which are explicitly public and intended for broad auditing of certificates. Discussion centers on domain enumeration “leakage,” wildcard certificates as a partial mitigation with security tradeoffs, and frustration at people treating CT-based crawling as abusive rather than expected.

---

### Comment pulse
- CT logs are widely mined by Google, Archive.org, security tools, and criminals; they’re public by design for CA accountability, not secrecy.  
- Using wildcard certificates hides individual subdomains from CT, but concentrates risk: one compromised host exposes valid credentials for the entire domain.  
- Some scrapers spoof major crawler user‑agents, but this IP matches OpenAI’s published ranges; IP verification and published ranges help distinguish legit crawlers from imitators.

---

### LLM perspective
- View: CT-based discovery is now standard OSINT; operators should assume any certificate instantly exposes hostnames to global crawlers.  
- Impact: Service owners, especially with semi-private subdomains, must treat obscurity as non-security and reconsider wildcard versus per-subdomain certs.  
- Watch next: Industry norms around CT-friendly crawling, better “new-domain” feeds, and clearer publisher controls via robots, opt‑outs, and authenticated crawler lists.
