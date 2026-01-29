# Somebody used spoofed ADSB signals to raster the meme of JD Vance

- Score: 225 | [HN](https://news.ycombinator.com/item?id=46802067) | Link: https://alecmuffett.com/article/143548

## TL;DR
Someone drew a JD Vance meme “flight path” over Mar‑a‑Lago by feeding fake ADS‑B data into ADS‑B Exchange, using an ICAO identity associated with Air Force Two and the callsign VANCE1. This wasn’t radio-layer spoofing: no real aircraft or air-traffic systems were affected, and the bogus track appears only on that one crowd-sourced site. HN discussion focuses on how easy internet-side spoofing is, why RF spoofing would be far more serious legally, and what this means for trusting public flight trackers.

---

## Comment pulse
- Not RF spoofing → A fake feeder sent data only to ADS‑B Exchange; other aggregators show nothing, so no real transponder was impersonated.
- Novelty is the raster art → Prior spoofing was crude shapes or text; this demonstrates more sophisticated image-style tracks—counterpoint: still just a cosmetic prank on one site.
- Legal risk remains → FCC/FAA treat RF fakery harshly; even data-level hoaxes near airports could prompt tighter anti-spoofing and liability for feeder operators.

---

## LLM perspective
- View: Public flight-tracking data is easy to pollute at the aggregation layer, undermining casual users’ trust in “open skies” maps.  
- Impact: ADS‑B aggregators, OSINT researchers, and journalists depending on these feeds may need provenance checks, cross-site validation, and anomaly detection.  
- Watch next: Whether major sites add feeder attestation, cross-network consistency checks, and publish clearer policies or sanctions for intentional data fakery.
