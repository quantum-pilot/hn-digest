# Mobile carriers can get your GPS location

- Score: 375 | [HN](https://news.ycombinator.com/item?id=46838597) | Link: https://an.dywa.ng/carrier-gnss.html

### TL;DR
Mobile networks don’t just infer your location from cell towers; they can directly query your phone for its GNSS (GPS/GLONASS/Galileo/BeiDou) coordinates via control‑plane protocols (RRLP in 2G/3G, LPP in 4G/5G). This gives law enforcement and intelligence agencies map‑level precision, often without a warrant and largely invisible to users. Apple’s iOS 26.3 adds an option (on a few new devices/carriers) to limit “precise location” to networks. The article argues users should be able to block and see all such GNSS requests.

---

### Comment pulse
- Accountability over secrecy → Users should disable data sharing, get notified of any bypass, and have legal recourse; punish misuse like fire hazards—counterpoint: better to drown surveillance systems in synthetic data noise.
- Alternative networks → LoRa/Reticulum mesh systems promise peer‑to‑peer, low‑infrastructure messaging, but suffer from limited real‑world range, radio overload risk, and awkward encryption/key models.
- Emergency tradeoffs → EU/US use different “hidden SMS” GPS pings for 112/911; Apple’s new toggle is device- and carrier-limited, raising concern about degrading emergency location.

---

### LLM perspective
- View: Control‑plane location APIs make “location off” misleading; OS vendors need to mediate modem behavior and surface every external location query.
- Impact: Carriers, handset makers, and data brokers face pressure for transparency; privacy‑sensitive users may shift to niche networks or supplement with off‑grid tools.
- Watch next: Independent modem audits, standardized user-visible prompts for network location pings, and regulation narrowing data brokerage and warrantless government purchases.
