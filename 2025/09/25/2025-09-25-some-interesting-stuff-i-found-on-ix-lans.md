# Some interesting stuff I found on IX LANs

- Score: 134 | [HN](https://news.ycombinator.com/item?id=45370882) | Link: https://blog.benjojo.co.uk/post/ixp-bad-broadcast-packets-interesting

- TL;DR
    - Internet exchanges are shared Layer-2 peering LANs. bgp.tools sniffs broadcast/multicast and routinely finds misconfigured defaults on IX ports: discovery beacons (LLDP/CDP/MNDP), auto-addressing (DHCP/DHCPv6, IPv6 RA), interior routing (OSPF/IS-IS/RIP), MPLS LDP, STP/loop probes, consumer protocols (UPnP, mDNS, NetBIOS), exposed management (MikroTik Winbox), Cisco DNS broadcasts, and SONiC’s “ping all IPv6 nodes.” Fallout: traffic redirection, info leaks, wasted resources. Fixes: enforce MAC/L3 ACLs on IX fabrics and disable noisy features. HN adds IX primers, war stories, and debate over LLDP and simplicity.

- Comment pulse
    - Misconfiguration on IXs is common → defaults (STP, DHCP, OSPF) leak via accidental bridging; unmanaged switches can worsen. — counterpoint: simplicity beats fragile over-engineering.
    - What an IX is → shared L2 peering LAN where routers run BGP; complex transport means VLAN mistakes can bridge office gear onto the exchange.
    - LLDP on IXs → great for cable tracing, but exposes metadata; normally not forwarded, yet leaks occur when segments are mis-bridged.

- LLM perspective
    - View: Treat peering ports as hostile L2 → disable discovery, DHCP/RA, interior routing, STP; apply MAC/L3 ACLs on IX fabrics.
    - Impact: Fewer route leaks, hijacks, and accidental transit; less CPU churn from SONiC pings and unsolicited multicast/broadcast.
    - Watch next: Vendors and IX policy → disable IPv6 RA on peering, fix SONiC arp_update; deploy standard ACL templates and quarantine tests.
