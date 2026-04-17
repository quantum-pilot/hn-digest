# IPv6 traffic crosses the 50% mark

- Score: 767 | [HN](https://news.ycombinator.com/item?id=47777894) | Link: https://www.google.com/intl/en/ipv6/statistics.html?yzh=28197

### TL;DR
Google’s IPv6 stats now show more than half of user requests reaching it over IPv6, with clear weekly oscillations: higher usage on weekends, lower on workdays. Commenters note that mobile and residential networks (often IPv6 or IPv6+NAT64) are driving this, while enterprise and campus networks lag. Despite protocol support being ubiquitous, major platforms like GitHub and Twilio remain IPv4-only, and operational worries (IP-based access controls, NAT habits, unclear incentives) continue to slow full dual‑stack or IPv6‑first deployment.

---

### Comment pulse
- Big platforms still IPv4-only → GitHub, Twilio, ZScaler etc. lack IPv6, partly due to fear of breaking customers using IP allowlists—counterpoint: IP-based security is brittle anyway.  
- Adoption patterns → Mobile and residential networks lead; corporate/education lag, explaining Google’s weekend IPv6 spikes and apparent plateau that’s actually cyclical growth.  
- Technical framing → Tailscale’s FAQ praised; debate over NAT’s persistence, misuse of “successor” vs “alternative,” and omission of DHCPv6-PD as a clean way to delegate subnets.

---

### LLM perspective
- View: 50% user reachability is a behavioral milestone; the bottleneck is organizational risk-aversion, not protocol readiness.  
- Impact: SaaS vendors and enterprises must untangle IPv4-centric security, monitoring, and compliance, or they’ll block IPv6-heavy users and regions.  
- Watch next: IPv4 pricing hikes, government or large-operator IPv6-only pushes, and whether major holdouts quietly ship production-grade IPv6.
