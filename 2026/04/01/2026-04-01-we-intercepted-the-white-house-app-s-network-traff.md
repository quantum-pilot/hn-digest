# We intercepted the White House app's network traffic

- Score: 231 | [HN](https://news.ycombinator.com/item?id=47595865) | Link: https://www.atomic.computer/blog/white-house-app-network-traffic-analysis/

### TL;DR
The author man-in-the-middled the official White House iOS app and found that most network calls go to commercial services, not whitehouse.gov. On launch and use, the app updates a persistent OneSignal profile with network identifiers, device fingerprinting details, and detailed usage metrics, while Elfsight widgets load remotely-controlled JavaScript and numerous cookies. YouTube embeds pull in Google’s ad/DoubleClick stack. Despite this, the App Store privacy manifest declares no data collection or tracking, prompting HN debate over risk severity and standards for government apps.

---

### Comment pulse
- “77% third-party” feels sensational to some; many endpoints are routine CDNs. Others argue brokers like Google/Facebook later resell this “boring” telemetry — counterpoint: don’t shoot the messenger.
- Discussion around TLS interception: iOS still trusts user CAs for most apps, making MITM feasible; commenters see this as vital for auditing opaque mobile data flows.
- Several argue government apps must avoid external telemetry providers and self-host assets; others question why state-branded apps deserve stricter treatment than ordinary consumer software.

---

### LLM perspective
- View: The core problem is misalignment between declared “no tracking” and real-world analytics/ads integrations, not merely the presence of third-party domains.
- Impact: Public institutions and contractors face reputational and regulatory exposure if privacy labels understate cross-network profiling capabilities.
- Watch next: Independent tooling for routine mobile traffic audits, plus stronger store-level enforcement of privacy manifests and limits on embedded ad/analytics SDKs in gov apps.
