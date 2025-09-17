# Wanted to spy on my dog, ended up spying on TP-Link

- Score: 418 | [HN](https://news.ycombinator.com/item?id=45251690) | Link: https://kennedn.com/blog/posts/tapo/

TL;DR
An engineer bought a TP-Link Tapo cam and reverse‑engineered its onboarding: MITM’d the app with Frida+mitmproxy, decrypted the securePassthrough channel, decompiled the APK to reveal a hardcoded default admin password (TPL075526460603), then scripted a cloudless setup that enables RTSP/ONVIF and fixes password sync quirks. They found inconsistent crypto (MD5 and SHA‑256) and odd key handling. HN fixates on the two‑way audio vs ONVIF tradeoff and extends the critique to insecure, ISP‑managed routers.

Comment pulse
- Frida/HTTP Toolkit + mitmproxy are effective → bypasses pinning, captures onboarding traffic; open scripts worked with minimal tweaks.
- Two‑way audio requires tapo://, but ONVIF pan/tilt breaks → users juggle streams to talk and move cameras — counterpoint: accept single‑feature workflows.
- Consumer routers are unaudited black boxes → outdated firmware, defaults, ISP control increase risk — counterpoint: end‑to‑end encryption mitigates eavesdropping.

LLM perspective
- View: Default credentials plus encrypted tunnels create security theater; local-first onboarding is feasible and improves reliability.
- Impact: Expect community tools enabling offline setup to spread across IoT brands, reducing cloud lock-in and subscription upsells.
- Watch next: Vendor response: randomize per-device passwords, unify crypto, deprecate MD5, enforce pinning; community: publish benchmarks, harden scripts, responsible disclosure timelines.
