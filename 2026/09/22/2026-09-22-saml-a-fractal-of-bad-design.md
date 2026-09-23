# SAML: A fractal of bad design

- Score: 329 | [HN](https://news.ycombinator.com/item?id=49806335) | Link: https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/

### TL;DR

Security engineer Matt Schwager argues SAML should be retired in favor of OpenID Connect. SAML’s XML foundation brings parser hazards, canonicalization differentials, enveloped-signature complexity, rarely used specification surface, and assumptions inherited from disconnected enterprise networks. He recommends vendors stop new SAML integrations and migrate customers gradually. HN commenters broadly agree SAML is dangerous but dispute a clean victory for OIDC: JWT and JOSE have failures too, enterprise customers still expect SAML features, and business incentives impede provider-independent identity.

### Comment pulse

- SAML compounds implementation risk → XML parsing, signature scope, canonicalization, and attacker-selected verification behavior repeatedly create authentication bypasses.
- OIDC is not automatically safe → JWT libraries suffer algorithm confusion and missing checks — counterpoint: XML signatures add substantially greater complexity.
- Enterprise migration remains pragmatic rather than absolute → stable SAML compatibility and IdP-initiated workflows keep dual-protocol support commercially relevant.

### LLM perspective

- View: Replacing a hazardous protocol reduces risk only when implementations enforce narrow profiles and verify every security invariant.
- Impact: New SaaS vendors can avoid SAML, while established identity providers face long customer-by-customer migrations.
- Watch next: Track SAML deprecation commitments, OIDC interoperability, exploit rates, and adoption of safer library defaults.
