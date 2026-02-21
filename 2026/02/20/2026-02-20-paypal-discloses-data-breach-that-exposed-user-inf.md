# PayPal discloses data breach that exposed user info for 6 months

- Score: 260 | [HN](https://news.ycombinator.com/item?id=47087719) | Link: https://www.bleepingcomputer.com/news/security/paypal-discloses-data-breach-exposing-users-personal-information/

### TL;DR
PayPal disclosed that a bug in its PayPal Working Capital loan application exposed the personal data (including SSNs and DOBs) of about 100 small-business customers from July–December 2025. The issue was a bad code change, not a network “hack”: the app itself could unintentionally show data to unauthorized parties. PayPal rolled back the change, reset passwords, refunded a few fraudulent transactions, and offered two years of Equifax monitoring. HN commenters focus less on this small incident and more on PayPal’s broader trust, usability, and relevance problems.

---

### Comment pulse
- Deep distrust of PayPal → many recount account freezes, confiscated balances, or impossible verification hoops; several refuse to ever use it again.  
- Questioning PayPal’s relevance → Stripe/Apple/Google Pay and bank e‑transfers cover most needs—counterpoint: PayPal still useful for buyer protection, micropayments, and broad international coverage.  
- Skepticism about disclosure timing → “no delay due to law enforcement” sounds narrow; suspicion they stalled for PR reasons amid growing security/UX friction across fintech.

---

### LLM perspective
- View: Classic business-logic failure—no perimeter breach needed; sensitive fields were simply exposed by flawed application behavior.  
- Impact: Only ~100 users, but SSNs and DOBs invite identity theft; regulators will scrutinize PayPal’s secure development practices.  
- Watch next: Any new regulatory deadlines for breach disclosure, and whether merchants/users meaningfully shift volume from PayPal to competing payment rails.
