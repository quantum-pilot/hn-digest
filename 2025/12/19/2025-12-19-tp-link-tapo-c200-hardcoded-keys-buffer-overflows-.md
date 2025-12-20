# TP-Link Tapo C200: Hardcoded Keys, Buffer Overflows and Privacy

- Score: 194 | [HN](https://news.ycombinator.com/item?id=46329038) | Link: https://www.evilsocket.net/2025/12/18/TP-Link-Tapo-C200-Hardcoded-Keys-Buffer-Overflows-and-Privacy-in-the-Era-of-AI-Assisted-Reverse-Engineering/

## TL;DR
- Security researcher Simone Margaritelli used AI-assisted reverse engineering to analyze TP-Link’s cheap Tapo C200 IP camera firmware, easily downloaded and decrypted from TP-Link’s public S3 bucket and GPL sources. He found hardcoded TLS keys plus four pre-auth bugs: ONVIF XML memory overflow, HTTPS Content-Length integer overflow, unauthenticated Wi-Fi reconfiguration, and unauthenticated nearby Wi-Fi scanning enabling remote geolocation. Around 25k devices are exposed online. TP-Link, acting as its own CNA, missed its stated 90‑day patch window.

## Comment pulse
- Open firmware bucket is praised as transparency enabling research and updates, not a vulnerability — counterpoint: wording risks encouraging management to hide firmware instead.  
- Many see issues as systemic to low-cost OEM IP cameras; similar flaws reported in Zyxel devices and white‑label hardware reused across ecosystems.  
- Strong advice to isolate cameras on IoT VLANs, block internet, disable UPnP, or flash open firmware like Thingino to regain control.  

## LLM perspective
- View: AI-assisted reversing turns commodity IoT devices into high-yield targets by compressing weeks of firmware analysis into hours for mid-level attackers.  
- Impact: Vendors must assume rapid bug discovery post-release; relying on obscurity or slow patch pipelines becomes untenable, especially with internet-exposed cameras.  
- Watch next: Independent CNAs or metrics beyond raw CVE counts may be needed to prevent vendors gaming security posture through under-reporting.
