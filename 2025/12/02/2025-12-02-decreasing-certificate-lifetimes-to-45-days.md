# Decreasing Certificate Lifetimes to 45 Days

- Score: 148 | [HN](https://news.ycombinator.com/item?id=46117126) | Link: https://letsencrypt.org/2025/12/02/from-90-to-45.html

- TL;DR  
  Let’s Encrypt will phase certificate lifetimes down from 90 to 45 days and sharply reduce how long domain validations can be reused, following industry-wide CA/Browser Forum rules. This assumes fully automated issuance and renewal, with ARI guiding when to renew and monitoring catching failures. To offset more frequent validations, they’re pushing DNS-PERSIST-01, where a single long-lived DNS TXT record can authorize repeated renewals. Hacker News reactions praise automation, worry about churn and enterprise friction, and debate safe approaches to certificate pinning.

- Comment pulse  
  Automation-first certificates are good → ACME and short lifetimes reduce compromise impact and make non-automated enterprise tooling look increasingly irresponsible.  
  DNS-PERSIST-01 excites admins → static TXT records remove DNS-API automation needs; critics dislike account IDs in DNS—counterpoint: CAs could instead store opaque tokens.  
  Frequent policy changes frustrate some → they fear brittle integrations and needless work, while others say short certs nudged them into automation and fewer outages.

- LLM perspective  
  View: Treat TLS certificates like ephemeral infrastructure; integrate issuance and reloads into deployment pipelines rather than separate “security tasks”.  
  Impact: Orgs with manual renewals or legacy app servers must standardize ACME tooling and thoroughly test automated reloads in staging.  
  Watch next: Track DNS-PERSIST uptake, ARI support in major clients, and any browser pushes toward CT-enforced revocation or automation signals.
