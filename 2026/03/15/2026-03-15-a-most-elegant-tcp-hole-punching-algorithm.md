# A most elegant TCP hole punching algorithm

- Score: 205 | [HN](https://news.ycombinator.com/item?id=47384032) | Link: https://robertsdotpm.github.io/cryptography/tcp_hole_punching.html

### TL;DR
The article presents a deterministic TCP hole punching scheme that needs only the peer’s IP: both sides independently derive all parameters (time bucket, port list, punch timing) from local time. A shared “bucket” is computed from the current timestamp with clock-skew tolerance, then used as a PRNG seed to pick identical source ports; non-blocking sockets spam SYNs, and a simple leader/follower handshake selects the winning connection. It’s explicitly a testing tool, trading coverage for simplicity and relying on NATs that preserve source ports, which many commenters question; discussion centers on real-world NAT behavior, practicality vs. complexity, and the argument that IPv6 is the true fix.

---

### Comment pulse
- NAT port preservation is a fragile assumption → many CPEs, CG-NATs randomize ports or even egress IPs, so success rates may be low — counterpoint: author knowingly trades coverage for simplicity.  
- If peers already exchange IPs, they could also agree on ports or brute-force multiple ones → the minimal extra complexity may not justify this scheme’s constraints.  
- TCP hole punching seems unreliable on real hardware; UDP works better → some want standardized in-band signaling or just widespread IPv6 instead of clever NAT workarounds.

---

### LLM perspective
- View: Clever deterministic parameter derivation is valuable for reproducible experiments, but shouldn’t be mistaken for a generally robust P2P connectivity solution.  
- Impact: Most useful to networking researchers, protocol designers, and people debugging NAT behavior; less so to mainstream app developers behind CG-NAT.  
- Watch next: Empirical success-rate studies across router models, CG-NATs, and ISPs; comparisons with STUN/TURN and IPv6-based alternatives.
