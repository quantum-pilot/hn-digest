# Microsoft Can Track Users via a Windows Device ID

- Score: 323 | [HN](https://news.ycombinator.com/item?id=48815196) | Link: https://www.pcmag.com/news/a-hackers-arrest-reveals-microsoft-can-track-users-via-a-windows-device

### TL;DR
Windows assigns each installation a Global Device ID, which Microsoft apparently used to tell law enforcement that a specific PC accessed an ngrok signup page. Commenters note that machine identifiers are standard across OSes; the real concern is how GDID gets silently attached to browsing or endpoint‑security telemetry, then retained and subpoenaed. Speculation centers on Defender/SmartScreen or third‑party analytics, while the thread broadens into distrust of big‑tech privacy claims and debates over Linux versus Windows tracking.  
*Content unavailable; summarizing from title/comments.*

### Comment pulse
- Machine IDs exist on all major OSes → Worry is opaque boundary: which processes see GDID and whether browser/Defender automatically attach it to web requests.  
- Traffic analysis likely used → SmartScreen, Defender MAPS, or analytics see visited domains plus GDID; subpoenas then link ngrok signup to a Windows device.  
- Microsoft privacy stance condemned → Commenters see long‑standing surveillance culture; some migrate to Linux/Apple, though others note Linux has systemd/dbus machine‑ids and enterprise telemetry too.

### LLM perspective
- View: The controversy is less about identifiers’ existence than undisclosed flows linking local device IDs with detailed browsing telemetry.  
- Impact: Expect renewed scrutiny of SmartScreen‑style services, browser defaults, and endpoint security tools used in enterprises and consumer Windows installs.  
- Watch next: Independent audits clarifying which identifiers browsers, ngrok clients, and Defender send, and concrete retention limits or legal‑process requirements.
