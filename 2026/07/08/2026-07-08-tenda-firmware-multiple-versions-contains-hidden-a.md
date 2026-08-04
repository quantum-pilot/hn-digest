# Tenda firmware (multiple versions) contains hidden authentication backdoor

- Score: 343 | [HN](https://news.ycombinator.com/item?id=48825749) | Link: https://kb.cert.org/vuls/id/213560

### TL;DR

Five listed Tenda firmware builds contain an undocumented fallback in `/bin/httpd`: after normal MD5 password verification fails, `login()` compares the submitted password in plaintext with `sys.rzadmin.password`. A match creates an administrator session with no username validation, enabling device reconfiguration and wider local-network compromise. The issue is tracked as CVE‑2026‑11405. Coordinators could not reach Tenda, and no patch is available; users should disable remote web management and limit local exposure. A commenter linked 2022 reverse engineering that identified the fallback password as `rzadmin`, suggesting the mechanism may be longstanding.

### Comment pulse

- Intent divided readers → some called it a forgotten developer credential — counterpoint: a fixed hidden admin path across releases looks deliberately retained.
- Open firmware won support → auditable alternatives avoid vendor black boxes — counterpoint: missing drivers can sacrifice MIMO, beamforming, efficiency, or throughput.
- Exposure extends beyond niche buyers → commenters noted Tenda’s popularity with Asian ISPs and presence in US consumer gear.

### LLM perspective

- **View:** The decisive flaw is architectural: secret alternate authentication bypasses both account identity and the configured password.
- **Impact:** A shared fallback credential would enable remote takeover where management is exposed; LAN-only devices still face local attackers.
- **Watch next:** Tenda acknowledgement, fixed firmware, credential consistency across models, rebranded hardware, and reliable tests beyond version strings.
