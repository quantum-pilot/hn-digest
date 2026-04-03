# Subscription bombing and how to mitigate it

- Score: 279 | [HN](https://news.ycombinator.com/item?id=47609882) | Link: https://bytemash.net/posts/subscription-bombing-your-signup-form-is-a-weapon/

### TL;DR
Subscription bombing uses bots to sign up a victim’s email on many sites, flooding their inbox with “welcome” and “reset password” emails so real security alerts get buried. The author spotted low-rate, globally distributed fake signups plus password-reset traffic, then mitigated with behavioral CAPTCHA, stricter bot filtering, and a rule to send only one email until the address is verified. HN comments broaden this to payment-form abuse, layered bot defenses, email-verification negligence, and worries about centralizing control in services like Cloudflare.

---

### Comment pulse
- Attackers repurpose signup/payment flows to validate stolen credit cards → tiny test charges, refunds, and rotated IPs evade rate limits; “silent blocks” can waste attackers’ time unnoticed.  
- Newsletter operators: defenses are now “Swiss cheese model” → Turnstile, webdriver detection, honeypots, step-ups; VPN prevalence ruined IP reputation as a simple filter — counterpoint: centralizing on big CAPTCHA providers erodes internet resilience.  
- Owners of generic emails report constant misdirected receipts and disclosures → companies skip verification to reduce friction and accept some fraud; victims resort to filters and wildcard aliases.

---

### LLM perspective
- View: Treat any unauthenticated email-triggering action (signup, reset, card change) as a high-risk API needing abuse budgets and verification.  
- Impact: Product teams must weigh conversion friction against real downstream harm; email and payment providers may pressure laggards.  
- Watch next: Shared best-practice checklists, browser-signal standards, and lighter-weight, privacy-preserving bot checks to avoid overreliance on single vendors.
