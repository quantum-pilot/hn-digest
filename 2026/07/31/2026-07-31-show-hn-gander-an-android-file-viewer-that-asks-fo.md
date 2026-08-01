# Show HN: Gander, an Android file viewer that asks for no permissions

- Score: 190 | [HN](https://news.ycombinator.com/item?id=49119425) | Link: https://github.com/mokshablr/gander

## TL;DR
Gander is an Android file viewer intentionally built to request zero permissions, aiming to handle local documents without internet or storage access. HN commenters like the privacy-first stance but note Android’s model can still leak data: apps without INTERNET can hand data to browsers, shared-UID apps, or content providers that do have network access. The thread also pushes for stronger supply-chain assurances (signatures, F-Droid listing) and broader format support (OpenDocument), which the developer is actively addressing.

*Content unavailable; summarizing from title/comments.*

---

## Comment pulse
- “No INTERNET permission” ≠ airtight isolation → intents, sharedUserId, and content providers can relay data to online apps — counterpoint: still a meaningful risk reduction versus typical apps.  
- Demand for privacy-respecting, local-only tools is high → Android OEMs hide per-app internet toggles, weakening the permission’s integrity and incentivizing workarounds.  
- Community wants verifiable, consolidating tooling → signature added for Obtainium, F-Droid is on roadmap, and OpenDocument support (ods/odt) is being debugged/expanded.

---

## LLM perspective
- View: Treat “no permissions” apps as lower-risk, not risk-free; combine with OS-level internet firewalls and browser interceptors.  
- Impact: Power users on LineageOS/GrapheneOS benefit most; mainstream users rely on trust plus distribution channels like F-Droid.  
- Watch next: Independent audits, reproducible builds, and permission dashboards that surface potential indirect network paths will matter more than marketing claims.
