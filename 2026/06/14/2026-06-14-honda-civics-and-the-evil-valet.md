# Honda Civics and the Evil Valet

- Score: 397 | [HN](https://news.ycombinator.com/item?id=48523080) | Link: https://juniperspring.org/posts/honda-evil-valet/

### TL;DR
Honda’s 10th‑gen Civic head unit runs an Android‑style recovery that accepts USB update packages signed with the public AOSP test key. With physical access to the front USB port, an attacker can craft and flash their own package for arbitrary code execution—no exploit or root escalation needed—enabling the “EvilValet” attack scenario. The author ships tooling (ota‑builder, apk‑rebuilder, AIDL mappers) and calls for contributors, while Hacker News debates car infotainment as a surveillance risk, physical‑access threat models, and poor firmware‑update practices.

---

### Comment pulse
- Civic head unit updates are Android recovery zips signed by AOSP test keys → anyone with USB access can flash arbitrary code on many units.  
- Modern cars are rolling sensor platforms → governments now warn staff not to pair devices or discuss secrets near infotainment systems — counterpoint: average-person risk is limited but nonzero.  
- Physical access is debated: some say “game over,” others stress hardening anyway; war stories show firmware signed but never verified, and Civics can still be high‑value targets.

---

### LLM perspective
- View: Treat car head units as general-purpose networked computers; they deserve real code-signing, key management, and update validation, not test keys.  
- Impact: Security researchers gain a solid toolkit; regulators and fleet operators gain another concrete example to justify stricter in‑vehicle device policies.  
- Watch next: Replicate this analysis across other OEMs, map CAN-bus reachability from infotainment, and track manufacturer responses or recalls.
