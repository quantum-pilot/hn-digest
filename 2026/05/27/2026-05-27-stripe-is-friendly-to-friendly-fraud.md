# Stripe is friendly to “friendly fraud”

- Score: 310 | [HN](https://news.ycombinator.com/item?id=48287982) | Link: https://www.gingerlime.com/2026/stripe-seem-friendly-to-friendly-fraud/

- TL;DR  
Friendly fraud is when real cardholders dispute legitimate charges and win. The author describes a buyer who repeatedly disputed a cheap physical product, admitted the scam in email, yet still won both Stripe disputes. Stripe confirmed they do not feed such merchant-provided evidence into cross-merchant fraud signals and only suggest per-merchant Radar rules, often paid. HN commenters trade mitigation tips, argue about whether Stripe or banks/card networks deserve blame, and question Stripe’s incentives and Radar’s effectiveness.

- Comment pulse  
  - Merchants advise auto-banning cards, emails, devices after chargebacks and enabling 3D Secure to shift liability—counterpoint: determined abusers easily rotate identities and bypass fingerprints.  
  - Some say only customer and issuing bank are culpable; others note networks decide disputes and accuse Stripe of rarely contesting to save costs.  
  - Stripe Radar is criticized as mis-scoring risky payments; broader sentiment casts Stripe as PayPal-like incumbent whose incentives conflict with small merchants.

- LLM perspective  
  - View: Card networks, not just processors, must support tagging proven chargeback abusers so future disputes face higher scrutiny.  
  - Impact: Systematic sharing of post-transaction abuse signals would mainly protect small merchants selling low-margin, easily reshipped physical goods.  
  - Watch next: Experiments with “abuse report” APIs, network-wide risk scoring, and regulator guidance on balancing due process with fraud prevention.
