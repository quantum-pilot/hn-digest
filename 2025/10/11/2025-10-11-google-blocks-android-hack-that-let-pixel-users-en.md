# Google blocks Android hack that let Pixel users enable VoLTE anywhere

- Score: 126 | [HN](https://news.ycombinator.com/item?id=45553764) | Link: https://www.androidauthority.com/pixel-ims-broken-october-update-3606444/

TL;DR
Google’s October 2025 Pixel update closes a testing loophole the Pixel IMS app used (via Shizuku shell access) to override carrier checks and force VoLTE/VoWiFi on imported Pixels. Google labeled it CVE-2025-48617, a high‑severity privilege escalation, likely to appear in December’s bulletin under RBUS. A new, rougher workaround reportedly re‑enables VoLTE (not VoWiFi); Wi‑Fi calling now needs root or official support. HN debates whether this is security or carrier‑driven lock‑in, citing dual‑SIM quirks and messy VoLTE/VoNR provisioning across Android.

Comment pulse
- Not a vulnerability → Required ADB/Shizuku shell; users chose to grant power-user access — counterpoint: Letting apps inherit shell to override IMS is privilege escalation.
- Blame carriers → Certifications, whitelists, and fragmented VoLTE/VoNR configs block features on unlocked/imported phones; Apple’s centralized updates hide this, Android exposes mess.
- User pain → Dual‑SIM/Wi‑Fi calling behaviors differ; iOS allows SIM1 calls over SIM2 data, while Pixels and many Androids block or require carrier bloat/config hacks.

LLM perspective
- View: Security patch closes a gray-market feature gap; users will chase new workarounds until official IMS provisioning is broader and standardized.
- Impact: Importers, travelers, and dual‑SIM users lose VoWiFi; some gain VoLTE via new app; rooting risks break Gemini features and payments.
- Watch next: December security bulletin details, Shizuku/wireless‑debugging restrictions, Google/GSMA carrier expansions, and whether a safe, documented IMS config discovery standard emerges.
