# DynIP – Dynamic DNS with RFC 2136, IPv6, DNSSEC, and BYOD

- Score: 316 | [HN](https://news.ycombinator.com/item?id=48276363) | Link: https://dynip.dev/

### TL;DR
DynIP is a modern dynamic DNS service aimed at homelabs and infrastructure teams, built on real DNS standards instead of proprietary update APIs. It supports RFC 2136 with TSIG (so many routers and external-dns work natively), dual-stack IPv4/IPv6, optional per‑zone DNSSEC, and “bring your own domain” via NS delegation. Architecture uses a hidden primary with geographically split secondaries and sub‑minute propagation. Discussion compares it to deSEC and self‑hosted BIND, notes UX rough edges, and positions it alongside—rather than instead of—tools like Tailscale.

---

### Comment pulse
- Standards-focused DDNS → TSIG, IPv6, DNSSEC, BYOD and Docker agent; users compare to deSEC and request IPv6 prefix delegation support — counterpoint: not implemented yet.  
- UX/compatibility gaps → password reset flow confusing when logged in, Firefox Focus blocked scripts, Hover registrar reported missing NS glue.  
- Alternatives and coexistence → many self-host BIND with RFC 2136 or use k8s external-dns; others rely on Tailscale/WireGuard, keeping DDNS only for public services.

---

### LLM perspective
- View: Nicely targeted midpoint between hobby DDNS and full DNS hosting, emphasizing standards compliance and router-native integration.  
- Impact: Most interesting for homelabbers, MSPs, fleet operators, and small infra teams that want DNSSEC/IPv6 without running their own auth stack.  
- Watch next: Support for IPv6 prefix delegation, more registrar how-tos, production external-dns recipes, and reliability metrics vs incumbents like deSEC and Cloudflare.
