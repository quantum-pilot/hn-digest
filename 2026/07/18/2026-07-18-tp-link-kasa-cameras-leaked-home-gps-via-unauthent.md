# TP-Link Kasa cameras leaked home GPS via unauthenticated UDP for 6 years

- Score: 217 | [HN](https://news.ycombinator.com/item?id=48952565) | Link: https://github.com/BadChemical/IoT-Vulnerability-Research-Public/blob/main/TP-Link_Kasa_EC71/Kasa_EC71.md

- TL;DR  
  An in-depth firmware teardown of TP-Link’s Kasa EC71 camera found three serious issues: fleet-wide hardcoded TLS keys, unsalted MD5 storage of global TP-Link ID credentials, and unauthenticated UDP responses leaking precise home GPS and device fingerprints on the local network, even after “factory reset,” enabling secondhand-account takeover. The leak stems from a 2016-era protocol reused across models and ignored for years. TP-Link finally patched in 2.4.1 after a painful, delay-ridden disclosure process, but scope remains unclear.

- Comment pulse  
  - IoT should avoid cloud dependency → prefer devices that work locally, block internet at router; distrust spans countries—government-controlled gateways proposed, but practicality and trust questioned.  
  - Some say LAN-only GPS leak is minor compared to other ways to infer location; others argue this wrongly shifts blame from insecure vendors to users.  
  - Commenters highlight pervasive unencrypted location/PII flows through third-party and ISP infrastructure, feeding data brokers and rendering even strong vendor privacy policies largely irrelevant.

- LLM perspective  
  - View: This case shows how legacy local protocols and weak crypto decisions can silently undermine entire smart-home ecosystems for years.  
  - Impact: Beyond Kasa cameras, any TP-Link ID user and secondary-market buyer faces elevated account-takeover and physical-location exposure risks.  
  - Watch next: Independent testing of sibling models, mandated third-party IoT security reviews, and enforcement of privacy-policy claims around opt-in geolocation.
