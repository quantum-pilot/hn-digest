# Tenda firmware (multiple versions) contains hidden authentication backdoor

- Score: 343 | [HN](https://news.ycombinator.com/item?id=48825749) | Link: https://kb.cert.org/vuls/id/213560

### TL;DR
Researchers found multiple Tenda router firmware versions contain a hidden authentication backdoor: a hardcoded password that works with any username, yielding admin access. The same credential (“rzadmin”) appears unchanged in earlier public analyses, suggesting years of vendor inaction. Commenters debate whether this is malice or a leftover developer credential, but agree it destroys trust in black-box consumer routers. Many advocate OpenWRT or custom setups, while noting trade-offs in Wi‑Fi features, performance, and energy efficiency versus closed, cheap hardware.

*Content unavailable; summarizing from title/comments.*

### Comment pulse
- Tenda backdoor uses hardcoded password “rzadmin” with any username → trivial admin login; likely a forgotten dev credential, unchanged for years.  
- Brand discussion → Tenda is long-standing, cheap, popular in Asia and via ISPs; commenters see low quality, poor security culture, but not clear state control.  
- Security reactions → some now insist on OpenWRT-only routers; others note missing MIMO/beamforming and >1Gbit support, so security must also live beyond the gateway.  

### LLM perspective
- View: Hardcoded router credentials are systemic; vendor incentives prioritize features and low cost over secure development, transparency, and independent audits.  
- Impact: Households, small businesses, and ISPs deploying cheap CPE risk silent compromise of networks via a single, unchangeable hidden login.  
- Watch next: IoT security rules, router security labels, third-party firmware audits, and open firmware that fully supports modern Wi‑Fi features.
