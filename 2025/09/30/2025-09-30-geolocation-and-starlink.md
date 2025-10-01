# Geolocation and Starlink

- Score: 142 | [HN](https://news.ycombinator.com/item?id=45422514) | Link: https://www.potaroo.net/ispcol/2025-09/starlinkgeo.html

TL;DR
APNIC Labs estimated ISP market share per country using ad impressions mapped by IP geolocation and BGP. Starlink’s roaming LEO service breaks the “IP=country” assumption: ships, aircraft, and cross‑border dishes cause large misattributions (e.g., Yemen erroneously shows 59% Starlink). APNIC now marks 20 Starlink country entries “unclassified.” The piece asks whether geolocation should reflect territory, gateways, or flag‑state, and how to represent “at sea/in flight.” HN debates legality, weak enforcement, and whether IP geolocation is useful beyond country level.

Comment pulse
- Starlink resellers register in approved countries, operate dishes elsewhere; terminals have GPS so geofencing is feasible—counterpoint: circumvention empowers citizens under censorship.
- IP geolocation works surprisingly well for fixed networks; it fails with roaming/mobile/satellite, and ad-based sampling inherits those biases.
- States have little leverage; they may deny licenses or punish users. Extreme chatter about anti-satellite retaliation exists but seems impractical and escalatory.

LLM perspective
- View: Static IP-to-country is obsolete for LEO; adopt dynamic, session-based location with “at sea” and “in flight” codes.
- Impact: Content licensing, tax/regulation, abuse tracing, and market-share metrics degrade; small nations see large skew from maritime and roaming traffic.
- Watch next: Standardize mobile geofeeds; add ISO/UN location categories; require provider-signed per-session location attestations with privacy safeguards and auditability.
