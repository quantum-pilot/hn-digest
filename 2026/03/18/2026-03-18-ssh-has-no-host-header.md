# SSH has no Host header

- Score: 151 | [HN](https://news.ycombinator.com/item?id=47421828) | Link: https://blog.exe.dev/ssh-host-header

### TL;DR
SSH lacks a Host-like header, so exe.dev can’t demux SSH to many customer VMs on shared IPv4 the way HTTP reverse proxies do. They instead allocate a small pool of IPv4 addresses, reuse each IP across users, and route SSH via a proxy that keys on (destination IP, client SSH key) to select the right VM. HN debates IPv6-only options, jump hosts, port- or SRV-based routing, and deeper limitations of SSH’s protocol and key/certificate design.

### Comment pulse
- IPv6-only pricing sounds attractive, but commenters and the author report real-world IPv6 unreliability at ISPs and datacenters, so products must assume IPv4 first.  
- Others propose classic solutions—jump/bastion hosts, per-user ports, SRV records—but these either hurt the zero-config ssh hostname UX or break on firewalls/middleboxes.  
- Another thread critiques SSH’s ad-hoc protocol and bare keys, debating whether certificate-style constraints meaningfully improve security, privacy, and key-reuse hygiene.

### LLM perspective
- View: Their (IP, user-key) routing is a pragmatic hack: operationally complex, but delivers a clean mental model for customers.  
- Impact: Makes “SSH by hostname” viable on constrained IPv4, which similar multi-tenant VM platforms or PaaS providers may emulate.  
- Watch next: Better SSH SNI-like extensions or standardized SRV/jump-host support could generalize this pattern without bespoke control planes.
