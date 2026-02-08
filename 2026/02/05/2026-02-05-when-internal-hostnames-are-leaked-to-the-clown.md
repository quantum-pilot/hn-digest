# When internal hostnames are leaked to the clown

- Score: 448 | [HN](https://news.ycombinator.com/item?id=46895972) | Link: https://rachelbythebay.com/w/2026/02/03/badnas/

- TL;DR  
  - An off-the-shelf NAS used Sentry for client-side error logging, unintentionally sending its internal hostname to Sentry’s cloud, which then attempted outbound requests back to that host. HN commenters clarify this isn’t certificate transparency leakage but Sentry’s tracing behavior, note the SSRF-like risk of making Sentry probe arbitrary IPs, and debate whether internal hostnames are actually sensitive. Mitigations discussed include blocking telemetry at DNS/proxy level, hardening home networks with filters and CSP, or avoiding proprietary NAS firmware entirely.  
  *Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - Issue is Sentry traces, not CT logs → Sentry reads Host, then its servers call that host, enabling semi-blind SSRF-style probing. — counterpoint: confusing blog.  
  - Some argue internal hostnames aren’t private since DNS, certs, etc. leak them; better hide sensitive info in HTTPS paths, not subdomains.  
  - Defenses suggested: block Sentry via Pi-hole/AdGuard, use uBlock, or front NAS with Nginx adding strict CSP and referrer policies plus private TLS.

- LLM perspective  
  - View: Telemetry from appliances often exfiltrates internal metadata; treat every internet-connected box as untrusted and assume logs include hostnames and URLs.  
  - Impact: Home and small-office users on vendor firmware are exposed; they lack visibility into trackers and can’t easily control outbound telemetry.  
  - Watch next: Measure how consumer devices send hostnames or URLs to monitoring SaaS, and whether vendors offer local-only or opt-out logging modes.
