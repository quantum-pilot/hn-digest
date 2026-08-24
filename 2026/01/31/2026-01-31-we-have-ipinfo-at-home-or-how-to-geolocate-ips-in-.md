# We have ipinfo at home or how to geolocate IPs in your CLI using latency

- Score: 194 | [HN](https://news.ycombinator.com/item?id=46834953) | Link: https://blog.globalping.io/we-have-ipinfo-at-home-or-how-to-geolocate-ips-in-your-cli-using-latency/

### TL;DR

A Globalping demo estimates an IP’s location from low-latency traceroutes across community probes. It samples five probes per continent, then defaults to 50 within the winning continent, country or US state, progressively reporting country, state and nearest city. The last responding hop handles targets that block ICMP, and one VPN example matched IPinfo’s Miami result. The author warns that random coverage causes neighboring-country errors, the method fails in sparse regions, and production use needs about 500 probes per phase. Commenters positioned latency mainly as verification for existing geolocation.

### Comment pulse

- Production practitioners said routing asymmetry, anycast and CDN behavior defeat distance models; useful inference requires dense probes near the target.
- Latency works better for servers than consumer networks and for checking prior location data; traceroute may locate only an upstream router.
- Adversaries can delay or spoof responses, while adaptive probe selection or HTTP-based models may reduce cost and routing noise.

### LLM perspective

- View: Latency is a physical signal, not a coordinate system; Internet routing makes nearest-probe heuristics opportunistic.
- Impact: Operators gain a lightweight anomaly check, but treating city output as ground truth can misroute or misattribute traffic.
- Watch next: Calibrated accuracy by network type, deterministic probe coverage, spoof resistance, confidence scoring and comparisons with trained trilateration.
