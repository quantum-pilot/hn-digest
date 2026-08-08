# Localsend: An open-source cross-platform alternative to AirDrop

- Score: 725 | [HN](https://news.ycombinator.com/item?id=47933208) | Link: https://github.com/localsend/localsend

### TL;DR

LocalSend is a free, open-source file-and-message transfer app for Windows, macOS, Linux, Android, iOS, and Fire OS. Nearby devices communicate directly over the same local network through a REST API secured with HTTPS and per-device, on-the-fly certificates; no internet connection or third-party server is required. Distribution spans app stores, package managers, and standalone builds, but the app lacks automatic updates. HN users generally liked its cross-platform reliability, while stressing that unlike AirDrop it cannot create its own peer network, so offline transfers still require a hotspot or ad-hoc LAN.

### Comment pulse

- AirDrop’s automatic peer networking is the missing convenience; LocalSend transfers only after devices can already reach one another.
- Some found LocalSend more dependable than AirDrop — counterpoint: others reported slow discovery despite opening firewall ports.
- Browser-based PairDrop and relay-backed Sendme broaden reach, but room codes or relays introduce different usability and trust tradeoffs.

### LLM perspective

- Optional ad-hoc networking would narrow AirDrop’s largest experiential advantage without changing local-first transfer.
- Signed releases and package-manager updates matter because manual installs otherwise age silently.
- Benchmark discovery time, transfer speed, and firewall behavior across home, guest, and enterprise networks.
