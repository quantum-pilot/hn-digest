# DynIP – Dynamic DNS with RFC 2136, IPv6, DNSSEC, and BYOD

- Score: 316 | [HN](https://news.ycombinator.com/item?id=48276363) | Link: https://dynip.dev/

### TL;DR

DynIP is a hosted dynamic-DNS service targeting modern homelabs and fleets: roughly 60-second propagation, native RFC 2136/TSIG plus HTTP updates, dual-stack and IPv6-only records, DNSSEC, custom-domain delegation, router-specific snippets, and support for private APN addresses. Its author describes a hidden PowerDNS primary with geographically separated secondaries that validate and forward updates, plus a container updater and free tier. HN welcomed standards support but noted mature alternatives such as deSEC and self-hosted BIND, requested IPv6 prefix-delegation updates, reported onboarding bugs, and argued Tailscale can replace DDNS for private access.

### Comment pulse

- IPv6 prefix delegation is a notable gap → deSEC can replace a rotating network prefix while preserving each host’s interface identifier.
- Standards enable exit options → BIND and Kubernetes external-dns already support RFC 2136, making self-hosting viable when operational simplicity matters less.
- Tailscale can remove private DDNS needs → overlay naming handles personal access — counterpoint: public services still require globally resolvable endpoints.

### LLM perspective

- **View:** DynIP’s differentiation is integration quality around open DNS standards, not a proprietary protocol; that lowers client lock-in.
- **Impact:** Private-APN support simplifies cellular fleets, but public DNS records containing internal addresses can expose naming and topology metadata.
- **Watch next:** Fix registrar glue and confirmation flows, add prefix delegation, publish uptime, audits, limits, browser compatibility, and disaster-recovery details.
