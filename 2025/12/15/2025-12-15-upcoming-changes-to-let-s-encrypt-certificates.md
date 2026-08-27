# Upcoming Changes to Let's Encrypt Certificates

- Score: 212 | [HN](https://news.ycombinator.com/item?id=46279241) | Link: https://community.letsencrypt.org/t/upcoming-changes-to-let-s-encrypt-certificates/243873

### TL;DR

Let’s Encrypt will introduce cross-signed Generation Y roots and intermediates, end TLS client-authentication support in its default hierarchy, and gradually shorten certificate lifetimes. The classic profile switches hierarchies on May 13, 2026; a temporary tlsclient profile remains available until then. Short-lived and IP-address certificates become generally available through opt-in profiles. Early adopters can test 45-day certificates in 2026, defaults fall to 64 days in 2027 and 45 in 2028, following CA/Browser Forum requirements rather than a unilateral Let’s Encrypt decision.

### Comment pulse

- Short lifetimes push ACME automation and reduce reliance on broken revocation — legacy sites may instead fail or disappear.
- Critics fear operational and transparency-log load; others note multiple free ACME providers reduce Let’s Encrypt concentration.
- The staged timeline provides years for testing, making manual annual renewal the immediate process to replace.

### LLM perspective

- View: Automation becomes part of certificate correctness, not an optional convenience, once renewal windows halve.
- Impact: Legacy operators face migration work while managed platforms and ACME-native servers absorb most changes automatically.
- Watch next: Generation Y compatibility, client-auth migrations, renewal monitoring, CA failover, CAA settings, and CT capacity.
