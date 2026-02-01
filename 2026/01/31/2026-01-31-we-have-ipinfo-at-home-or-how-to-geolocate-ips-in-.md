# We have ipinfo at home or how to geolocate IPs in your CLI using latency

- Score: 194 | [HN](https://news.ycombinator.com/item?id=46834953) | Link: https://blog.globalping.io/we-have-ipinfo-at-home-or-how-to-geolocate-ips-in-your-cli-using-latency/

### TL;DR
A developer built an open-source CLI that geolocates IPs by measuring latency and traceroute from a distributed probe network (Globalping), instead of relying on registry/GeoIP databases that VPNs can lie to. The tool narrows location in phases: continent → country → (if US) state → nearby city, picking the lowest-latency probes and matching ipinfo’s VPN case studies like “Bahamas” IPs actually in Miami. It’s accurate when probe coverage is dense, weaker at borders and sparsely covered regions, and intended as a demo, not production.

---

### Comment pulse
- Demo, not product → Author says accuracy really needs hundreds of probes per phase; ideas raised for gradient-descent-style probing to cut probe count.
- Research angle → DEFCON work used HTTP latency + ML to handle routing non-linearity, yielding continent-level attribution and sandbox/malware geofencing use-cases.
- Industry experience → Trilateration often fails on the internet; latency works best to verify existing geo data, mostly for infrastructure IPs, not consumer access networks—counterpoint: spoofing and traceroute games are possible but rare.

---

### LLM perspective
- View: Latency-based geolocation is a strong validation and debugging signal, but unreliable as a sole truth source for broad IP space.
- Impact: Most useful to infra providers, security teams, and VPN detectives; end users gain a sanity-check tool, not an oracle.
- Watch next: Better probe selection algorithms, HTTP-based measurements, ML models, and published benchmarks against commercial GeoIP and VPN exit nodes.
