# Can someone please explain whether Cloudflare blackmailed Canonical?

- Score: 231 | [HN](https://news.ycombinator.com/item?id=48098537) | Link: https://www.flyingpenguin.com/can-someone-please-explain-whether-cloudflare-blackmailed-canonical/

### TL;DR
The article reconstructs Canonical’s April 2026 DDoS: Ubuntu’s sites go down, then its critical package mirrors are hammered until Canonical moves just those two endpoints behind Cloudflare, stabilizing service. In parallel, the author traces how a Cloudflare‑fronted DDoS‑for‑hire service (Beamed) openly markets Cloudflare‑bypass while enjoying Cloudflare hosting. He argues this creates a de‑facto protection racket: Cloudflare “fronts” the booter’s web presence for free while selling mitigation to victims, even without explicit ransom or coordination.  

---

### Comment pulse
- “Renting capacity from Cloudflare” is wrong → attackers only host their marketing site behind Cloudflare; no evidence attack traffic used Cloudflare infra — counterpoint: Cloudflare IPs do appear in some abuse.  
- Cloudflare should be neutral infrastructure → only act on lawful orders to avoid politicized deplatforming; any stricter vetting harms open access.  
- Cloudflare already selectively deplatforms and its ToS forbids abuse → continuing to host a service advertising Cloudflare‑bypass and DDoS suggests inconsistent enforcement and weak abuse handling.  

---

### LLM perspective
- View: The real issue is structural incentives when one giant mediates both “attackers’ websites” and “victims’ defenses.”  
- Impact: Centralized CDNs gain quasi‑gatekeeper power over reachability, abuse reporting, and incident response economics.  
- Watch next: Clearer transparency on abuse actions, audits of DDoS‑tool hosting, and competition/antitrust pressure on dominant security CDNs.
