# Running Your Own As: BGP on FreeBSD with FRR, GRE Tunnels, and Policy Routing

- Score: 130 | [HN](https://news.ycombinator.com/item?id=46934266) | Link: https://blog.hofstede.it/running-your-own-as-bgp-on-freebsd-with-frr-gre-tunnels-and-policy-routing/

### TL;DR
A hobbyist shows how to run a real public Autonomous System from a single FreeBSD VM: get an IPv6 /48 and ASN via a sponsoring RIPE LIR, peer over BGP using FRR, and distribute subnets to remote servers with GRE/GIF tunnels. A clever dual-FIB setup plus PF policy routing lets a VPS simultaneously use both provider-assigned and personal IPv6 space without spoofing issues. HN discusses hobbyist alternatives like DN42, address-allocation politics, and lighter-weight tunnel/BGP setups.

---

### Comment pulse
- Use DN42 instead of the public internet → full BGP practice with private addressing and WireGuard, no RIR paperwork or global-impact misconfigurations.  
- Individual IPv6 PI feels too gated → RIR policies expect multihoming and “serious” use, frustrating tinkerers—counterpoint: via sponsoring LIRs it’s ~€75/year and practically attainable.  
- Owning space vs overlays → some see public PI as overkill given WireGuard/Nebula and dynamic DNS; others value provider-independence, reputation stability, and clean routing.

---

### LLM perspective
- View: This design is a strong reference for small ASes: FRR + FreeBSD FIBs + PF covers most “one-AS, many-hosters” needs.  
- Impact: Hobby operators and small businesses gain routing autonomy without buying routers; colos and VPS providers may see more BGP-savvy customers.  
- Watch next: Comparable Linux guides (FRR + VRFs), managed “personal ASN” services, and simpler tooling around RPKI, bogon lists, and tunnel provisioning.
