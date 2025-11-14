# Checkout.com hacked, refuses ransom payment, donates to security labs

- Score: 525 | [HN](https://news.ycombinator.com/item?id=45912698) | Link: https://www.checkout.com/blog/protecting-our-merchants-standing-up-to-extortion

- TL;DR
    - Checkout.com disclosed an extortion attempt by ShinyHunters via an improperly decommissioned legacy third‑party file store (used pre‑2021), exposing onboarding/operational docs for <25% of current merchants. Processing systems, funds, and card data were unaffected. The company refused to pay and will donate the ransom amount to CMU and Oxford security labs; it’s notifying affected parties and regulators. HN praises the plain apology but demands a technical postmortem, questions timing and “third‑party” framing, and debates donation vs paying ransom or investing internally; social‑engineering/phished secrets noted.

- Comment pulse
    - Strong response → self-disclosure, refusal to pay, plain apology. — counterpoint: Attackers alerted them; without a detailed postmortem and remediation plan, trust isn’t rebuilt.
    - Donation is virtue signaling → budget should harden security and staffing. — counterpoint: Redirecting ransom publicly signals non-payment and may deter future extortion.
    - Paying ransom can reduce harm → some prefer containment if data is sensitive; others push to outlaw ransom payments to shrink incentives.

- LLM perspective
    - View: The real failure is asset lifecycle control; orphaned third‑party stores persist without owners, alerts, or deletion SLAs.
    - Impact: Merchants face KYC data exposure, phishing risk, and regulatory scrutiny; rivals will benchmark Checkout’s transparency and time‑to‑notify.
    - Watch next: Publish a 60‑day postmortem with decommissioning controls, secret scanning coverage, DLP, detection metrics (MTTD/MTTR), and whether data appears for sale.
