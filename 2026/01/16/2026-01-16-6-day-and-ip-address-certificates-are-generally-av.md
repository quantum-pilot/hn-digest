# 6-Day and IP Address Certificates Are Generally Available

- Score: 311 | [HN](https://news.ycombinator.com/item?id=46647491) | Link: https://letsencrypt.org/2026/01/15/6day-and-ip-general-availability

### TL;DR

Let’s Encrypt now offers opt-in certificates valid for 160 hours and certificates for IPv4 and IPv6 addresses. Short lifetimes reduce exposure after key compromise because revocation is unreliable; IP certificates must be short-lived because addresses change hands faster than domains. Default lifetimes will separately fall from 90 to 45 days. HN readers highlighted uneven client support—Certbot work remains incomplete while lego and several alternatives work—and debated renewal scheduling, self-hosted DNS-over-HTTPS on iOS, and possible .onion support.

### Comment pulse

- Client support is fragmented → lego, acme.sh, Caddy, Traefik, acmez, and cert-manager work; Certbot remains under development.
- The 160-hour lifetime distributes renewals across weekdays → counterpoint: fixed weekly schedules may simplify failure monitoring.
- IP certificates unlock some self-hosted iOS DoH setups → reverse proxies with domain certificates already satisfy other users.

### LLM perspective

- View: Short-lived certificates trade revocation dependence for automation discipline.
- Impact: Operators gain IP-native TLS, but brittle renewal pipelines become unacceptable.
- Watch next: Certbot support, renewal-rate limits, and adoption of ACME certificates for .onion services.
