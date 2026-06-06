# Localsend: An open-source cross-platform alternative to AirDrop

- Score: 725 | [HN](https://news.ycombinator.com/item?id=47933208) | Link: https://github.com/localsend/localsend

### TL;DR
LocalSend is an open-source, cross‑platform AirDrop-style app for Windows, macOS, Linux, Android, iOS, and Fire OS. It transfers files and text over existing local networks only, using a simple REST/HTTPS protocol with self-generated TLS certificates, so nothing ever touches external servers or the internet. It’s distributed through major app stores and common package managers, and can also be built with Flutter and Rust from source. HN discussion centers on networking expectations, alternative tools, and packaging tradeoffs.

### Comment pulse
- Localsend needing an existing LAN feels clunky versus AirDrop’s automatic ad‑hoc Wi‑Fi; users must juggle hotspots, router isolation, and firewall tweaks for discovery.  
- Commenters share alternatives: thinair, FFL, FlyingCarpet, Sendme/Iroh, and browser-based PairDrop; these add internet relays or WebRTC but often require awkward room codes.  
- One dev contrasts Tauri vs Electron/Flutter: smaller installers but painful Linux packaging and webview quirks; another questions such apps versus cloud albums, messaging, or SMB.  

### LLM perspective
- View: Local-first, open tools like LocalSend show demand for offline, private sharing beyond Apple‑ or Google‑controlled ecosystems.  
- Impact: Helps Linux, mixed-OS, and privacy-conscious users; pressures platform vendors to improve native sharing or open protocols.  
- Watch next: Better automatic peer discovery over Wi‑Fi Direct/WebRTC, mobile OS share-sheet integration, and interop standards between projects.
