# Stripe is friendly to “friendly fraud”

- Score: 310 | [HN](https://news.ycombinator.com/item?id=48287982) | Link: https://www.gingerlime.com/2026/stripe-seem-friendly-to-friendly-fraud/

### TL;DR

A small merchant says a customer placed two cigar-glue orders and disputed both; one had delivery proof, and the buyer later gloated in writing. Despite that evidence and screenshots, Stripe reportedly would neither feed the case into cross-merchant fraud signals nor flag the buyer, suggesting only merchant-specific Radar rules. The author argues this leaves each seller exposed while banks, networks, and Stripe externalize losses. HN split over whether Stripe failed merchants or reasonably avoided dangerous network-wide bans.

### Comment pulse

- Merchant-side defenses are imperfect → ban cards, emails, and device fingerprints after chargebacks; determined abusers can rotate identifiers, while 3-D Secure may shift liability.
- Attribution remains contested → Stripe says issuers decide outcomes — counterpoint: a card-industry commenter says networks arbitrate and Stripe sometimes declines winning cases.
- Clear support did not soften the policy dispute → commenters valued Stripe’s candor, but experienced merchants described weak Radar scores and misaligned incentives.

### LLM perspective

- **View:** Fraud systems need graduated reputation signals, not binary bans: corroborated post-transaction abuse should increase scrutiny without becoming unilateral blacklisting.
- **Impact:** Payment processors should expose evidence handling, escalation status, and liability paths so merchants can price and manage chargeback risk.
- **Watch next:** Chargeback appeal tooling, network rule disclosures, merchant loss rates, and whether processors waive fees after documented abuse.
