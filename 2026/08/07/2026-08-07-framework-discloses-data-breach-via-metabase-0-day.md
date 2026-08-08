# Framework discloses data breach via Metabase 0-day

- Score: 141 | [HN](https://news.ycombinator.com/item?id=49206130) | Link: https://community.frame.work/t/framework-data-breach-discussion/83939

- TL;DR  
  Framework disclosed that its Metabase Cloud analytics instance was compromised via a 0‑day, exposing customer PII (names, emails, addresses, order metadata) but not payment data, which is handled by Stripe. They notified users within hours of Metabase’s alert and shared detailed incident context, which many commend. However, customers and HN commenters are angry that rich PII was ever pushed to a third‑party BI tool, criticize “limited breach” messaging, and call for strict data‑minimization, retention limits, and less reliance on SaaS analytics.

- Comment pulse  
  - Analytics and CRM SaaS are seen as the weakest security link → repeated breaches show offloading PII to vendors magnifies blast radius.  
  - Framework’s response praised for speed and transparency → others call “limited breach” spin, want compensation, audits, and stricter data‑minimization and retention rules.  
  - Metabase 0‑day details worry engineers → attacker ran arbitrary queries, exfiltrated sample rows; many advocate self‑hosting behind VPN or abandoning Metabase Cloud entirely.

- LLM perspective  
  - View: This incident exemplifies modern “PII supply‑chain” risk—breaches now propagate through analytics and SaaS ecosystems, not core payment processors.  
  - Impact: Privacy‑conscious users, EU regulators, and smaller vendors will push harder for data‑minimization, pseudonymization, and aggressive deletion of dormant accounts.  
  - Watch next: Whether Metabase publishes technical details and mitigations, and if clients migrate to self‑hosted, VPN‑only, or in‑house analytics alternatives.
