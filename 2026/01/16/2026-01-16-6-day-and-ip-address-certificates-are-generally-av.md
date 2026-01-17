# 6-Day and IP Address Certificates Are Generally Available

- Score: 311 | [HN](https://news.ycombinator.com/item?id=46647491) | Link: https://letsencrypt.org/2026/01/15/6day-and-ip-general-availability

## TL;DR
Let’s Encrypt now offers generally available 160‑hour “short‑lived” TLS certificates and IP address certificates (IPv4/IPv6), obtained by selecting a special ACME profile. Short lifetimes reduce reliance on broken revocation and shrink the damage window for leaked keys; IP certs must be short‑lived because IP ownership changes quickly. Defaults will still be 90 days for now, stepping down to 45. HN discussion centers on tooling support, iOS DoH quirks, renewal scheduling, and future hopes for .onion certificates.

## Comment pulse
- ACME client support for IP certs is uneven; lego, acme.sh, Caddy, Traefik, cert-manager work now, while certbot support remains pending.  
- Short 160‑hour lifetimes raise scheduling questions; some want 8‑day cycles, but 6‑ish days spreads renewal load evenly across weekdays.  
- IP certs enable self‑hosted DoH on iOS, which demands certs for FQDN and IP — counterpoint: some succeed using reverse proxies and custom domains.  

## LLM perspective
- View: Short‑lived and IP certs push the ecosystem toward automation, continuous validation, and reduced trust in revocation infrastructure.  
- Impact: Best suited to operators already using robust ACME automation; manual or brittle setups may struggle with 6‑day renewals.  
- Watch next: certbot IP support, browser attitudes to shorter maximum lifetimes, and whether major CAs adopt similar short‑lived offerings.
