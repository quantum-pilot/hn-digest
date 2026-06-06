# Gov.uk has replaced Stripe with Dutch provider Adyen

- Score: 311 | [HN](https://news.ycombinator.com/item?id=48415217) | Link: https://www.theregister.com/public-sector/2026/06/04/govuk-goes-dutch-on-payments-as-it-dumps-stripe/5250763

### TL;DR
The UK Government Digital Service is moving a big chunk of GOV.UK Pay from Stripe to Dutch processor Adyen under a three‑year contract worth up to £25.3m. Adyen will handle card and new “pay by bank” open‑banking payments for local authorities, police and armed forces, covering ~17% of transactions but 70%+ of participating organizations. Worldpay stays for central government and the NHS. HN discussion zooms in on payment economics, public instant‑payment rails, and Adyen’s enterprise‑only focus versus Stripe’s dev‑friendly model.

---

### Comment pulse
- Public instant‑payment rails show true costs → Pix and UPI operate huge national volumes cheaply, suggesting card fees and processor margins are structurally inflated — counterpoint: they do shift liquidity burdens to banks.  
- Stripe vs Adyen positioning → Stripe wins small merchants with self‑serve onboarding and developer focus; Adyen explicitly targets larger merchants, often rejecting <€5m/year clients and pushing them to resellers.  
- Who should pay fees? → Some argue passing transaction costs to users would drive adoption of cheaper bank transfers; others note regulation and poor APIs still lock in card usage.

---

### LLM perspective
- View: Moving to Adyen plus “pay by bank” is a quiet step toward account‑to‑account, open‑banking‑centric public payments.  
- Impact: Local authorities may lower card dependence; card networks and high‑margin acquirers face gradual erosion, especially on government volumes.  
- Watch next: Actual pay‑by‑bank uptake, fee structures disclosed to councils, and whether UK layers on Pix/UPI‑style real‑time infrastructure.
