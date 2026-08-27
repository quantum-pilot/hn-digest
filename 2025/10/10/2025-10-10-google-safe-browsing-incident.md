# Google Safe Browsing incident

- Score: 186 | [HN](https://news.ycombinator.com/item?id=45538760) | Link: https://www.statichost.eu/blog/google-safe-browsing/

### TL;DR

StaticHost's shared `statichost.eu` domain received a Google Safe Browsing warning after phishing subdomains appeared, blocking access for roughly six hours and sometimes affecting customers' custom domains. The founder removed the offending sites and requested review; Google lifted the warning within hours. Rather than calling the detection erroneous, the post questions how much power a single service has over reachability. StaticHost moved new user sites to `statichost.page` and sought Public Suffix List recognition to isolate tenant reputations.

### Comment pulse

- Many readers said Safe Browsing correctly reacted to real phishing on a shared registrable domain.
- Others recommended independent monitoring because ISPs, antivirus products, and network filters can impose similar blocks.

### LLM perspective

- View: This was collateral damage from shared-domain reputation, not clearly a false-positive phishing judgment.
- Impact: Multi-tenant hosts inherit platform-wide abuse risk unless browsers can recognize tenant boundaries.
- Watch next: Public Suffix List acceptance and abuse-response controls will determine whether future incidents stay isolated.
