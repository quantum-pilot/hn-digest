# Android now stops you sharing your location in photos

- Score: 298 | [HN](https://news.ycombinator.com/item?id=47750669) | Link: https://shkspr.mobi/blog/2026/04/android-now-stops-you-sharing-your-location-in-photos/

### TL;DR  
Android now strips GPS data from photo metadata when sharing from phones via browsers, Bluetooth, QuickShare, or email; only USB copies preserve it. Google frames this as privacy, preventing hidden EXIF leaks, but it breaks benign web apps like OpenBenches that map photos. Devs are pushed toward native apps with ACCESS_MEDIA_LOCATION permissions. HN reactions mostly support stronger defaults, yet criticize Google’s paternalism and lack of opt‑in controls (e.g., an upload‑time “include location” toggle).

---

### Comment pulse

- Stripping EXIF by default → matches user expectations; most never realised uploads exposed precise GPS to arbitrary sites — counterpoint: power-users lose legitimate workflows.  
- Critics: this is “privacy by locking you out of your own data”; Google and platforms still keep metadata while export/sharing paths are crippled.  
- Volunteer mapping/reporting tools depending on geotagged uploads are badly hurt; many call for an HTML includeLocation hint plus explicit, one‑time user permission.  

---

### LLM perspective

- View: Good default to redact hidden PII, but users need clear, per‑upload controls to intentionally share rich metadata with trusted services.  
- Impact: Web‑first civic, scientific and archival projects lose capability, pushing them toward heavier native apps or cumbersome workarounds like zipping images.  
- Watch next: Chrome/Android permission updates, HTML spec discussions on location‑bearing uploads, and whether alternative standards for verifiable, user‑granted photo provenance emerge.
