# Upcoming Changes to Let's Encrypt Certificates

- Score: 212 | [HN](https://news.ycombinator.com/item?id=46279241) | Link: https://community.letsencrypt.org/t/upcoming-changes-to-let-s-encrypt-certificates/243873

### TL;DR

Let’s Encrypt is rolling out a cross-signed Generation Y hierarchy comprising two new roots and six intermediates. The default classic profile switches May 13, 2026; the new intermediates omit TLS client-authentication usage, while a temporary tlsclient profile remains on Generation X through May. The tlsserver and shortlived profiles begin moving this week, bringing short-lived certificates and IP-address support to general availability. Driven by CA/Browser Forum requirements, optional 45-day certificates arrive in 2026, defaults fall from 90 to 64 days in 2027 and 45 in 2028; most users need do nothing.

### Comment pulse

- Critics feared monthly renewal burdens would retire legacy sites — counterpoint: automation advocates said ACME can reduce labor and multiple free providers enable redundancy.
- Commenters stressed the lifetime mandate came from browser and CA/Browser Forum policy, not a unilateral Let’s Encrypt decision.
- Short lifetimes aim to reduce dependence on broken revocation; skeptics raised Certificate Transparency storage growth and broader policy-ratcheting concerns.

### LLM perspective

- View: The hierarchy migration is routine compatibility work; lifetime compression is the operationally consequential change.
- Impact: Manual certificate workflows become untenable, pushing operators toward ACME, managed hosting, monitoring, and CA failover.
- Watch next: Generation Y compatibility, client-auth migration, 45-day testing, automation failures, CT-log capacity, and legacy-site attrition.
