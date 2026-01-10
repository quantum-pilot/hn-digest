# SendGrid isn’t emailing about ICE or BLM – it’s a phishing attack

- Score: 169 | [HN](https://news.ycombinator.com/item?id=46555615) | Link: https://fredbenenson.com/blog/2026/01/09/sendgrid-isnt-emailing-you-about-ice-or-blm-its-a-phishing-attack/

## TL;DR
Attackers are compromising real SendGrid customer accounts and using them to send phishing emails that look like official SendGrid policy updates about hot‑button issues (BLM, LGBT pride, ICE donations, language changes, account termination). Because they’re sent via SendGrid infrastructure and legitimate customer domains, they pass SPF/DKIM and appear authentic. The “opt‑out” buttons lead to fake login pages that steal credentials and 2FA codes. HN discussion centers on better mail‑server filtering and whether SendGrid’s model or execution is at fault.

---

## Comment pulse
- Tight GSuite/regex rules for “SendGrid” mail → can quarantine fakes; counterpoint: narrow sender‑specific filters don’t scale, better rely on SPF/DKIM plus user training.  
- Critics blame SendGrid’s execution, not inherent business model → weak support, deliverability issues, and sloppy billing suggest deeper operational problems attackers can exploit.  
- Brand impersonation outpaces protocols → SPF/DKIM/DMARC protect domains, but “friendly name” spoofing plus mobile clients hiding real addresses keeps users exposed.

---

## LLM perspective
- View: This shows phishing evolving from crude scams to psychologically tuned, infrastructure‑abusing attacks that ride on real reputations.  
- Impact: Any SaaS that sends on behalf of customers becomes a high‑leverage phishing platform unless it enforces strong auth and anomaly detection.  
- Watch next: Mandatory 2FA, behavioral monitoring of bulk senders, and UX changes that always surface real sender domains, especially on mobile.
