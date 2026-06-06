# Credit cards are vulnerable to brute force kind attacks

- Score: 174 | [HN](https://news.ycombinator.com/item?id=47979839) | Link: https://metin.nextc.org/posts/Credit_Cards_Are_Vulnerable_To_Brute_Force_Kind_Attacks.html

### TL;DR
PCI-DSS lets merchants show the first 6 and last 4 digits of a card plus expiry. The author’s account was breached; attackers saw that masked PAN on a big e‑commerce site, then used many low‑rate validation APIs to enumerate the remaining digits and then brute‑force the CVV, aided by precise error codes (“bad PAN” vs “bad CVV”). They then charged non‑3DS “trusted” merchants and cashed out. He was refunded, but the episode shows how standards, weak rate limits, and ecosystem incentives make brute‑force style attacks practical.

---

### Comment pulse
- Fraud can survive card replacement → tokenized “card updater” / digital wallet links keep charging after reissue, unless explicitly revoked with the issuer.  
- Settlement vs authorization → networks will bill you on a card number alone; fraud is caught only if you or systems dispute charges.  
- Networks claim to fight card testing → ML, penalties, monitoring; attackers adapt via distributed, low‑rate probes and entropy mistakes (e.g., Revolut Japan issuing many similar cards).

---

### LLM perspective
- View: The real bug is business incentives: standards define minimums; issuers tolerate residual brute‑force risk if fraud remains “manageable.”  
- Impact: Consumers rely on after‑the‑fact remediation; merchants and some issuers quietly eat fraud costs, passed on via higher prices and fees.  
- Watch next: Stricter error messages, unified rate‑limiting across acquirers, broader 3DS use, and wider adoption of per‑merchant virtual cards.
