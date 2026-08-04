# Nearly half of LG smart TV apps contain residential proxy SDKs

- Score: 176 | [HN](https://news.ycombinator.com/item?id=48635954) | Link: https://spur.us/blog/smart-tv-apps-residential-proxy-sdks

### TL;DR

Researchers report residential-proxy SDKs in nearly half of LG smart-TV apps; across 6,038 LG webOS and Samsung Tizen packages, 2,058 monetized household IP addresses, sometimes after closure. Many were thin games, clocks, or screensavers, with proxy vendors appearing as publishers. Security concern extends beyond IP misuse: absent or failed private-range filtering could expose routers, NAS devices, cameras, and other LAN systems. Providers cited consent, KYC, and traffic controls. HN stressed these were third-party apps, debated whether prompts constitute meaningful consent, and recommended isolating or disconnecting smart TVs.

### Comment pulse

- The headline needs scope → affected packages are third-party store apps, not LG-built software — counterpoint: platform review still determines what televisions may execute.
- Consent is visible but fragile → some prompts disclose proxying and offer ads instead, yet remote-driven setup and persistent background operation undermine comprehension.
- Network separation is the practical defense → commenters favor disabled Wi-Fi, gateway-less VLANs, or external Linux/Apple TV devices over trusting television firmware.

### LLM perspective

- **View:** A residential proxy changes device trust: outbound connectivity becomes delegated execution by unknown customers, governed mostly outside the home.
- **Impact:** Households inherit abuse attribution and lateral-movement risk; app stores become security gatekeepers for a monetization model users cannot audit.
- **Watch next:** Demand per-app traffic logs, persistent status indicators, revocable consent, LAN-isolation tests, publisher disclosure, and platform-wide proxy SDK policies.
