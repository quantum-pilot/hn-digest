# Some interesting stuff I found on IX LANs

- Score: 134 | [HN](https://news.ycombinator.com/item?id=45370882) | Link: https://blog.benjojo.co.uk/post/ixp-bad-broadcast-packets-interesting

### TL;DR

The author’s bgp.tools monitors broadcast and multicast traffic on internet-exchange LANs, exposing widespread edge-router misconfiguration. Discovery protocols leak device details; DHCP can enable targeted redirection; IPv6 advertisements can unintentionally provide transit; routing, management, desktop-discovery, legacy, and typo-triggered DNS traffic escape onto shared fabrics. Many packets have predictable MAC destinations or ports, so exchanges could block them with ACLs or at least monitor them. Commenters supplied similar incidents and explained how complex VLANs, stale configuration, or bad patching bridge inappropriate devices into peering networks.

### Comment pulse

- Operators recalled OSPF adjacency and STP failures, showing these leaks are practical rather than merely theoretical.
- LLDP’s operational usefulness divided commenters because public IX exposure turns helpful discovery data into attack surface.

### LLM perspective

- View: IX fabrics are shared hostile LANs; enterprise-friendly defaults become liabilities when edge ports inherit them.
- Impact: Leaks expose topology, management surfaces, or routing control to unrelated networks and sometimes adversaries.
- Watch next: IX adoption of default-deny filters, quarantine testing, and participant alerts with measurable remediation rates.
