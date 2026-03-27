# DOOM Over DNS

- Score: 188 | [HN](https://news.ycombinator.com/item?id=47490705) | Link: https://github.com/resumex/doom-over-dns

## TL;DR
A .NET port of shareware Doom is split into about 1,964 compressed chunks and stored entirely in DNS TXT records hosted on Cloudflare. A PowerShell 7 script reconstructs the WAD and DLLs at runtime purely via DNS queries, loading everything directly into memory without touching disk. The repo includes tools to publish data across one or more Cloudflare zones, handle free-tier limits, and resume uploads. HN loves the hack but debates abuse of infrastructure and the misleading “over DNS” phrasing.

---

## Comment pulse
- Clever, but ethically gray → abusing DNS as free storage erodes the “honor system” and could push providers toward more policing—counterpoint: tiny PoC; Cloudflare already serves larger assets free.
- Misleading title → DNS is used only as storage; computation happens locally. Similar feats possible via dnsfs; speculative talk of ultra-slow “DNS-based compute.”
- Long tradition of protocol bending → recalls Dan Kaminsky’s DNS SSH tunneling, pingfs over ICMP, and whimsical data-storage stunts like the Harder Drive video.

---

## LLM perspective
- View: This is a precise, educational demo of treating infrastructure protocols as generic content-addressable storage.
- Impact: Raises awareness for operators about nontraditional load patterns on DNS, and for devs about protocol flexibility and abuse.
- Watch next: Provider responses in ToS/rate limits, follow-up hacks over ICMP/other control planes, and security tools flagging such unconventional traffic.
