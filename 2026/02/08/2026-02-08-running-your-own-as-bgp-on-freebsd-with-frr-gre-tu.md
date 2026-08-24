# Running Your Own As: BGP on FreeBSD with FRR, GRE Tunnels, and Policy Routing

- Score: 130 | [HN](https://news.ycombinator.com/item?id=46934266) | Link: https://blog.hofstede.it/running-your-own-as-bgp-on-freebsd-with-frr-gre-tunnels-and-policy-routing/

### TL;DR

An operator explains how to obtain an ASN and IPv6 /48 through a sponsoring RIPE LIR, create RPKI records, and announce provider-independent addresses from a FreeBSD VM. FRR peers with two upstreams, filters bogons, limits prefixes, and steers traffic using communities and AS-path prepending; GRE/GIF tunnels distribute subnets to remote hosts. A reject route prevents aggregate loops, while PF handles firewalling, MSS clamping, reply symmetry, and source-based selection between two FIBs so provider and personal IPv6 coexist. Commenters suggested DN42 for safe practice and debated cost, accessibility, and simpler overlays.

### Comment pulse

- DN42 offers private address space, WireGuard peering, and real routing protocols for learning without announcing routes to the public internet.
- Ownership drew disagreement: some valued migration-stable public addresses—counterpoint: others preferred DNS plus WireGuard overlays and questioned RIPE’s individual-access barriers.
- One commenter cited roughly €75 yearly ASN costs and cheap transit; another flagged unexplained disabling of checksum and segmentation offloads.

### LLM perspective

- View: The design is coherent, but assumes fluency in registry policy, BGP hygiene, tunnels, firewalls, and failure recovery.
- Impact: Small operators gain portable addressing and multihoming; they assume responsibility for security, availability, abuse handling, and path performance.
- Watch next: ROA validity, route leaks, tunnel MTUs, offload behavior, asymmetric paths, upstream failover, FIB regressions, and resource costs.
