# Let's Encrypt bans certificate usage in any US sanctioned territory [pdf]

- Score: 301 | [HN](https://news.ycombinator.com/item?id=48453275) | Link: https://letsencrypt.org/documents/LE-SA-v1.7-June-04-2026-diff.pdf

- TL;DR  
Let’s Encrypt updated its Subscriber Agreement to require users to attest they are not in, owned by, or acting for entities in comprehensively US‑sanctioned territories and will follow US export/sanctions law. HN readers worry this contradicts LE’s mission of universal, free TLS and extends US geopolitical control over critical security infrastructure. LE staff reply that this mostly codifies existing OFAC‑driven practice, mainly targeting governments rather than ordinary users, but the change spotlights how centralized trust roots inherit their host country’s politics.

- Comment pulse  
  - Mission vs sanctions: critics say LE betrays “anyone can use it” by obeying US policy — counterpoint: staff argue it just clarifies ongoing OFAC‑driven practice.  
  - Jurisdiction: some urge moving LE or cloning it outside US control; others note root-trust is social, and non-US CAs still depend on US-led browser vendors.  
  - Power: some call PKI “digital tyranny” enabling control; others note exclusion is intrinsic to preventing MITM, with users still free to use self-signed certs.

- LLM perspective  
  - View: Clearer communication about who’s blocked and why could reduce confusion and demonstrate LE’s minimal-necessary approach to sanctions compliance.  
  - Impact: Sanctioned governments may struggle slightly more to obtain trusted TLS, but ordinary citizens’ risk remains censorship, not lack of HTTPS.  
  - Watch next: Watch whether major browser vendors or non-US nonprofits sponsor alternative, jurisdictionally diverse ACME CAs to dilute single-country policy influence.
