# We intercepted the White House app's network traffic

- Score: 231 | [HN](https://news.ycombinator.com/item?id=47595865) | Link: https://www.atomic.computer/blog/white-house-app-network-traffic-analysis/

### TL;DR

Atomic Computer’s dynamic audit of the White House iOS app captured 206 app-initiated requests across all five tabs: 23% reached whitehouse.gov and 77% reached 30 third-party hosts. More consequential than the raw percentage, OneSignal received a persistent identifier, IP, device and OS details, activity timestamps, session counts, and duration; Elfsight dynamically supplied widget scripts and set cookies, while YouTube embeds invoked DoubleClick. This conflicts with the app’s manifest claiming no collected data or tracking. HN called the percentage sensational but agreed government software deserves stricter disclosure.

### Comment pulse

- Many external calls were ordinary fonts, thumbnails, or CDN assets — counterpoint: OneSignal’s durable profile and server-selected Elfsight code are qualitatively different.
- User-installed iOS certificates enable inspection for OS-TLS apps without pinning; bundled TLS stacks or pinning make it substantially harder.
- DNS filtering can block known trackers, but users cannot govern later transfer or use once a third party receives data.

### LLM perspective

- **View:** Request count is a weak severity metric; data categories, persistence, executable control, and disclosure determine risk.
- **Impact:** Official-app users unknowingly expose telemetry to vendors beyond the government’s direct operational boundary.
- **Watch next:** Manifest correction, third-party removal, first-party analytics, independent replication, retention terms, app review, and agency response.
