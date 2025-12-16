# Upcoming Changes to Let's Encrypt Certificates

- Score: 212 | [HN](https://news.ycombinator.com/item?id=46279241) | Link: https://community.letsencrypt.org/t/upcoming-changes-to-let-s-encrypt-certificates/243873

- TL;DR  
  - Let’s Encrypt is rolling out a new “Generation Y” root/intermediate hierarchy, deprecating TLS client-auth certificates, and preparing for industry-mandated shorter lifetimes. Classic-profile users switch to Gen‑Y in May 2026; short-lived and tlsserver profiles move sooner and gain official IP-address certificates. Driven by CA/Browser Forum rules, lifetimes will fall from 90 to 64 days in 2027, then 45 in 2028. HN discussion centers on automation burdens, centralization risks, CT log scaling, and whether this security ratchet is worth the complexity.

- Comment pulse  
  - Certificate lifetime cut driven by CA/Browser rules, not Let's Encrypt; critics fear legacy sites will die without automation — counterpoint: ACME-based renewal should reduce labor.  
  - Some see this as security policy ratcheting like password rotation; they argue owners should choose lifetimes, not browsers and CAs enforcing ever-shorter defaults.  
  - Others worry about CT log growth and Let's Encrypt centralization; defenders note multiple free ACME CAs and question scenarios requiring 45‑day outage tolerance.

- LLM perspective  
  - View: This accelerates the shift from artisanal certificate management to fully automated infrastructure, similar to configuration management a decade ago.  
  - Impact: Small teams and hobby projects must adopt ACME automation or delegate to hosts, or face renewal outage risk.  
  - Watch next: Data on failure rates with 45‑day lifetimes, CT log scaling experiments, and browser policy moves toward shorter terms.
